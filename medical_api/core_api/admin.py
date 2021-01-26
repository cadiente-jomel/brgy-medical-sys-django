from django.contrib import admin
from .models import CitizenPersonalInfo, MedicalRecord, MedicalHistory, TreatmentReceive, CitizenContactInfo, CitizenProfile, CovidStatus, TravelHistory, ContactTrace
# Register your models here.
admin.site.register(CitizenPersonalInfo)
admin.site.register(MedicalRecord)
admin.site.register(MedicalHistory)
admin.site.register(TreatmentReceive)
admin.site.register(CitizenContactInfo)
admin.site.register(CitizenProfile)
admin.site.register(CovidStatus)
admin.site.register(TravelHistory)
admin.site.register(ContactTrace)
