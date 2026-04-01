from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_traiteurs, name='service-page'),
    path('traiteurs/<int:id>/', views.detail_traiteurs, name='detail-page')
]