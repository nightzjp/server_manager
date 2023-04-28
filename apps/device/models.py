from django.db import models
from simplepro.components import fields

from public.models import BaseModel
from utils import constant


class Algorithm(BaseModel):
    """算法模型管理类"""

    ai_name = models.CharField(max_length=8, null=True, blank=True, verbose_name="模型名称")
    ai_status = models.BooleanField(default=False, verbose_name="是否启用")
    ai_is_used = models.SmallIntegerField(
        choices=constant.AI_IS_USED, default=0, verbose_name="使用状态"
    )
    ai_source = models.SmallIntegerField(
        choices=constant.AI_SOURCE, default=0, verbose_name="模型来源"
    )
    ai_describe = models.CharField(
        max_length=64, null=True, blank=True, verbose_name="模型描述"
    )
    ai_file = models.FileField(
        upload_to="ai", null=True, blank=True, verbose_name="模型文件"
    )

    class Meta:
        verbose_name = "算法模型管理类"
        verbose_name_plural = verbose_name


class Device(BaseModel):
    """设备视频源"""

    d_name = models.CharField(max_length=16, null=True, blank=True, verbose_name="设备名称")
    d_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="IP地址")
    d_address = models.CharField(
        max_length=128, null=True, blank=True, verbose_name="设备地址"
    )
    d_geo = models.CharField(max_length=64, null=True, blank=True, verbose_name="经纬度")
    d_source = models.SmallIntegerField(
        choices=constant.D_SOURCE, default=0, verbose_name="设备来源"
    )
    d_type = models.SmallIntegerField(
        choices=constant.D_TYPE, default=0, verbose_name="设备类型"
    )
    d_brand = models.SmallIntegerField(
        choices=constant.D_BRAND, default=0, verbose_name="设备品牌"
    )
    d_status = models.SmallIntegerField(
        choices=constant.D_STATUS, default=0, verbose_name="设备状态"
    )
    d_format = models.SmallIntegerField(
        choices=constant.D_FORMAT, default=0, verbose_name="流类型"
    )
    d_channel = models.SmallIntegerField(default=0, verbose_name="通道号")
    d_last_login = models.DateTimeField(blank=True, null=True, verbose_name="最后一次连接时间")
    d_last_logout = models.DateTimeField(blank=True, null=True, verbose_name="最后一次下线时间")
    d_algorithm = models.ManyToManyField(to="Algorithm")

    class Meta:
        verbose_name = "设备视频源"
        verbose_name_plural = verbose_name
