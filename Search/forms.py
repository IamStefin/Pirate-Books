from django import forms

class SearchForm(forms.Form):
    term = forms.CharField(label="")