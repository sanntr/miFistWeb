from django.urls import path
from . import views

urlpatterns = [
   path('article', views.repons_aticles, name="article"),
   path('', views.forms, name='busqueda')
]
