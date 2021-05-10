from django import forms
from .models import Provider

class ProviderForm(forms.ModelForm):
    Meta:
        model = Provider
        fields = "__all__"