from django.contrib import admin
from simpleui.admin import AjaxAdmin

from system import models


@admin.register(models.MqttConfig)
class MqttConfigAdmin(AjaxAdmin):
    list_display = [
        "m_status",
        "m_client_id",
        "m_ip",
        "m_port",
        "m_username",
        "m_password",
    ]


@admin.register(models.HttpConfig)
class HttpConfigAdmin(AjaxAdmin):
    list_display = [
        "h_status",
        "h_ip",
        "h_port",
        "h_username",
        "h_password",
        "h_period",
    ]


@admin.register(models.NetworkConfig)
class NetworkConfigAdmin(AjaxAdmin):
    list_display = ["n_name", "n_ip", "n_mask", "n_gateway", "n_dns"]


@admin.register(models.SystemInfo)
class SystemInfoAdmin(AjaxAdmin):
    list_display = [
        "d_type",
        "d_id",
        "d_mac",
        "d_firmware_version",
        "d_machine_version",
        "d_algorithm_version",
        "d_ffmpeg_version",
        "d_config",
    ]
