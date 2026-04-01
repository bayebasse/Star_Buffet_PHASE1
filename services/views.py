from django.shortcuts import render

# Create your views here.

from .models import Traiteur

def liste_traiteurs(request):
    traiteurs = Traiteur.objects.all()
    return render(request, 'liste.html', {'traiteurs': traiteurs})