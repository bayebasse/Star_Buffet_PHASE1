from django.db import models




class Specialite(models.Model):
    nom=models.CharField(max_length=30)
    def __str__(self):
        return self.nom

class Traiteur(models.Model):
    nomcomplet=models.CharField(max_length=200)
    specialites=models.ManyToManyField(Specialite)
    description=models.TextField()
    adresse=models.CharField(max_length=200)
    est_actif=models.BooleanField()
    email=models.EmailField()
    datedecreation=models.DateTimeField(auto_now_add=True)
    telephone=models.CharField(max_length=9)
    image=models.URLField(blank=True,null=True)

    def __str__(self):
        return self.nomcomplet


