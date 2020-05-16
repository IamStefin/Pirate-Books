from django import forms
from .models import SubmitBook

class UploadForm(forms.ModelForm):
    document  = forms.FileField(label="")
    class Meta:
        model = SubmitBook
        fields = ('title', 'document', 'author' )