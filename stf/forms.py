from django import forms

from .models import *

class ResumeForm(forms.ModelForm):
    class Meta:
        model=JobSeeker
        fields=['Name','Email','Mobile','resume']