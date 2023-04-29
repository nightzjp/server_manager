from django.db import models
from django.contrib.auth.models import User
from simplepro.components import fields

from public.models import BaseModel
from utils import constant, validators


class UserProxy(User):
    """用户模型代理类"""

    class Meta:
        proxy = True
        verbose_name = "用户代理类"
        verbose_name_plural = verbose_name


class MqttConfig(BaseModel):
    """Mqtt配置"""

    m_status = fields.SwitchField(default=False, verbose_name="是否启用")
    m_client_id = fields.CharField(
        max_length=32,
        blank=False,
        verbose_name="客户端唯一标识",
        placeholder="请输入客户端id",
        show_word_limit=True,
        prefix_icon="el-icon-lock",
    )
    m_ip = fields.CharField(
        max_length=16,
        blank=False,
        verbose_name="IP地址",
        placeholder="请输入MQTT服务器地址",
        prefix_icon="el-icon-edit",
        validators=[validators.validate_ipv4_address],
    )
    m_port = fields.InputNumberField(min_value=1024, max_value=65535, verbose_name="端口")
    m_username = fields.CharField(
        max_length=16,
        blank=False,
        verbose_name="用户名",
        placeholder="请输入用户名",
        show_word_limit=True,
        prefix_icon="el-icon-user",
    )
    m_password = fields.CharField(
        max_length=16,
        blank=False,
        verbose_name="密码",
        placeholder="请输入密码",
        show_word_limit=True,
        show_password=True,
        prefix_icon="el-icon-lock",
    )

    class Meta:
        verbose_name = "Mqtt配置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.m_ip


class HttpConfig(BaseModel):
    """Http配置"""

    h_status = fields.SwitchField(default=False, verbose_name="是否启用")
    h_ip = fields.CharField(
        max_length=16,
        blank=False,
        verbose_name="服务器地址",
        placeholder="请输入HTTP服务器地址",
        prefix_icon="el-icon-edit",
        validators=[validators.validate_ipv4_address],
    )
    h_port = fields.InputNumberField(min_value=1024, max_value=65535, verbose_name="端口")
    h_username = fields.CharField(
        max_length=16,
        blank=False,
        verbose_name="用户名",
        placeholder="请输入用户名",
        show_word_limit=True,
        prefix_icon="el-icon-user",
    )
    h_password = fields.CharField(
        max_length=16,
        blank=False,
        verbose_name="密码",
        placeholder="请输入密码",
        show_word_limit=True,
        show_password=True,
        prefix_icon="el-icon-lock",
    )
    h_period = fields.InputNumberField(
        min_value=60,
        max_value=99999,
        verbose_name="同步周期",
        help_text="单位: 分钟",
    )

    class Meta:
        verbose_name = "HTTP配置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.h_ip


class NetworkConfig(BaseModel):
    """网络配置"""

    n_name = fields.CharField(max_length=16, blank=False, verbose_name="网口名称")
    n_ip = fields.CharField(
        max_length=16,
        blank=False,
        verbose_name="IP地址",
        validators=[validators.validate_ipv4_address],
    )
    n_mask = fields.CharField(max_length=16, blank=False, verbose_name="子网掩码")
    n_broadcast = fields.CharField(max_length=16, blank=False, verbose_name="广播地址")
    n_gateway = fields.CharField(
        max_length=16,
        blank=False,
        verbose_name="默认网关",
        validators=[validators.validate_ipv4_address],
    )
    n_dns = fields.CharField(max_length=16, blank=False, verbose_name="DNS配置")

    class Meta:
        verbose_name = "网络配置"
        verbose_name_plural = verbose_name


class SystemInfo(BaseModel):
    """设备信息"""

    d_type = fields.CharField(max_length=32, blank=True, verbose_name="设备型号")
    d_id = fields.CharField(max_length=32, blank=True, verbose_name="设备ID")
    d_mac = fields.CharField(max_length=32, blank=True, verbose_name="Mac地址")
    d_firmware_version = fields.CharField(max_length=8, blank=True, verbose_name="固件版本")
    d_machine_version = fields.CharField(max_length=9, blank=True, verbose_name="一体机版本")
    d_algorithm_version = fields.CharField(
        max_length=8, blank=True, verbose_name="算法软件版本"
    )
    d_ffmpeg_version = fields.CharField(max_length=8, blank=True, verbose_name="拉流软件版本")
    d_config = fields.RadioField(
        choices=constant.S_CONFIG, default=0, verbose_name="抓拍图片上传配置"
    )

    class Meta:
        verbose_name = "设备信息"
        verbose_name_plural = verbose_name
