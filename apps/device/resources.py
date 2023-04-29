import uuid

from import_export import resources, fields, widgets

from device import models
from utils import constant


class SourceWidget(widgets.CharWidget):
    def render(self, value, obj=None):
        return constant.D_SOURCE[value][1]


class TypeWidget(widgets.CharWidget):
    def render(self, value, obj=None):
        return constant.D_TYPE[value][1]


class BrandWidget(widgets.CharWidget):
    def render(self, value, obj=None):
        return constant.D_BRAND[value][1]


class FormatWidget(widgets.CharWidget):
    def render(self, value, obj=None):
        return constant.D_FORMAT[value][1]


class StatusWidget(widgets.CharWidget):
    def render(self, value, obj=None):
        return constant.D_STATUS[value][1]


class DeviceResource(resources.ModelResource):
    """设备自定义导入导出"""

    d_source = fields.Field(attribute="d_source", widget=SourceWidget())
    d_type = fields.Field(attribute="d_type", widget=TypeWidget())
    d_brand = fields.Field(attribute="d_brand", widget=BrandWidget())
    d_format = fields.Field(attribute="d_format", widget=FormatWidget())
    d_status = fields.Field(attribute="d_status", widget=StatusWidget())

    class Meta:
        model = models.Device
        fields = [
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
        ]

    def export(self, queryset=None, *args, **kwargs):
        """导出触发"""
        return super(DeviceResource, self).export(queryset, *args, **kwargs)

    def save_instance(self, instance, using_transactions=True, dry_run=False):
        """保存触发"""
        return super(DeviceResource, self).save_instance(
            instance, using_transactions, dry_run
        )

    def import_obj(self, obj, data, dry_run, **kwargs):
        """导入触发"""
        return super(DeviceResource, self).import_obj(obj, data, dry_run, **kwargs)

    def after_import(self, dataset, result, using_transactions, dry_run, **kwargs):
        return super(DeviceResource, self).after_import(
            dataset, result, using_transactions, dry_run, **kwargs
        )
