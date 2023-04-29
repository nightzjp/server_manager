from django.core.management.base import BaseCommand

from system.models import NetworkConfig
from utils.network import network


class Command(BaseCommand):
    help = "Get the value from the message queue and write to queue"

    def handle(self, *args, **options):
        """启动命令运行这个方法"""
        _network_list = network.get_network_config(physical=True)
        print(f"获取到{len(_network_list)}张网卡信息")
        if not NetworkConfig.objects.exists():
            print("网络初始化.")
            for _ in _network_list:
                NetworkConfig.objects.create(
                    n_name=_.get("iface"),
                    n_ip=_.get("ip"),
                    n_mask=_.get("netmask"),
                    n_broadcast=_.get("broadcast"),
                    n_gateway=_.get("gateway"),
                    n_dns=_.get("dns"),
                )
            print("初始化完成!")
        else:
            print("数据库已存在网卡配置，无需重新获取.")
