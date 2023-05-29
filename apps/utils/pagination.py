from collections import OrderedDict

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomLimitOffsetPagination(LimitOffsetPagination):
    """自定义分页器：优化大数据查询缓慢"""

    def get_count(self, queryset):
        try:
            return queryset.first().id - queryset.last().id + 1
        except (AttributeError, TypeError):
            return len(queryset)

    def get_paginated_response(self, data):
        return Response(OrderedDict([('count', self.count), ('results', data)]))
