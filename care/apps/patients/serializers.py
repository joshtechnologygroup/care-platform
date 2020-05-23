from rest_framework import serializers
from django.utils.translation import ugettext as _
from rest_framework import serializers as rest_serializers
from rest_framework import exceptions as rest_exceptions
from apps.patients import models as patient_models
from apps.facility import models as facility_models


class PatientSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = patient_models.Patient
        fields = (
            "id",
            "facility",
            "nearest_facility",
            "meta_info",
            "name",
            "age",
            "gender",
            "phone_number",
            "address",
            "date_of_birth",
            "year_of_birth",
            "nationality",
            "passport_no",
            "aadhar_no",
            "is_medical_worker",
            "blood_group",
            "contact_with_confirmed_carrier",
            "state",
            "district",
            "contact_with_suspected_carrier",
            "estimated_contact_date",
            "past_travel",
            "is_active",
            "countries_travelled_old",
            "countries_travelled",
            "date_of_return",
            "present_health",
            "ongoing_medication",
            "has_SARI",
            "local_body",
            "disease_status",
            "number_of_aged_dependents",
            "created_by",
            "number_of_chronic_diseased_dependents",
            "patient_search_id",
            "date_of_receipt_of_information",
            "patient_group",
        )
        extra_kwargs = {
            "facility": {"required": True},
            "nearest_facility": {"required": True},
            "state": {"required": True},
            "district": {"required": True},
        }

    def validate(self, attrs):
        patient_group = patient_models.Patient.objects.filter(
            attrs.get("aadhar_no",attrs.get('passport_no'))).first()
        if patient_group:
            raise rest_exceptions.PermissionDenied()
        return attrs


class PatientGroupSerializer(rest_serializers.ModelSerializer):

    class Meta:
        model = patient_models.PatientGroup
        fields = (
            "id","name","description","created_at",)
        read_only_fields=("created_at",)    