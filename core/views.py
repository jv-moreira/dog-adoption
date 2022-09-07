from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Dog
from .forms import DogModelForm, ContactForm, FindForm
from django.contrib import messages


def index(request):
    form = FindForm(request.POST or None)

    dogs = Dog.objects.all()

    if str(request.method) == 'POST':
        if form.is_valid():
            print(form.cleaned_data['breed'])
            print(form.cleaned_data['age'])
            print(form.cleaned_data['sex'])
            return find(request, form.cleaned_data['breed'], form.cleaned_data['age'], form.cleaned_data['sex'])

    context = {
        'dogs': dogs,
        'form': form
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
    dog = get_object_or_404(Dog, id=id)

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


def find(request, breed=None, age=None, sex=None):
    if breed is not None and age is not None and sex is not None:
        dogs = get_list_or_404(Dog, breed__name=breed, age=age, sex=sex)
    else:
        dogs = Dog.objects.all()

    context = {'dogs': dogs}

    return render(request, 'find.html', context)
