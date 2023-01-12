import pika
import time
import os

# read rabbitmq connection url from environment variable
amqp_url = os.environ['AMQP_URL_FROM_BOT']
url_params = pika.URLParameters(amqp_url)

# connect to rabbitmq
connection = pika.BlockingConnection(url_params)
chan = connection.channel()


# declare a new queue
# durable flag is set so that messages are retained
# in the rabbitmq volume even between restarts
chan.queue_declare(queue='frombot', durable=True)


def receive_msg(ch, method, properties, body):
    body.decode('utf-8')
    ch.basic_ack(delivery_tag=method.delivery_tag)


# to make sure the consumer receives only one message at a time
# next message is received only after acking the previous one
chan.basic_qos(prefetch_count=1)

# define the queue consumption
chan.basic_consume(queue='frombot',
                   on_message_callback=receive_msg)

# start consuming
chan.start_consuming()