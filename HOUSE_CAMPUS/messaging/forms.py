from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["subject", "message"]

        widgets = {
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Subject"
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Write your message here..."
            }),
        }