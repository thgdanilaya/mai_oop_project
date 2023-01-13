import pika
import os

def sender(path):
    amqp_url = os.environ['AMQP_URL_TO_BOT']
    url_params = pika.URLParameters(amqp_url)
    connection = pika.BlockingConnection(url_params)
    channel = connection.channel()
    channel.queue_declare(queue='tobot')
    channel.basic_publish(exchange='', routing_key='tobot', body=path)
    connection.close()