from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_us, name='about'),
    path('contact/', views.contact_us, name='contact')
]