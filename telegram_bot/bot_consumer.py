import pika
import os


def callback(ch, method, properties, body):
    return body


amqp_url = os.environ['AMQP_URL_TO_BOT']
url_params = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(url_params)
channel = connection.channel()
channel.basic_consume(queue='tobot', auto_ack=True, on_message_callback=callback)

channel.start_consuming()