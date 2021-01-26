from django.db import models
from PIL import Image
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


class CitizenContactInfo(models.Model):
    citizen = models.ForeignKey(
        CitizenPersonalInfo, on_delete=models.CASCADE, related_name='citizen_contact')
    email = models.EmailField()
    contact_no = models.CharField(
        'contact number', max_length=20, help_text='include the prefix')

    def __str__(self):
        return f'{self.citizen.first_name} {self.citizen.last_name} contact info'


class CitizenProfile(models.Model):
    citizen = models.ForeignKey(
        CitizenPersonalInfo, on_delete=models.CASCADE, related_name='citizen_profile')
    profile_pic = models.ImageField(
        upload_to='profile', default='default.jpg', blank=None)

    def __str__(self):
        return f'{self.citizen.first_name} {self.citizen.last_name} contact info'

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.profile_pic.path)
        if img.width < 300 or img.height > 300:
            output = (300, 300)
            img.thumbnail(output)
            img.save(self.profile_pic.path)


class MedicalRecord(models.Model):
    citizen = models.ForeignKey(
        CitizenPersonalInfo, on_delete=models.CASCADE, related_name='citizen_medical')
    weight = models.IntegerField(help_text='in kg')
    blood_pressure = models.CharField(max_length=10)
    temperature = models.IntegerField(help_text='in celsius')
    pulse_rate = models.IntegerField()

    def __str__(self):
        return f'{self.citizen.first_name} {self.citizen.last_name} record'


class MedicalHistory(models.Model):
    medical_rec = models.ManyToManyField(
        MedicalRecord, related_name='medical_history', verbose_name='medical record')
    history = models.CharField(max_length=400)

    def __str__(self):
        citizen = self.medical_rec.all().first().citizen
        return f'{citizen.first_name} {citizen.last_name} History'

    class Meta:
        verbose_name_plural = 'Medical Histories'


class TreatmetReceive(models.Model):
    medical_rec = models.ManyToManyField(
        MedicalRecord, related_name='treatment_record', verbose_name='treatment record')
    treatment = models.CharField(max_length=400)

    def __str__(self):
        citizen = self.medical_rec.all().first().citizen
        return f'{citizen.first_name} {citizen.last_name} treatment received'

    class Meta:
        verbose_name_plural = 'Treatment Received'
