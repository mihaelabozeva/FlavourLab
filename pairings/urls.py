from django.urls import path
from . import views

app_name = "pairings"

urlpatterns = [
    path("", views.PairingListView.as_view(), name="list"),
    path("add/", views.PairingCreateView.as_view(), name="create"),
    path("<int:pk>/", views.PairingDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.PairingUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.PairingDeleteView.as_view(), name="delete"),
]
