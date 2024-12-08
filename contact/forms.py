from django import forms
from .models import EventContact

class EventContactForm(forms.ModelForm):
    class Meta:
        model = EventContact
        fields = ['event_name', 'organizer_name', 'email', 'phone', 'query']
        widgets = {
            'query': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter your message or query'}),
        }
