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
        self.push_key = "_device_push"

    @property
    def event_method(self):
        return {
            "camera_add": self.camera_add,  # 接收摄像头添加功能
            "camera_del": self.camera_del,  # 接受摄像头删除功能
            "update_response": self.update_response,  # 接收升级反馈
        }

    def camera_add(self):
        """摄像头添加"""
        pass

    def camera_del(self):
        """摄像头删除"""
        pass

    def update_response(self):
        """接收升级反馈"""
        pass

    @staticmethod
    def generate_body(topic, data):
        """生成通用消息体"""
        return json.dumps({"topic": topic, "data": data})

    def connect(self):
        credit = pika.PlainCredentials(username=self.username, password=self.password)
        self.channel = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.host, port=self.port, credentials=credit
            )
        ).channel()

    def push_enqueue(self, topic, data):
        """
        推送数据
        {
            "topic": "topic",
            "data": "data",
        }
        """
        self.connect()
        channel = self.channel
        channel.queue_declare(queue=self.push_key, durable=True)  # 队列持久化
        channel.basic_publish(
            exchange="",
            routing_key=self.push_key,
            body=self.generate_body(topic, data),
            properties=pika.BasicProperties(
                delivery_mode=2,  # 消息持久化
            ),
        )
        channel.close()

    def pop_queue(self, queue_name, timeout=0):
        """
        获取数据
        {
            "topic": "topic",
            "data": "data",
        }
        """
        self.connect()
        channel = self.channel

        channel.queue_declare(queue=queue_name, durable=True)
        channel.basic_consume(
            on_message_callback=self.callback, queue=queue_name, auto_ack=True
        )

        channel.start_consuming()

    def callback(self, channel, method, properties, body):
        """数据回调"""
        receive = json.loads(body.decode())
        print(receive)
        method_name = self.event_method.get(receive.get("topic"))
        if not callable(method_name):
            print("未知主题，不可调用")
        else:
            method_name(receive.get("data"))
