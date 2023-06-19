from django import forms
from .models import Shortener

class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(
        widget=forms.URLInput(attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"})
    )
    url_index = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Give an Index to your URL (Optional)"})
    )

    class Meta:
        model = Shortener
        fields = ('long_url', 'url_index',)

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by index or URL'})) # SearcForm in MYURL's to query based on index or URL