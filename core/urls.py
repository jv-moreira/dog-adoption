from django.urls import path
from .views import index, register, contact


urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('contact', contact, name='contact')
]
