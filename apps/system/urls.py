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
from rest_framework.routers import DefaultRouter

from system import views

router = DefaultRouter()
router.register(r"mqtt_config", views.MqttConfigViewSet, basename="mqtt_config")
router.register(r"http_config", views.HttpConfigViewSet, basename="http_config")
router.register(r"network_config", views.NetWorkConfigViewSet, basename="network_config")
router.register(r"system_info", views.SystemInfoViewSet, basename="system_info")

urlpatterns = []

urlpatterns += router.urls
