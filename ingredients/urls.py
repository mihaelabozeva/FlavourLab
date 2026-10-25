from django.urls import path
from ingredients.views import IngredientListView, IngredientDetailView, IngredientCreateView, IngredientUpdateView, \
    IngredientDeleteView, FlavourNoteCreateView, FlavourNoteListView, FlavourNoteDeleteView

app_name = 'ingredients'
urlpatterns = [path("", IngredientListView.as_view(), name='list'),
               path("add/", IngredientCreateView.as_view(), name='create'),
               path("notes/", FlavourNoteListView.as_view(), name="note_list"),
               path("notes/add/", FlavourNoteCreateView.as_view(), name="note_create"),
               path("notes/<int:pk>/delete/", FlavourNoteDeleteView.as_view(), name="note_delete"),
               path("<int:pk>/edit/", IngredientUpdateView.as_view(), name="update"),
               path("<int:pk>/delete/", IngredientDeleteView.as_view(), name="delete"),
               path("<int:pk>/", IngredientDetailView.as_view(), name='detail')]

