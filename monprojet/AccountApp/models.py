from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator

class User(AbstractUser):
    pass
class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Doctor(User):
    license_number= models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6)])
    phone= models.CharField(max_length=8, )
    specialties = models.ManyToManyField('Specialty', related_name='doctors')
    def __str__(self):
      return self.get_full_name() or self.username
class Patient(User):
    national_id= models.CharField(max_length=6, unique=True, validators=[RegexValidator(r"^\d{8}$", message="La CIN doit contenir 8 chiffres.")])
    phone= models.CharField(max_length=8)
    birth_date= models.DateField()
    def __str__(self):
     return self.get_full_name() or self.username
    




# Create your models here.
