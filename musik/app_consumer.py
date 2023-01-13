import os, sys, pika
from app_producer import sender
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from parse.parse_generate import parse_args
from models import Models_functions
from utils import Utils_functions

args = parse_args()
M = Models_functions(args)
M.download_networks()
models_ls = M.get_networks()
U = Utils_functions(args)

def callback(ch, method, properties, body):
    chatid = body
    U.generate(models_ls,chatid)
    path = "./generations/" + str(chatid) + ".wav"
    sender(path)

amqp_url = os.environ['AMQP_URL_FROM_BOT']
url_params = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(url_params)
channel = connection.channel()
channel.basic_consume(queue='frombot', auto_ack=True, on_message_callback=callback)
channel.start_consuming()
    
