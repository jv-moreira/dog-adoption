from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    created_at = models.DateField('Created', auto_now_add=True)
    updated_at = models.DateField('Updated', auto_now=True)
    is_active = models.BooleanField('Active', default=True)

    class Meta:
        abstract = True


class Breed(Base):
    name = models.CharField('Name', max_length=100)

    class Meta:
        verbose_name = 'Breed'
        verbose_name_plural = 'Breeds'

    def __str__(self):
        return self.name


class Dog(Base):
    GENDER_CHOICES = (
        ('Male', 'M'),
        ('Female', 'F')
    )

    name = models.CharField('Name', max_length=100)
    age = models.IntegerField('Age')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    sex = models.CharField('Sex', max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    image = StdImageField('Image', upload_to='dogs', variations={'thumb': (124, 124)})

    class Meta:
        verbose_name = 'Dog'
        verbose_name_plural = 'Dogs'

    def __str__(self):
        return self.name

