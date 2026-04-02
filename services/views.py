from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from .models import Traiteur, Specialite
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def liste_traiteurs(request):
    traiteurs = Traiteur.objects.all()

    return render(request, 'liste.html', {'traiteurs': traiteurs})


def detail_traiteurs(request, id):
    details = get_object_or_404(Traiteur, id=id)
    return render(request, 'detail.html', {'details': details})


class SignInView(CreateView):
   form_class = UserCreationForm          
   success_url = reverse_lazy('home')     
   template_name = 'registration/inscription_user.html'

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
        image = request.FILES.get("image")

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
