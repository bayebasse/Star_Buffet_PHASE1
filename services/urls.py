from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('liste/', views.liste_traiteurs, name='service-page'),
    path('traiteurs/<int:id>/', views.detail_traiteurs, name='detail-page'),
    path('inscription/', views.inscription_traiteur, name='inscription'),
    path('inscription-user/', views.SignInView.as_view(), name='user-inscription'),
]