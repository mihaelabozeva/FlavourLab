
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Experiment
from .forms import ExperimentForm


class ExperimentListView(ListView):
    model = Experiment
    template_name = "experiments/list.html"
    context_object_name = "experiments"


class ExperimentDetailView(DetailView):
    model = Experiment
    template_name = "experiments/detail.html"
    context_object_name = "experiment"


class ExperimentCreateView(CreateView):
    model = Experiment
    form_class = ExperimentForm
    template_name = "experiments/form.html"
    success_url = reverse_lazy("experiments:list")


class ExperimentUpdateView(UpdateView):
    model = Experiment
    form_class = ExperimentForm
    template_name = "experiments/form.html"
    context_object_name = "experiment"
    success_url = reverse_lazy("experiments:list")


class ExperimentDeleteView(DeleteView):
    model = Experiment
    template_name = "experiments/delete.html"
    context_object_name = "experiment"
    success_url = reverse_lazy("experiments:list")
