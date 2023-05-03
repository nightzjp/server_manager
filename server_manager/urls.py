"""
URL configuration for server_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from system import admin_view


urls_v1 = [
    path("device/", include(("device.urls", "device"))),
    path("system/", include(("system.urls", "system"))),
]

custom_urls_v1 = [
    path("upload/", csrf_exempt(admin_view.CustomUploadView.as_view()), name="upload")
]


urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', admin.site.urls),
    path("sp/", include("simplepro.urls")),
    path("v1/", include(urls_v1)),
    path("custom/", include(custom_urls_v1))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "视图管理平台"
admin.site.site_title = "视图管理平台"
admin.site.empty_value_display = "-"
