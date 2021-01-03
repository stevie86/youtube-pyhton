import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Accessing variables.
ytuser = os.getenv('YTUSERID')
api_key = os.getenv('APIKEY')

# Using variables.
#print(status)
print(api_key)

from googleapiclient.discovery import build

youtube = build('youtube', 'v3', developerKey=api_key)

request= youtube.channels().list(
    part='contentDetails',
    forUsername='SieleDiensAfrika')
response = request.execute()    
youtube.close()