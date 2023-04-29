from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Get the value from the message queue and write to queue"

    def handle(self, *args, **options):
        """启动命令运行这个方法"""
        if not User.objects.exists():
            print("初始化用户")
            User.objects.create_superuser(
                username="admin", password="admin!@345", email="admin@localhost.com"
            )
        else:
            print("已存在初始用户，无需初始化")
