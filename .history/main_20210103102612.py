from youtube_statistics import YTstats
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Accessing variables.
ytuser = os.getenv('YTUSERID')
api_key = os.getenv('APIKEY')
# Amazing Discoveries South Africa
channel_id= "UC1oOoBASMrTyUBSltYcx0jA"


yt = YTstats(api_key, channel_id)
yt.get_channel_statistics()
