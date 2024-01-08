# gmail_sender/forms.py

from django import forms
from .models import EmailDetail

class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailDetail
        fields = ['to_email', 'subject', 'message']
