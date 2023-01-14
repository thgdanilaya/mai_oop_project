import os, sys, pika
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from parse.parse_generate import parse_args
from models import Models_functions
from utils import Utils_functions
import googleconfig
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from googleapiclient.discovery import build

from google_server import uploadgoogle
args = parse_args()
M = Models_functions(args)
M.download_networks()
models_ls = M.get_networks()
U = Utils_functions(args)


def callback(ch, method, properties, body):
    chatid = body.decode("utf-8")
    U.generate(models_ls,chatid)
    uploadgoogle(chatid)
    os.remove("/src/app/generations/snd" + chatid + ".wav")

amqp_url = os.environ['AMQP_URL_FROM_BOT']
url_params = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(url_params)
channel = connection.channel()
channel.queue_declare(queue='frombot')
channel.basic_consume(queue='frombot', auto_ack=True, on_message_callback=callback)
channel.start_consuming()
    
