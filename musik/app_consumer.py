import os, sys, pika
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from parse.parse_generate import parse_args
from models import Models_functions
from utils import Utils_functions
import googleconfig
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from googleapiclient.discovery import build

args = parse_args()
M = Models_functions(args)
M.download_networks()
models_ls = M.get_networks()
U = Utils_functions(args)
folder_id = '1IrR3LbT-5FCHkIK7qG9NlrrSOZULozT-'
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

def callback(ch, method, properties, body):
    chatid = body
    U.generate(models_ls,chatid)
    file_path = "./generations/" + str(chatid) + ".wav"
    name = str(chatid) + ".wav"
    file_metadata = {
                    'name': name,
                    'parents': [folder_id]
                }
    media = MediaFileUpload(file_path, resumable=True)
    service.files().create(body=file_metadata, media_body=media, fields='id').execute()

amqp_url = os.environ['AMQP_URL_FROM_BOT']
url_params = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(url_params)
channel = connection.channel()
channel.basic_consume(queue='frombot', auto_ack=True, on_message_callback=callback)
channel.start_consuming()
    
