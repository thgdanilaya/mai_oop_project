import pika
import os

amqp_url = os.environ['AMQP_URL_FROM_BOT']
url_params = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(url_params)
channel = connection.channel()

channel.queue_declare(queue='tobot')

channel.basic_publish(exchange='', routing_key='tobot', body='Audio here')
connection.close()