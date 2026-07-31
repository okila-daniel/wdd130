from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class StudentRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control form-control-lg"

        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "phone",
            "whatsapp_number",
            "password1",
            "password2",
        )

        widgets = {
            "first_name": forms.TextInput(attrs={
                "placeholder": "First Name"
            }),
            "last_name": forms.TextInput(attrs={
                "placeholder": "Last Name"
            }),
            "username": forms.TextInput(attrs={
                "placeholder": "Username"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Email Address"
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "Phone Number"
            }),
            "whatsapp_number": forms.TextInput(attrs={
                "placeholder": "WhatsApp Number"
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)

        user.role = "student"
        user.university = "Maasai Mara University"
        user.county = "Narok"
        user.town = "Narok"

        if commit:
            user.save()

        return user

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