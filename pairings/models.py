from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q


class Pairing(models.Model):
    first_ingredient = models.ForeignKey(
        'ingredients.Ingredient',
        on_delete=models.CASCADE,
        related_name='pairings_as_first',
    )
    second_ingredient = models.ForeignKey(
        'ingredients.Ingredient',
        on_delete=models.CASCADE,
        related_name='pairings_as_second',
    )
    explanation = models.TextField()

    class Meta:
        ordering = ['first_ingredient__name', 'second_ingredient__name']

    def clean(self):
        if not (self.first_ingredient_id and self.second_ingredient_id):
            return

        if self.first_ingredient_id == self.second_ingredient_id:
            raise ValidationError("An ingredient cannot be paired with itself.")

        duplicates = Pairing.objects.filter(
            Q(first_ingredient_id=self.first_ingredient_id,
              second_ingredient_id=self.second_ingredient_id)
            | Q(first_ingredient_id=self.second_ingredient_id,
                second_ingredient_id=self.first_ingredient_id)
        ).exclude(pk=self.pk)

        if duplicates.exists():
            raise ValidationError("This pairing already exists.")

    def __str__(self):
        return f"{self.first_ingredient} + {self.second_ingredient}"