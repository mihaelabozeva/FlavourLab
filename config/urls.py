from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
path('', RedirectView.as_view(pattern_name='ingredients:list', permanent=False), name='home'),
    path('admin/', admin.site.urls),
    path('ingredients/', include('ingredients.urls')),
    path('pairings/', include('pairings.urls')),
    path('experiments/', include('experiments.urls')),

]
