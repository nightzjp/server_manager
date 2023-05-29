from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import GenericViewSet


class CustomGenericViewSet(GenericViewSet):
    """自定义GenericViewSet"""

    lookup_field = "uid"

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj
