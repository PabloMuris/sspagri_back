from django import forms
from .models import Site


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['created_by','name','country','members','timezone','area']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome do site"}),
            "country": forms.Select(attrs={"class": "form-select"}),
            "members": forms.SelectMultiple(attrs={"class": "form-multiselect"}),
            "timezone": forms.TextInput(attrs={"class": "form-control"}),
            "area": forms.Textarea(attrs={"class": "form-control"}),  # poderia ser widget GIS também
        }