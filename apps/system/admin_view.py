from django.shortcuts import render
from django.views import View


class CustomUploadView(View):
    """自定义上传"""

    def get(self, request, *args, **kwargs):
        return render(request, "admin/custom_upload.html", locals())
