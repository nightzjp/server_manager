import uuid
from datetime import datetime

from django.db import models
from simplepro.components import fields


class BaseQuerySet(models.QuerySet):
    def set_delete(self):
        return super(BaseQuerySet, self).update(delete_at=datetime.now())


class BaseManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop("alive_only", True)
        super(BaseManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        """软删除"""
        if self.alive_only:
            # 为True，表示返回给admin的queryset为已过滤数据
            return BaseQuerySet(self.model).filter(delete_at__isnull=True)
        return BaseQuerySet(self.model)


class BaseModel(models.Model):
    """
    自定义Model基类
    """

    id = models.BigAutoField(primary_key=True)
    uid = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, verbose_name="UUID"
    )
    create_at = fields.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="创建时间"
    )
    update_at = fields.DateTimeField(auto_now=True, verbose_name="更新时间")
    delete_at = fields.DateTimeField(null=True, blank=True, verbose_name="删除时间")
    create_by = fields.CharField(
        null=True, blank=True, max_length=32, verbose_name="创建人"
    )

    detail = fields.CharField(
        null=True,
        blank=True,
        max_length=200,
        show_word_limit=True,
        prefix_icon="el-icon-edit",
        verbose_name="备注信息",
        placeholder="请输入备注信息(可为空)",
    )

    objects = BaseManager()  # 默认查看已存在数据
    all_objects = BaseManager(alive_only=False)  # 返回已存在数据(包括已删除)

    class Meta:
        abstract = True
        ordering = ["-create_at"]

    def set_delete(self):
        """软删除"""
        self.delete_at = datetime.now()
        self.save()
