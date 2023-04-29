import ipaddress

from django.db.models.fields.files import FileField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_ipv4_address(value):
    """
    校验IP地址
    """
    try:
        ipaddress.IPv4Address(value)
    except ValueError:
        raise ValidationError(
            _("Enter a valid IPv4 address."), code="invalid", params={"value": value}
        )
    else:
        # Leading zeros are forbidden to avoid ambiguity with the octal
        # notation. This restriction is included in Python 3.9.5+.
        if any(octet != "0" and octet[0] == "0" for octet in value.split(".")):
            raise ValidationError(
                _("Enter a valid IPv4 address."),
                code="invalid",
                params={"value": value},
            )


def validate_file_suffix(value: FileField):
    """校验文件后缀"""
    if value.name.rsplit(".")[-1] != "zip":
        raise ValidationError("必须上传zip格式压缩包")
