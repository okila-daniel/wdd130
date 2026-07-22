from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property

        exclude = ["landlord"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),

            "house_type": forms.Select(attrs={"class": "form-select"}),

            "university": forms.TextInput(attrs={"class": "form-control"}),

            "county": forms.TextInput(attrs={"class": "form-control"}),

            "town": forms.TextInput(attrs={"class": "form-control"}),

            "address": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Street, Estate, Building..."
            }),

            "price": forms.NumberInput(attrs={"class": "form-control"}),

            "bedrooms": forms.NumberInput(attrs={"class": "form-control"}),

            "bathrooms": forms.NumberInput(attrs={"class": "form-control"}),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5
            }),

            "distance_to_university": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "latitude": forms.HiddenInput(),

            "longitude": forms.HiddenInput(),

            "available": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }