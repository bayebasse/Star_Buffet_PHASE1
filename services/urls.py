from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_traiteurs, name='service-page'),

]