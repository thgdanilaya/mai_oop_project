import pika
import os

# # read rabbitmq connection url from environment variable
# amqp_url = os.environ['AMQP_URL']
# url_params = pika.URLParameters(amqp_url)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue="Hello")

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body="Hello world")
print("Sent msg")
connection.close()