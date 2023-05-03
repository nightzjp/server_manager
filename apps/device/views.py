from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import mixins

from device import models
from device import serializers
from device import filters


class AlgorithmViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = models.Algorithm.objects.order_by("-create_at")
    serializer_class = serializers.AlgorithmSerializers
    filterset_class = filters.AlgorithmFilter


class DeviceViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = models.Device.objects.order_by("-create_at")
    serializer_class = serializers.DeviceSerializers
    filterset_class = filters.DeviceFilter
