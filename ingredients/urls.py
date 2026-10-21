from django.urls import path
from ingredients.views import IngredientListView, IngredientDetailView

app_name = 'ingredients'
urlpatterns = [path("", IngredientListView.as_view(), name='list'),
               path("<int:pk>/", IngredientDetailView.as_view(), name='detail')]

