from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import (
    CitizenPersonalInfoSerializer, MedicalRecordSerializer, MedicalHistorySerializer, TreatmentReceiveSerializer, CitizenContactInfoSerializer, CitizenProfileSerializer, CovidStatusSerializer, TravelHistorySerializer, ContactTraceSerializer
)
from core_api.models import (
    CitizenPersonalInfo, MedicalRecord,
    MedicalHistory, TreatmentReceive,
    CitizenContactInfo, CitizenProfile,
    CovidStatus, TravelHistory, ContactTrace)


class CitizenPersonalViewset(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = CitizenPersonalInfo.objects.all()
    serializer_class = CitizenPersonalInfoSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CitizenPersonal(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = CitizenPersonalInfo.objects.all()
    serializer_class = CitizenPersonalInfoSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class MedicalRecordViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MedicalRecord(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class MedicalHistoryViewset(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MedicalHistory(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TreatmentReceiveViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = TreatmentReceive.objects.all()
    serializer_class = TreatmentReceiveSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TreatmentReceive(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = TreatmentReceive.objects.all()
    serializer_class = TreatmentReceiveSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CitizenContactInfoViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = CitizenContactInfo.objects.all()
    serializer_class = CitizenContactInfoSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CitizenContactInfo(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = CitizenContactInfo.objects.all()
    serializer_class = CitizenContactInfoSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CitizenProfileViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = CitizenProfile.objects.all()
    serializer_class = CitizenProfileSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CitizenProfile(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = CitizenProfile.objects.all()
    serializer_class = CitizenProfileSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CovidStatusViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = CovidStatus.objects.all()
    serializer_class = CovidStatusSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CovidStatus(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = CovidStatus.objects.all()
    serializer_class = CovidStatusSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TravelHistoryViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = TravelHistory.objects.all()
    serializer_class = TravelHistorySerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TravelHistory(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = TravelHistory.objects.all()
    serializer_class = TravelHistorySerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ContactTraceViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = ContactTrace.objects.all()
    serializer_class = ContactTraceSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ContactTrace(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = ContactTrace.objects.all()
    serializer_class = ContactTraceSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
