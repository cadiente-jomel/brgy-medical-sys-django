from core_api.models import CitizenPersonalInfo, MedicalRecord, MedicalHistory, TreatmentReceive, CitizenContactInfo, CitizenProfile, CovidStatus, TravelHistory, ContactTrace
from rest_framework import serializers


class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = '__all__'


class TreatmentReceiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentReceive
        fields = '__all__'


class MedicalRecordSerializer(serializers.ModelSerializer):
    medical_history = MedicalHistorySerializer(many=True, read_only=True)
    treatment_record = TreatmentReceiveSerializer(many=True, read_only=True)
    # citizen = serializers.PrimaryKeyRelatedField(
    #     queryset=MedicalRecord.objects.all(), source='citizen')

    def create(self, validated_data):
        med = MedicalRecord(**validated_data)
        return med

    class Meta:
        model = MedicalRecord
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


class CitizenPersonalInfoSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    citizen_profile = CitizenProfileSerializer(many=True, read_only=True)
    citizen_contact = CitizenContactInfoSerializer(
        many=True, read_only=True)
    covid_status = CovidStatusSerializer(many=True, read_only=True)
    contact_trace = ContactTraceSerializer(many=True, read_only=True)
    travel_history = TravelHistorySerializer(many=True, read_only=True)
    citizen_medical = MedicalRecordSerializer(many=True, read_only=True)
    # contact_information = CitizenContactInfoSerializer(
    #     many=True, read_only=True)
    # citizen_rofile = CitizenProfileSerializer(many=True, read_only=True)
    # medical_history = MedicalHistorySerializer(many=True, read_only=True)

    class Meta:
        model = CitizenPersonalInfo
        fields = ['id', 'first_name', 'last_name', 'age', 'birthdate', 'gender',
                  'address', 'civil_status', 'occupation', 'citizen_profile',
                  'citizen_contact', 'covid_status', 'contact_trace',
                  'travel_history', 'citizen_medical']
