from django import forms
from .models import Shortener

class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(
        widget=forms.URLInput(attrs={"class": "form-control form-control-lg custom-field", "placeholder": "Your URL to shorten"})
    )
    url_index = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg custom-field", "placeholder": "Index to URL (Optional)"})
    )
    url_alias = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg custom-field", "placeholder": "Custom Alias (Optional)"})
    )
    class Meta:
        model = Shortener
        fields = ('long_url', 'url_index','url_alias',)


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by index or URL'})) # SearcForm in MYURL's to query based on index or URL