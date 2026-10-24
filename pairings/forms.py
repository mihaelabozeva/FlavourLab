from django import forms

from pairings.models import Pairing


class PairingForm(forms.ModelForm):
    class Meta:
        model = Pairing
        fields = [
            "first_ingredient",
            "second_ingredient",
            "explanation",
        ]
        labels = {
            "first_ingredient": "First ingredient",
            "second_ingredient": "Second ingredient",
            "explanation": "Why do these ingredients work together?",
        }
        help_texts = {
            "first_ingredient": "Choose the first ingredient.",
            "second_ingredient": "Choose a different ingredient.",
            "explanation": "Explain how their flavours complement each other.",
        }
        widgets = {
            "explanation": forms.Textarea(attrs={
                "placeholder": (
                    "Explain why these ingredients work together..."
                ),
                "rows": 4,
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        first = cleaned_data.get("first_ingredient")
        second = cleaned_data.get("second_ingredient")

        if first and second and first == second:
            raise forms.ValidationError(
                "Choose two different ingredients for a pairing."
            )

        return cleaned_data
