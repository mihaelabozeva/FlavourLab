from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class Pairing(models.Model):
    first_ingredient=models.ForeignKey('ingredients.Ingredient', on_delete=models.CASCADE, related_name='first_ingredient')
    second_ingredient=models.ForeignKey('ingredients.Ingredient', on_delete=models.CASCADE, related_name='second_ingredient')
    explanation=models.TextField()

    def clean(self):
        if (
                self.first_ingredient_id
                and self.second_ingredient_id
                and self.first_ingredient_id == self.second_ingredient_id
        ):
            raise ValidationError(
                "An ingredient cannot be paired with itself."
            )

    def __str__(self):
        return (
            f"{self.first_ingredient} + "
            f"{self.second_ingredient}"
        )