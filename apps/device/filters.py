from django_filters import rest_framework as filters

from device import models


class AlgorithmFilter(filters.FilterSet):
    class Meta:
        model = models.Algorithm
        fields = ["ai_name"]


class DeviceFilter(filters.FilterSet):
    class Meta:
        model = models.Device
        fields = ["d_name", "d_ip"]
