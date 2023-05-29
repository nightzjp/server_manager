from rest_framework import serializers

from device import models


class AlgorithmSerializers(serializers.ModelSerializer):
    """算法模型序列化器"""

    class Meta:
        model = models.Algorithm
        fields = [
            "uid",
            "ai_name",
            "ai_status",
            "ai_is_used",
            "ai_source",
            "ai_describe",
            "ai_file",
            "ai_source_id",
            "create_at",
        ]
        extra_kwargs = {
            "ai_source_id": {"read_only": True},
            "create_at": {"format": "%Y-%m-%d %H:%M:%S", "read_only": True},
        }


class DeviceSerializers(serializers.ModelSerializer):
    """设备序列化器"""

    class Meta:
        model = models.Device
        fields = [
            "uid",
            "d_name",
            "d_ip",
            "d_address",
            "d_geo",
            "d_source",
            "d_type",
            "d_brand",
            "d_status",
            "d_format",
            "d_username",
            "d_password",
            "d_rtsp",
            "d_channel",
            "d_last_login",
            "d_last_logout",
            "d_algorithm",
            "d_source_id",
            "create_at",
        ]
        extra_kwargs = {
            "d_source_id": {"read_only": True},
            "d_last_login": {"format": "%Y-%m-%d %H:%M:%S", "read_only": True},
            "d_last_logout": {"format": "%Y-%m-%d %H:%M:%S", "read_only": True},
            "create_at": {"format": "%Y-%m-%d %H:%M:%S", "read_only": True},
        }
