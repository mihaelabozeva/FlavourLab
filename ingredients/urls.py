from django.urls import path
from ingredients.views import IngredientListView, IngredientDetailView, IngredientCreateView, IngredientUpdateView, \
    IngredientDeleteView

app_name = 'ingredients'
urlpatterns = [path("", IngredientListView.as_view(), name='list'),
               path("add/", IngredientCreateView.as_view(), name='create'),
               path("<int:pk>/edit/", IngredientUpdateView.as_view(), name="update"),
               path("<int:pk>/delete/", IngredientDeleteView.as_view(), name="delete"),
               path("<int:pk>/", IngredientDetailView.as_view(), name='detail')]

