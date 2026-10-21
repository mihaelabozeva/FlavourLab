from django.contrib import admin

from ingredients.models import Ingredient, FlavourNote


# Register your models here.
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "intensity"]
    list_filter = ["category"]
    search_fields = ["name"]

@admin.register(FlavourNote)
class FlavourNoteAdmin(admin.ModelAdmin):
    ...