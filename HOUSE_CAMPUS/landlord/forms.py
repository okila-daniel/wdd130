from django import forms
from .models import LandlordApplication


class LandlordApplicationForm(forms.ModelForm):
    class Meta:
        model = LandlordApplication
        fields = [
            "phone",
            "national_id",
            "university",
            "county",
            "town",
            "number_of_properties",
            "id_document",
        ]

        widgets = {
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number"
            }),

            "national_id": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "National ID / Passport"
            }),

            "university": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "University"
            }),

            "county": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "County"
            }),

            "town": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Town"
            }),

            "number_of_properties": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Number of Properties"
            }),

            "id_document": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),
        }