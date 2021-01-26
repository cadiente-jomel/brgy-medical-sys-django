from django.contrib import admin
from .models import CitizenPersonalInfo, MedicalRecord, MedicalHistory, TreatmetReceive, CitizenContactInfo, CitizenProfile
# Register your models here.
admin.site.register(CitizenPersonalInfo)
admin.site.register(MedicalRecord)
admin.site.register(MedicalHistory)
admin.site.register(TreatmetReceive)
admin.site.register(CitizenContactInfo)
admin.site.register(CitizenProfile)
