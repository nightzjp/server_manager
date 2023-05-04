from django.core.management.base import BaseCommand

from apscheduler.schedulers.background import BlockingScheduler

from device.models import Device
from utils.cr import check_rtsp_stream


class Command(BaseCommand):
    help = "Get the value from the message queue and write to queue"

    def handle(self, *args, **options):
        """启动命令运行这个方法"""
        _scheduler = BlockingScheduler()
        try:
            _scheduler.add_job(
                func=self.get_time,
                trigger="interval",
                seconds=1800,  # 每隔1800s更新设备拉流状态
                jobstore='default',
                executor='default',
                replace_existing=True
            )
            _scheduler.start()
        except Exception as e:
            print(e)
            _scheduler.shutdown()


    @staticmethod
    def update_device_status():
        """每隔五分钟更新设备状态"""
        device_list = Device.objects.all()
        for device in device_list:
            device.d_status = check_rtsp_stream(device.d_rtsp)
