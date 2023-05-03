from rest_framework import serializers

from system import models


class MqttConfigSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.MqttConfig
        fields = [
            "m_status",
            "m_client_id",
            "m_ip",
            "m_port",
            "m_username",
            "m_password",
        ]


class HttpConfigSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.HttpConfig
        fields = ["h_status", "h_ip", "h_port", "h_username", "h_password", "h_period"]


class NetWorkConfigSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.NetworkConfig
        fields = ["n_name", "n_ip", "n_mask", "n_broadcast", "n_gateway", "n_dns"]


class SystemInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.SystemInfo
        fields = [
            "d_type",
            "d_id",
            "d_mac",
            "d_firmware_version",
            "d_machine_version",
            "d_algorithm_version",
            "d_ffmpeg_version",
            "d_config",
        ]
