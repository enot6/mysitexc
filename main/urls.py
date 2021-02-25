from django.urls import path
from . import views

urlpatterns = [
    path('', views.solsys, name='home'),
    path('solarsystem', views.solsys, name='home2'),
    path('secondpage', views.about, name='about'),
    path('mercury', views.MercuryPage, name='mercury'),
    path('venus', views.VenusPage, name='venus'),
    path('earth', views.EarthPage, name='earth'),
    path('mars', views.MarsPage, name='mars'),
    path('jupiter', views.JupiterPage, name='jupiter'),
    path('saturn', views.SaturnPage, name='saturn'),
    path('uranus', views.UranusPage, name='uranus'),
]