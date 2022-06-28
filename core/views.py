from django.shortcuts import render
from .models import Dog
from .forms import DogModelForm, ContactForm
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


def contact(request, id):
    #TODO: Use get_or_404
    dog = Dog.objects.get(id=id)

    form = ContactForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            messages.success(request, 'Email sent!')
            form = ContactForm()

        else:
            messages.error(request, 'Error!')

    context = {'form': form, 'id': id, 'dog': dog}

    return render(request, 'contact.html', context)
