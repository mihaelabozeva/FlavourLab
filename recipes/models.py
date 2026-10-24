from django.db import models

from ingredients.models import Ingredient


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    instructions = models.TextField()
    ingredients = models.ManyToManyField('ingredients.Ingredient', related_name='recipes')

    def __str__(self):
        return self.name