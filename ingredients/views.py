from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ingredients.forms import IngredientForm
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

class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredients/form.html"
    success_url = reverse_lazy("ingredients:list")

class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredients/form.html"
    success_url = reverse_lazy("ingredients:list")

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "ingredients/delete.html"
    context_object_name = "ingredient"
    success_url = reverse_lazy("ingredients:list")