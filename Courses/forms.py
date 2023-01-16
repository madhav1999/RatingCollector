from django import forms
from .models import Coursedata


class rating(forms.ModelForm):
    class Meta:
        model = Coursedata
        fields = ["comments", ]
