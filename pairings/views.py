from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Pairing
from .forms import PairingForm


class PairingListView(ListView):
    model = Pairing
    template_name = "pairings/list.html"
    context_object_name = "pairings"
    queryset = Pairing.objects.select_related(
        "first_ingredient",
        "second_ingredient",
    )


class PairingDetailView(DetailView):
    model = Pairing
    template_name = "pairings/detail.html"
    context_object_name = "pairing"


class PairingCreateView(SuccessMessageMixin, CreateView):
    model = Pairing
    form_class = PairingForm
    template_name = "pairings/form.html"
    success_url = reverse_lazy("pairings:list")
    success_message = "Pairing created successfully."


class PairingUpdateView(SuccessMessageMixin,UpdateView):
    model = Pairing
    form_class = PairingForm
    template_name = "pairings/form.html"
    success_url = reverse_lazy("pairings:list")
    success_message = "Pairing updated."


class PairingDeleteView(SuccessMessageMixin,DeleteView):
    model = Pairing
    template_name = "pairings/delete.html"
    context_object_name = "pairing"
    success_url = reverse_lazy("pairings:list")
    success_message = "Pairing deleted."
