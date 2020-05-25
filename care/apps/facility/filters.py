from django_filters import rest_framework as filters

from apps.facility import models as facility_models


class FacilityFilter(filters.FilterSet):
    code = filters.CharFilter(field_name="facility_code", lookup_expr="istartswith")
    name = filters.CharFilter(field_name="name", lookup_expr="istartswith")
    address = filters.CharFilter(field_name="address", lookup_expr="istartswith")
    facility_type_name = filters.CharFilter(
        field_name="facility_type__name", lookup_expr="istartswith"
    )
    owned_by_name = filters.CharFilter(
        field_name="owned_by__name", lookup_expr="istartswith"
    )
    total_patient = filters.RangeFilter(field_name="total_patient", lookup_expr="range")
    positive_patient = filters.RangeFilter(
        field_name="positive_patient", lookup_expr="range"
    )
    negative_patient = filters.RangeFilter(
        field_name="negative_patient", lookup_expr="range"
    )
    created_at = filters.DateTimeFromToRangeFilter(field_name="created_at")
    updated_at = filters.DateTimeFromToRangeFilter(field_name="updated_at")

    class Meta:
        model = facility_models.Facility
        fields = (
            "name",
            "code",
            "address",
            "district",
            "facility_type_name",
            "owned_by_name",
            "district",
            "total_patient",
            "positive_patient",
            "negative_patient",
            "created_at",
            "updated_at",
        )
