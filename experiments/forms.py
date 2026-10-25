from django import forms
from .models import Experiment

class ExperimentForm(forms.ModelForm):
    created_at = forms.DateTimeField(
        label="Created at",
        required=False,
        disabled=True,
    )
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["created_at"].initial = self.instance.created_at
        else:
            self.fields.pop("created_at")