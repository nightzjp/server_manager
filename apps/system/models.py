from django.db import models
from simplepro.components import fields

from public.models import BaseModel
from utils import constant


class MqttConfig(BaseModel):
    """Mqtt配置"""

    m_status = models.BooleanField(default=False, verbose_name="是否启用")
    m_client_id = models.CharField(
        max_length=32, null=True, blank=True, verbose_name="客户端唯一标识"
    )
    m_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="服务器地址")
    m_port = models.CharField(max_length=5, null=True, blank=True, verbose_name="端口")
    m_username = models.CharField(
        max_length=16, null=True, blank=True, verbose_name="用户名"
    )
    m_password = models.CharField(
        max_length=16, null=True, blank=True, verbose_name="密码"
    )

    class Meta:
        verbose_name = "Mqtt配置"
        verbose_name_plural = verbose_name


class HttpConfig(BaseModel):
    """Http配置"""

    h_status = models.BooleanField(default=False, verbose_name="是否启用")
    h_ip = models.CharField(max_length=32, null=True, blank=True, verbose_name="服务器地址")
    h_port = models.CharField(max_length=5, null=True, blank=True, verbose_name="端口")
    h_username = models.CharField(
        max_length=16, null=True, blank=True, verbose_name="用户名"
    )
    h_password = models.CharField(
        max_length=16, null=True, blank=True, verbose_name="密码"
    )
    h_period = models.SmallIntegerField(default=0, verbose_name="同步周期")

    class Meta:
        verbose_name = "HTTP配置"
        verbose_name_plural = verbose_name


class NetworkConfig(BaseModel):
    """网络配置"""

    n_name = models.CharField(max_length=16, null=True, blank=True, verbose_name="网口名称")
    n_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="IP地址")
    n_mask = models.CharField(max_length=16, null=True, blank=True, verbose_name="子网掩码")
    n_broadcast = models.CharField(
        max_length=16, null=True, blank=True, verbose_name="广播地址"
    )
    n_gateway = models.GenericIPAddressField(null=True, blank=True, verbose_name="默认网关")
    n_dns = models.GenericIPAddressField(null=True, blank=True, verbose_name="DNS配置")

    class Meta:
        verbose_name = "网络配置"
        verbose_name_plural = verbose_name


class SystemInfo(BaseModel):
    """设备信息"""

    d_type = models.CharField(max_length=32, null=True, blank=True, verbose_name="设备型号")
    d_id = models.CharField(max_length=32, null=True, blank=True, verbose_name="设备ID")
    d_mac = models.CharField(max_length=32, null=True, blank=True, verbose_name="Mac地址")
    d_firmware_version = models.CharField(
        max_length=8, null=True, blank=True, verbose_name="固件版本"
    )
    d_machine_version = models.CharField(
        max_length=9, null=True, blank=True, verbose_name="一体机版本"
    )
    d_algorithm_version = models.CharField(
        max_length=8, null=True, blank=True, verbose_name="算法软件版本"
    )
    d_ffmpeg_version = models.CharField(
        max_length=8, null=True, blank=True, verbose_name="拉流软件版本"
    )
    d_config = models.SmallIntegerField(
        choices=constant.S_CONFIG, default=0, verbose_name="抓拍图片上传配置"
    )

    class Meta:
        verbose_name = "设备信息"
        verbose_name_plural = verbose_name
