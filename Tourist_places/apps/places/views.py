from django.shortcuts import render,get_object_or_404
from .models import DestinosTuristicos
from datetime import date

# Create your views here.

def destinoShowDescription(request, myID):
    place = get_object_or_404(DestinosTuristicos ,id = myID)
    context = {
        'place': place,
    }
    return render(request,'destinations.html',context)

def index(request):

    dests = DestinosTuristicos.objects.all()
    today = date.today()
    context = {
        'dests':dests,
    }
    return render(request, "index.html", context)