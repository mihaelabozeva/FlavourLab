
from django import forms
from .models import Experiment


class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = [
            "title",
            "ingredients",
            "observations",
            "result",
        ]
        labels = {
            "title": "Experiment title",
            "ingredients": "Ingredients used",
            "observations": "Cooking observations",
            "result": "Experiment result",
        }
        help_texts = {
            "ingredients": "Select all ingredients used in your experiment.",
            "observations": "Record what you noticed while cooking.",
            "result": "Describe what worked, what did not, and what you learned.",
        }
        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "e.g. Testing lemon with basil",
            }),
            "ingredients": forms.CheckboxSelectMultiple(),
            "observations": forms.Textarea(attrs={
                "placeholder": "What did you notice?",
                "rows": 4,
            }),
            "result": forms.Textarea(attrs={
                "placeholder": "What was the result of your experiment?",
                "rows": 4,
            }),
        }
