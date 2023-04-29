from django.contrib import admin
from simpleui.admin import AjaxAdmin
from import_export.admin import ImportExportActionModelAdmin

from device import models


@admin.register(models.Algorithm)
class AlgorithmAdmin(AjaxAdmin):
    list_display = ["ai_name", "ai_status", "ai_is_used", "ai_source", "ai_describe"]
    list_filter = ["ai_is_used", "ai_source"]
    search_fields = ["ai_name"]
    list_editable = ["ai_status"]
    readonly_fields = ["create_by", "delete_at", "ai_source", "ai_is_used"]
    change_list_template = "admin/device/algorithm/change_list.html"


@admin.register(models.Device)
class DeviceAdmin(ImportExportActionModelAdmin, AjaxAdmin):
    list_display = [
        "d_name",
        "d_ip",
        "d_address",
        "d_source",
        "d_type",
        "d_brand",
        "d_status",
        "d_channel",
        "d_rtsp",
    ]
    search_fields = ["d_name"]
    list_filter = [
        "d_source",
        "d_type",
        "d_brand",
        "d_status",
    ]
    readonly_fields = [
        "create_by",
        "delete_at",
        "d_source",
        "d_status",
        "d_format",
        "d_last_login",
        "d_last_logout",
    ]
    change_list_template = "admin/device/device/change_list.html"
