from django.urls import path
from .views import index, register, contact, find


urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('contact/<int:id>', contact, name='contact'),
    path("find/<str:breed>/<int:age>/<str:sex>", find, name='find')
]
