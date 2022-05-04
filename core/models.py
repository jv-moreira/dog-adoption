from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    created_at = models.DateField('Created', auto_now_add=True)
    updated_at = models.DateField('Updated', auto_now=True)
    is_active = models.BooleanField('Active', default=True)

    class Meta:
        abstract = True


class Dog(Base):
    BREEDS_CHOICES = (
        ('Akita', 'Akita'),
        ('American Foxhound', 'American Foxhound'),
        ('Australian Cattle Dog', 'Australian Cattle Dog'),
        ('Basset Hound', 'Basset Hound'),
        ('Beagle', 'Beagle'),
        ('Border Collie', 'Border Collie'),
        ('Boxer', 'Boxer'),
        ('Bulldog', 'Bulldog'),
        ('Chihuahua', 'Chihuahua'),
        ('Chow Chow', 'Chow Chow')
    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    name = models.CharField('Name', max_length=100)
    age = models.IntegerField('Age')
    breed = models.CharField('Breed', max_length=100, choices=BREEDS_CHOICES)
    sex = models.CharField('Sex', max_length=10, choices=GENDER_CHOICES)
    image = StdImageField('Image', upload_to='dogs', variations={'thumb': (124, 124)})

    class Meta:
        verbose_name = 'Dog'
        verbose_name_plural = 'Dogs'

    def __str__(self):
        return self.name

