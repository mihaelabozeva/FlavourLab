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
        error_messages = {
            "first_ingredient": {"required": "Please choose the first ingredient."},
            "second_ingredient": {"required": "Please choose the second ingredient."},
            "explanation": {"required": "Please explain why these ingredients work together."},
        }
        widgets = {
            "explanation": forms.Textarea(attrs={
                "placeholder": (
                    "Explain why these ingredients work together..."
                ),
                "rows": 4,
            }),
        }
