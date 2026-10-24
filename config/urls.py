from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingredients/', include('ingredients.urls')),
    path('pairings/', include('pairings.urls')),
    path('experiments/', include('experiments.urls')),

]
