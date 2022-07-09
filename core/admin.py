from django.contrib import admin
from .models import Dog, Breed


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'breed', 'image']
