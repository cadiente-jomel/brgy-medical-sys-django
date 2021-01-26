from django.contrib import admin
from .models import CitizenPersonalInfo, MedicalRecord, MedicalHistory, TreatmetReceive
# Register your models here.
admin.site.register(CitizenPersonalInfo)
admin.site.register(MedicalRecord)
admin.site.register(MedicalHistory)
admin.site.register(TreatmetReceive)
