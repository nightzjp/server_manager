from django.contrib import admin
from simpleui.admin import AjaxAdmin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin

from system import models


@admin.register(models.UserProxy)
class UserProxyAdmin(UserAdmin):
    list_display = [
        "username",
        "email",
        "is_active",
        "is_staff",
        "last_login",
    ]
    list_filter = []
    search_fields = []
    readonly_fields = ["is_active", "is_staff"]
    list_per_page = 10
    top_html = ' <el-alert title="请谨慎操作用户相关信息!" type="warning"></el-alert>'
    change_list_template = "admin/system/userproxy/change_list.html"


@admin.register(LogEntry)
class LogEntryAdmin(AjaxAdmin):
    list_display = ["user", "content_type", "message", "action_time"]
    list_filter = ["action_time"]
    readonly_fields = ["action_time", "user", "content_type"]
    exclude = ["change_message", "action_flag", "object_repr", "object_id"]
    list_per_page = 10
    top_html = ' <el-alert title="日志信息只读!" type="warning"></el-alert>'
    change_list_template = "admin/system/logentry/change_list.html"

    @staticmethod
    def message(obj):
        return obj.get_change_message()

    message.short_description = "操作信息"


@admin.register(models.MqttConfig)
class MqttConfigAdmin(AjaxAdmin):
    list_display = [
        "m_client_id",
        "m_ip",
        "m_port",
        "m_username",
        "m_status",
    ]
    readonly_fields = ["create_by", "delete_at"]
    top_html = ' <el-alert title="为适配多平台，可增加多个mqtt配置!" type="success"></el-alert>'
    change_list_template = "admin/system/mqttconfig/change_list.html"

    def save_model(self, request, obj, form, change):
        obj.create_by = request.user.username
        return super(MqttConfigAdmin, self).save_model(request, obj, form, change)


@admin.register(models.HttpConfig)
class HttpConfigAdmin(AjaxAdmin):
    list_display = [
        "h_ip",
        "h_port",
        "h_username",
        "h_period",
        "h_status",
    ]
    readonly_fields = ["create_by", "delete_at"]
    top_html = ' <el-alert title="为适配多平台，可增加多个http配置!" type="success"></el-alert>'
    change_list_template = "admin/system/httpconfig/change_list.html"

    def save_model(self, request, obj, form, change):
        obj.create_by = request.user.username
        return super(HttpConfigAdmin, self).save_model(request, obj, form, change)


@admin.register(models.NetworkConfig)
class NetworkConfigAdmin(AjaxAdmin):
    list_display = ["n_name", "n_ip", "n_mask", "n_gateway", "n_dns"]
    top_html = ' <el-alert title="系统初始化自动读取网络配置，不可手动操作!" type="warning"></el-alert>'
    change_list_template = "admin/system/networkconfig/change_list.html"


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
    top_html = ' <el-alert title="系统信息后台自动获取，不可手动操作!" type="warning"></el-alert>'
    change_list_template = "admin/system/systeminfo/change_list.html"
