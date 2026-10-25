from django.db.models import Count
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ingredients.forms import IngredientForm, IngredientFilterForm
from ingredients.models import Ingredient, FlavourNote


# Create your views here.
class IngredientListView(ListView):
    model = Ingredient
    template_name = "ingredients/list.html"
    context_object_name = "ingredients"

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related("flavour_notes")
        self.filter_form = IngredientFilterForm(self.request.GET)

        if self.filter_form.is_valid():
            data = self.filter_form.cleaned_data

            if data["q"]:
                queryset = queryset.filter(name__icontains=data["q"])

            if data["category"]:
                queryset = queryset.filter(category=data["category"])

            if data["note"]:
                queryset = queryset.filter(flavour_notes=data["note"])

            if data["sort"]:
                queryset = queryset.order_by(data["sort"])

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not hasattr(self, "filter_form"):
            self.filter_form = IngredientFilterForm(self.request.GET)
        context["filter_form"] = self.filter_form
        return context

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

class FlavourNoteListView(ListView):
    model = FlavourNote
    template_name = "ingredients/note_list.html"
    context_object_name = "notes"

    def get_queryset(self):
        return FlavourNote.objects.annotate(
            ingredient_count=Count("ingredients")
        ).order_by("name")


class FlavourNoteCreateView(CreateView):
    model = FlavourNote
    fields = ["name"]
    template_name = "ingredients/note_form.html"
    success_url = reverse_lazy("ingredients:note_list")

class FlavourNoteDeleteView(DeleteView):
    model = FlavourNote
    template_name = "ingredients/note_delete.html"
    context_object_name = "note"
    success_url = reverse_lazy("ingredients:note_list")