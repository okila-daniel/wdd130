from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "whatsapp_number",
            "university",
            "county",
            "town",
            "password1",
            "password2",
        )

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "whatsapp_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "254712345678",
                }
            ),
            "university": forms.TextInput(attrs={"class": "form-control"}),
            "county": forms.TextInput(attrs={"class": "form-control"}),
            "town": forms.TextInput(attrs={"class": "form-control"}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone",
            "whatsapp_number",
            "university",
            "county",
            "town",
            "profile_picture",
        )

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "whatsapp_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "254712345678",
                }
            ),
            "university": forms.TextInput(attrs={"class": "form-control"}),
            "county": forms.TextInput(attrs={"class": "form-control"}),
            "town": forms.TextInput(attrs={"class": "form-control"}),
        }