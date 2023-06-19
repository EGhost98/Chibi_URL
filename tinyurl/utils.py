from django.conf import settings
from random import choice
from string import ascii_letters, digits
import string


SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)
AVAILABLE_CHARS = string.digits + string.ascii_lowercase + string.ascii_uppercase


def create_random_code(chars=AVAILABLE_CHARS): # Generate Short URL
    return "".join([choice(chars) for _ in range(SIZE)])


def create_shortened_url(model_instance):
    random_code = create_random_code()
    model_class = model_instance.__class__
    if model_class.objects.filter(short_url=random_code).exists(): #if short_url generated exists
        return create_shortened_url(model_instance)
    return random_code