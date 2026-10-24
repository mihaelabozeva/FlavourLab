from django.contrib import admin

from experiments.models import Experiment


# Register your models here.
@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    ...
