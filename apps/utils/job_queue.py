import json
import pika

from django.conf import settings


class RabbitQueue:
    def __init__(self, username=None, password=None, host=None, port=None):
        self.username = username or settings.RABBITMQ_USERNAME
        self.password = password or settings.RABBITMQ_PASSWORD
        self.host = host or settings.RABBITMQ_HOST
        self.port = port or settings.RABBITMQ_PORT
        self.channel = None

    def connect(self):
        credit = pika.PlainCredentials(username=self.username, password=self.password)
        self.channel = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.host, port=self.port, credentials=credit
            )
        ).channel()

    def push_enqueue(self, image_list):
        """推送数据"""
        self.connect()
        channel = self.channel
        key = "_device_push"
        channel.queue_declare(queue=key, durable=True)  # 队列持久化
        channel.basic_publish(
            exchange="",
            routing_key=key,
            body=json.dumps(image_list, ensure_ascii=False),
            properties=pika.BasicProperties(
                delivery_mode=2,  # 消息持久化
            ),
        )

        channel.close()

    def pop_queue(self, queue_name, timeout=0):
        """获取数据"""
        self.connect()
        channel = self.channel

        channel.queue_declare(queue=queue_name, durable=True)
        channel.basic_consume(
            on_message_callback=self.callback, queue=queue_name, auto_ack=True
        )

        channel.start_consuming()

    @staticmethod
    def callback(channel, method, properties, body):
        """数据回调"""
        receive = json.loads(body.decode())
        print(receive)
