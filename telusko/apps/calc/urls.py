from django.urls import path
from . import views

# URLs from app calc

urlpatterns = [
    path('',views.home ,name = 'home'),
    path('add',views.add,name='result'),
]
