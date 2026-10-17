from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class FlavourNote(models.Model):
    name=models.CharField(max_length=80, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    class Category(models.TextChoices):
        HERB = "herb", "Herb"
        SPICE = "spice", "Spice"
        FRUIT = "fruit", "Fruit"
        VEGETABLE = "vegetable", "Vegetable"
        DAIRY = "dairy", "Dairy"
        MEAT_FISH = "meat_fish", "Meat & Fish"
        GRAIN = "grain", "Grain"
        NUTS_SEEDS = "nuts_seeds", "Nuts & Seeds"
        OTHER = "other", "Other"

    name=models.CharField(max_length=80, unique=True)
    description=models.TextField()
    flavour_notes=models.ManyToManyField(FlavourNote, blank=True, related_name="ingredients")
    intensity=models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], help_text="1 - very mild, 5 - very strong")
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.OTHER)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

