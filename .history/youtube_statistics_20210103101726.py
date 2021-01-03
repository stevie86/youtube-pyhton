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

class YTstats:
    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None

        def get_channel_statistics(self):
            url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}'
            print(url)
