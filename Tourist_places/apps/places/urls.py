from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:myID>", views.destinoShowDescription, name="descripcion"),
]