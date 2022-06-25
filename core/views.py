from django.shortcuts import render
from .models import Dog
from .forms import DogModelForm
from django.contrib import messages


def index(request):
    dogs = Dog.objects.all()
    context = {
        'dogs': dogs
    }

    return render(request, 'index.html', context)


def register(request):
    if str(request.method) == 'POST':
        form = DogModelForm(request.POST, request.FILES)
        if form.is_valid():
            dog = form.save()
            messages.success(request, 'Dog registered!')
        else:
            messages.error(request, 'Error!')
    else:
        form = DogModelForm()

    context = {'form': form}

    return render(request, 'register.html', context)
