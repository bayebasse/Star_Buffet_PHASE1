from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Traiteur

def liste_traiteurs(request):
    traiteurs = Traiteur.objects.all()
    return render(request, 'liste.html', {'traiteurs': traiteurs})

def detail_traiteurs(request, id):
    details = get_object_or_404(Traiteur, id=id)
    return render(request, 'detail.html', {'details': details})