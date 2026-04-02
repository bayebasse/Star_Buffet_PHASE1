from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from .models import Traiteur, Specialite
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def Specialite_cuisine(request):
    Les_Specialites=Specialite.objects.all()
    return render(request,'liste.html',{'specialite':Les_Specialites})

@login_required
def liste_traiteurs(request):
    traiteurs = Traiteur.objects.all()
    specialites=Specialite.objects.all()
    context={
        'specialite': specialites,
        'traiteur': traiteurs
    }
    return render(request, 'liste.html', context)

def detail_traiteurs(request, id):
    details = get_object_or_404(Traiteur, id=id)
    return render(request, 'detail.html', {'details': details})

class SignUpView(CreateView):
  form_class = UserCreationForm
  template_name = "registration/inscription.html"

def home(request):
    return render(request, 'index.html') 

def inscription_traiteur(request):

    specialites = Specialite.objects.all()

    if request.method == "POST":
        nom = request.POST.get("nomcomplet")
        email = request.POST.get("email")
        description = request.POST.get("description")
        adresse = request.POST.get("adresse")
        telephone = request.POST.get("telephone")
        image = request.POST.get("image")

        traiteur = Traiteur.objects.create(
            nomcomplet=nom,
            email=email,
            description=description,
            adresse=adresse,
            telephone=telephone,
            image=image
        )

        # MANY TO MANY
        specialites_ids = request.POST.getlist("specialites")
        traiteur.specialites.set(specialites_ids)

        return redirect('service-page')

    return render(request, 'inscription.html', {'specialites': specialites})
