from django.views.generic import ListView, DetailView
from ingredients.models import Ingredient


# Create your views here.
class IngredientListView(ListView):
    model = Ingredient
    template_name = "ingredients/list.html"
    context_object_name = "ingredients"

    def get_queryset(self):
        return super().get_queryset().prefetch_related("flavour_notes")

class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = "ingredients/detail.html"
    context_object_name = "ingredient"

    def get_queryset(self):
        return super().get_queryset().prefetch_related("flavour_notes")
