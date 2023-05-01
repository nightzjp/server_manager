from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import mixins

from system import models
from system import serializers
from system import filters


class MqttConfigViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = models.MqttConfig.objects.order_by("-create_at")
    serializer_class = serializers.MqttConfigSerializers
    filterset_class = filters.MqttConfigFilter


class HttpConfigViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = models.HttpConfig.objects.order_by("-create_at")
    serializer_class = serializers.HttpConfigSerializers
    filterset_class = filters.HttpConfigFilter


class NetWorkConfigViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = models.NetworkConfig.objects.order_by("-create_at")
    serializer_class = serializers.NetWorkConfigSerializers
    filterset_class = filters.NetWorkConfigFilter


class SystemInfoViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    queryset = models.SystemInfo.objects.order_by("-create_at")
    serializer_class = serializers.SystemInfoSerializers
    filterset_class = filters.SystemInfoFilter
