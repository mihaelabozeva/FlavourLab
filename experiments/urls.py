from django.urls import path
from . import views

app_name = "experiments"

urlpatterns = [
    path("", views.ExperimentListView.as_view(), name="list"),
    path("add/", views.ExperimentCreateView.as_view(), name="create"),
    path("<int:pk>/", views.ExperimentDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.ExperimentUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.ExperimentDeleteView.as_view(), name="delete"),
]
