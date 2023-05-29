from rest_framework.viewsets import mixins

from system import models
from system import serializers
from system import filters
from public.views import CustomGenericViewSet


class MqttConfigViewSet(
    CustomGenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = models.MqttConfig.objects.order_by("-create_at")
    serializer_class = serializers.MqttConfigSerializers
    filterset_class = filters.MqttConfigFilter


class HttpConfigViewSet(
    CustomGenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = models.HttpConfig.objects.order_by("-create_at")
    serializer_class = serializers.HttpConfigSerializers
    filterset_class = filters.HttpConfigFilter


class NetWorkConfigViewSet(CustomGenericViewSet, mixins.ListModelMixin):
    queryset = models.NetworkConfig.objects.order_by("-create_at")
    serializer_class = serializers.NetWorkConfigSerializers
    filterset_class = filters.NetWorkConfigFilter


class SystemInfoViewSet(
    CustomGenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin
):
    queryset = models.SystemInfo.objects.order_by("-create_at")
    serializer_class = serializers.SystemInfoSerializers
    filterset_class = filters.SystemInfoFilter
