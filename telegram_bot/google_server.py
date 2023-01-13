import googlecongif
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from googleapiclient.discovery import build
import io

credentials = service_account.Credentials.from_service_account_file(
    googlecongif.SERVICE_ACCOUNT_FILE, scopes=googlecongif.SCOPES)
service = build('drive', 'v3', credentials=credentials)
folder_id = '1IrR3LbT-5FCHkIK7qG9NlrrSOZULozT-'


def download_file(filename, file_id):
    request = service.files().get_media(fileId=file_id)
    filename = '../test_audio/' + str(filename)
    fh = io.FileIO(filename, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        # print("Download %d%%." % int(status.progress() * 100))
    service.files().delete(fileId=file_id).execute()


def search_file(chat_id):
    files = service.files().list(pageSize=100, fields="nextPageToken, files(id, name, mimeType)",
                                 q=f"name contains '${chat_id}'").execute()
    # print(service.files().list(pageSize=100, fields="nextPageToken, files(id, name, mimeType)",
    #                            q="name contains" + str(chat_id) + ".wav").execute())
    print(files)
    if files == {'files': []}:
        nextPageToken = files.get('nextPageToken')
        print("uaosup")
        while files == {'files': []}:
            # files = service.files().list(pageSize=100,
            #                              fields="nextPageToken, files(id, name, mimeType, parents)",
            #                              pageToken=nextPageToken,
            #                              q=f"name contains '${chat_id}'").execute()
            # nextPageToken = files.get('nextPageToken')
            files = service.files().list(pageSize=100, fields="nextPageToken, files(id, name, mimeType)",
                                         q=f"name contains '${chat_id}'").execute()
            print(files)
        download_file(f"'${chat_id}'.wav", files['files'][0]['id'])
    else:
        download_file(f"'${chat_id}'.wav", files['files'][0]['id'])
