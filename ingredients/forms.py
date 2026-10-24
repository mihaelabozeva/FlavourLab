
from django import forms
from ingredients.models import Ingredient


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            "name",
            "description",
            "flavour_notes",
            "intensity",
            "category",
        ]
        labels = {
            "name": "Ingredient name",
            "description": "Description",
            "flavour_notes": "Flavour notes",
            "intensity": "Flavour intensity (1–5)",
            "category": "Category",
        }
        help_texts = {
            "intensity": "Choose from 1 (very mild) to 5 (very strong).",
            "flavour_notes": "Select all flavour notes that apply.",
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "e.g. Fresh basil",
                "class": "form-control",
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "Describe the ingredient...",
                "rows": 4,
                "class": "form-control",
            }),
            "flavour_notes": forms.CheckboxSelectMultiple(),
        }
