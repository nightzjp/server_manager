from django.contrib import admin
from simpleui.admin import AjaxAdmin
from import_export.admin import ImportExportActionModelAdmin

from device import models


@admin.register(models.Algorithm)
class AlgorithmAdmin(AjaxAdmin):
    list_display = ["ai_name", "ai_status", "ai_is_used", "ai_source", "ai_describe"]
    list_filter = ["ai_name", "ai_is_used", "ai_source"]
    list_editable = ["ai_status"]


@admin.register(models.Device)
class DeviceAdmin(ImportExportActionModelAdmin, AjaxAdmin):
    list_display = [
        "d_name",
        "d_ip",
        "d_address",
        "d_geo",
        "d_source",
        "d_type",
        "d_brand",
        "d_status",
        "d_format",
        "d_channel",
        "d_last_login",
        "d_last_logout",
    ]
    list_filter = [
        "d_name",
        "d_source",
        "d_type",
        "d_brand",
        "d_status",
        "d_format",
    ]
