
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
        error_messages = {
            "name": {
                "required": "Please enter a name for the ingredient.",
                "unique": "An ingredient with this name already exists.",
                "max_length": "The name can be at most 80 characters long.",
            },
            "description": {
                "required": "Please describe the ingredient.",
            },
            "intensity": {
                "required": "Please choose an intensity from 1 to 5.",
                "min_value": "Intensity must be at least 1.",
                "max_value": "Intensity cannot be higher than 5.",
                "invalid": "Intensity must be a whole number.",
            },
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


class IngredientFilterForm(forms.Form):
    q = forms.CharField(
        required=False,
        label="Search",
        widget=forms.TextInput(attrs={
            "placeholder": "Search ingredients...",
        }),
    )

    category = forms.ChoiceField(
        required=False,
        label="Category",
        choices=[("", "All categories")] + list(
            Ingredient.Category.choices
        ),
    )

    note = forms.ModelChoiceField(
        required=False,
        label="Flavour note",
        queryset=None,
        empty_label="All flavour notes",
    )

    sort = forms.ChoiceField(
        required=False,
        label="Sort by",
        choices=[
            ("name", "Name (A–Z)"),
            ("-name", "Name (Z–A)"),
            ("intensity", "Intensity (low to high)"),
            ("-intensity", "Intensity (high to low)"),
        ],
        initial="name",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from .models import FlavourNote
        self.fields["note"].queryset = FlavourNote.objects.order_by("name")
