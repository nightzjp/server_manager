from django.contrib import admin
from simpleui.admin import AjaxAdmin
from import_export.admin import ExportActionModelAdmin
from import_export.formats.base_formats import XLS, XLSX, CSV, JSON

from device import models
from device import resources
from utils.cr import check_rtsp_stream


@admin.register(models.Algorithm)
class AlgorithmAdmin(AjaxAdmin):
    list_display = ["ai_name", "ai_status", "ai_is_used", "ai_source", "ai_describe"]
    list_filter = ["ai_is_used", "ai_source"]
    search_fields = ["ai_name"]
    list_editable = ["ai_status"]
    readonly_fields = ["create_by", "delete_at", "ai_source", "ai_is_used"]
    top_html = ' <el-alert title="为了保证系统稳定性，不可轻易对模型进行编辑操作!" type="warning"></el-alert>'
    change_list_template = "admin/device/algorithm/change_list.html"
    
    def save_model(self, request, obj, form, change):
        obj.create_by = request.user.username
        return super(AlgorithmAdmin, self).save_model(request, obj, form, change)


@admin.register(models.Device)
class DeviceAdmin(ExportActionModelAdmin, AjaxAdmin):
    list_display = [
        "d_name",
        "d_ip",
        "d_address",
        "d_source",
        "d_type",
        "d_brand",
        "d_status",
        "d_channel",
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
    resource_class = resources.DeviceResource
    formats = [XLS, XLSX, CSV, JSON]
    top_html = ' <el-alert title="设备不可编辑!" type="warning"></el-alert>'
    change_list_template = "admin/device/device/change_list.html"

    def save_model(self, request, obj, form, change):
        obj.create_by = request.user.username
        if not obj.d_rtsp:
            obj.d_rtsp = self.parse_rtsp_address(obj)
        obj.d_status = check_rtsp_stream(obj.d_rtsp)
        return super(DeviceAdmin, self).save_model(request, obj, form, change)

    @staticmethod
    def parse_rtsp_address(obj: models.Device):
        """根据摄像头类型获取对应rtsp地址"""
        if obj.d_brand == 0:  # 海康
            return f"rtsp://{obj.d_username}:{obj.d_password}@{obj.d_ip}:554/h264/ch0/main/av_stream"
        elif obj.d_brand == 1:  # 大华
            return f"rtsp://{obj.d_username}:{obj.d_password}@{obj.d_ip}:554/h264/ch1/main/av_stream"
        elif obj.d_brand == 2:  # 华为
            return f"rtsp://{obj.d_username}:{obj.d_password}@{obj.d_ip}:554/LiveMedia/ch1/Media1"
        elif obj.d_brand == 3:  # 宇视
            return f"rtsp://{obj.d_username}:{obj.d_password}@{obj.d_ip}:554/video1"
        else:  # 未知|自定义
            return f"rtsp://{obj.d_username}:{obj.d_password}@{obj.d_ip}:554"

