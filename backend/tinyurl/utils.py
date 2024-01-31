import hashlib
from baseconv import base62
import secrets

def get_unique_counter_value():
    from .models import Counter
    counter = Counter.objects.first()
    counter_value = counter.value
    counter.value += 1
    counter.save()
    return counter_value

def generate_random_bits(bits=10):
    random_int = secrets.randbits(bits)
    binary_string = bin(random_int)[2:]
    padded_binary_string = binary_string.zfill(bits)
    return padded_binary_string

def create_shortened_url(orignal_url):
    from .models import Shortener
    orignal_url += str(get_unique_counter_value())
    orignal_url += generate_random_bits()
    hashed_value = hashlib.md5(orignal_url.encode()).hexdigest()
    hashed_integer = int(hashed_value[:16], 16)
    encoded_value = base62.encode(hashed_integer)
    short_key = encoded_value[:6].rjust(6, '0')
    if Shortener.objects.filter(short_url=short_key).exists():
        return create_shortened_url(orignal_url)
    return short_key