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