from django.utils.translation import ugettext as _
from rest_framework import serializers as rest_serializers
from rest_framework import exceptions as rest_exceptions
from apps.patients import (
    constants as patient_constants,
    models as patient_models,
)
from apps.facility import models as facility_models


class PatientFacilitySerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = patient_models.PatientFacility
        fields = (
            "patient_status",
            "facility",
            "patient_facility_id",
        )
        read_only_fields = ("facility",)


class GenderField(rest_serializers.RelatedField):
    def to_representation(self, value):
        if value == 1:
            return 'Male'
        if value == 2:
            return 'Female'
        else:
            return 'Others'


class PatientListSerializer(rest_serializers.ModelSerializer):

    status = rest_serializers.SerializerMethodField()
    gender = GenderField(queryset=patient_models.Patient.objects.none())
    ownership_type = rest_serializers.CharField()
    facility_type = rest_serializers.CharField()
    facility_name = rest_serializers.CharField()
    facility_district = rest_serializers.CharField()

    class Meta:
        model = patient_models.Patient
        fields = (
            "icmr_id",
            "govt_id",
            "facility",
            "name",
            "gender",
            "year",
            "month",
            "phone_number",
            "address",
            "district",
            "cluster_group",
            "status",
            "covid_status",
            "clinical_status",
            "clinical_status_updated_at",
            "portea_called_at",
            "portea_able_to_connect",
            "facility_name",
            "facility_district",
            "facility_type",
            "ownership_type",
            "nearest_facility",
            "id",
            "date_of_birth",
            "year_of_birth",
            "nationality",
            "passport_no",
            "aadhar_no",
            "is_medical_worker",
            "blood_group",
            "contact_with_confirmed_carrier",
            "state",
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
            "number_of_aged_dependents",
            "created_by",
            "number_of_chronic_diseased_dependents",
            "patient_search_id",
            "date_of_receipt_of_information",
            "symptoms",
            "diseases",
            "current_facility",
        )
        extra_kwargs = {
            "facility": {"required": True},
            "nearest_facility": {"required": True},
            "state": {"required": True},
            "district": {"required": True},
        }
        read_only_fields = (
            "symptoms",
            "diseases",
        )

    def get_status(self, instance):
        if instance.patient_status == patient_constants.FACILITY_STATUS:
            return instance.facility_status
        return instance.patient_status


class PatientGroupSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = patient_models.PatientGroup
        fields = (
            "id",
            "name",
            "description",
            "created_at",
        )
        read_only_fields = ("created_at",)


class CovidStatusSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = patient_models.CovidStatus
        fields = (
            "id",
            "name",
            "description",
        )


class ClinicalStatusSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = patient_models.ClinicalStatus
        fields = (
            "id",
            "name",
            "description",
        )


class PatientStatusSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = patient_models.PatientStatus
        fields = ("id", "name", "description")


class PatientTimeLineSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = patient_models.PatientTimeLine
        fields = (
            "date",
            "description",
        )


class PatientSampleTestSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = patient_models.PatientSampleTest
        fields = (
            "id",
            "patient",
            "testing_lab",
            "doctor_name",
            "result",
            "date_of_sample",
            "date_of_result",
            "status_updated_at",
        )
