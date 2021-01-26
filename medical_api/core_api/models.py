from django.db import models
import uuid
# Create your models here.


class CitizenPersonalInfo(models.Model):
    SEX = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('Non-binary', 'Non-binary')
    ]
    CIVIL_STATUS = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('W', 'Widow')
    ]
    id = models.CharField(max_length=250, primary_key=True,
                          default=uuid.uuid4, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    birthdate = models.DateField()
    gender = models.CharField(max_length=150, choices=SEX)
    address = models.CharField(max_length=400)
    civil_status = models.CharField(max_length=15, choices=CIVIL_STATUS)
    occupation = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Citizen Personal Information'
