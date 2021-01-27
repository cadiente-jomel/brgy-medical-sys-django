from core_api.models import CitizenPersonalInfo, MedicalRecord, MedicalHistory, TreatmentReceive, CitizenContactInfo, CitizenProfile, CovidStatus, TravelHistory, ContactTrace
from rest_framework import serializers


class CitizenPersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenPersonalInfo
        fields = '__all__'


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'


class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = '__all__'


class TreatmentReceiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentReceive
        fields = '__all__'


class CitizenContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenContactInfo
        fields = '__all__'


class CitizenProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenProfile
        fields = '__all__'


class CovidStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidStatus
        fields = '__all__'


class TravelHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelHistory
        fields = '__all__'


class ContactTraceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactTrace
        fields = '__all__'
