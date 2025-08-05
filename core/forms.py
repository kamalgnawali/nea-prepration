# core/forms.py
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'तपाईंको नाम'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'तपाईंको इमेल'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'तपाईंको सन्देश'}),
        }
