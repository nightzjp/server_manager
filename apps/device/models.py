from django.db import models
from simplepro.components import fields

from public.models import BaseModel
from utils import constant, validators


class Algorithm(BaseModel):
    """算法模型管理类"""

    ai_name = fields.CharField(
        max_length=8,
        blank=False,
        verbose_name="模型名称",
        placeholder="请输入模型名称",
        show_word_limit=True,
        prefix_icon="el-icon-edit",
    )
    ai_status = fields.SwitchField(default=False, verbose_name="是否启用")
    ai_is_used = fields.RadioField(
        choices=constant.AI_IS_USED, default=1, verbose_name="使用状态"
    )
    ai_source = fields.RadioField(
        choices=constant.AI_SOURCE, default=0, verbose_name="模型来源"
    )
    ai_describe = fields.CharField(
        max_length=64,
        blank=True,
        verbose_name="模型描述",
        placeholder="请输入模型描述信息",
        show_word_limit=True,
        prefix_icon="el-icon-edit",
    )
    ai_file = models.FileField(
        upload_to="ai",
        blank=False,
        verbose_name="模型文件",
        validators=[validators.validate_file_suffix],
        help_text="仅支持zip文件上传",
    )

    class Meta:
        verbose_name = "算法模型管理类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.ai_name}-{'已启用' if self.ai_status else '未启用'}"


class Device(BaseModel):
    """设备视频源"""

    d_name = fields.CharField(
        max_length=16,
        blank=False,
        verbose_name="设备名称",
        placeholder="请输入设备名称",
        show_word_limit=True,
        prefix_icon="el-icon-edit",
    )
    d_ip = fields.CharField(
        max_length=16,
        blank=False,
        verbose_name="IP地址",
        placeholder="请输入正确的IP地址",
        show_word_limit=True,
        prefix_icon="el-icon-edit",
        validators=[validators.validate_ipv4_address],
    )
    d_address = fields.AMapField(
        max_length=128, null=True, blank=True, pick_type="address", verbose_name="设备地址"
    )
    d_geo = fields.AMapField(max_length=64, null=True, blank=True, verbose_name="经纬度")
    d_source = fields.RadioField(
        choices=constant.D_SOURCE, default=0, verbose_name="设备来源"
    )
    d_type = fields.RadioField(choices=constant.D_TYPE, default=0, verbose_name="设备类型")
    d_brand = fields.RadioField(
        choices=constant.D_BRAND, default=0, verbose_name="设备品牌"
    )
    d_status = fields.RadioField(
        choices=constant.D_STATUS, default=0, verbose_name="设备状态"
    )
    d_format = fields.RadioField(
        choices=constant.D_FORMAT, default=0, verbose_name="流类型"
    )
    d_username = fields.CharField(
        max_length=8,
        blank=False,
        verbose_name="设备用户名",
        placeholder="请输入设备用户名",
        show_word_limit=True,
        prefix_icon="el-icon-user",
    )
    d_password = fields.CharField(
        max_length=16,
        blank=False,
        verbose_name="设备密码",
        placeholder="请输入设备密码",
        show_word_limit=True,
        show_password=True,
        prefix_icon="el-icon-lock",
    )
    d_rtsp = fields.CharField(
        max_length=64,
        blank=True,
        verbose_name="rtsp地址",
        placeholder="当设备类型为自定义填写",
        show_word_limit=True,
        prefix_icon="el-icon-camera",
    )
    d_channel = fields.InputNumberField(
        default=0, min_value=0, max_value=10, verbose_name="通道号"
    )
    d_last_login = fields.DateTimeField(blank=True, null=True, verbose_name="最后一次连接时间")
    d_last_logout = fields.DateTimeField(blank=True, null=True, verbose_name="最后一次下线时间")
    d_algorithm = fields.TransferField(
        to="Algorithm",
        blank=True,
        verbose_name="关联算法模型",
        help_text="请选择算法模型",
        filterable=True,
        placeholder="请输入关键字搜索",
        titles=["待选", "已选"],
        button_texts=["往左", "往右"],
    )

    class Meta:
        verbose_name = "设备视频源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.d_name}-{self.d_ip}"
