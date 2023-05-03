from django_filters import rest_framework as filters

from system import models


class MqttConfigFilter(filters.FilterSet):
    class Meta:
        model = models.MqttConfig
        fields = []


class HttpConfigFilter(filters.FilterSet):
    class Meta:
        model = models.HttpConfig
        fields = []


class NetWorkConfigFilter(filters.FilterSet):
    class Meta:
        model = models.NetworkConfig
        fields = []


class SystemInfoFilter(filters.FilterSet):
    class Meta:
        model = models.SystemInfo
        fields = []
