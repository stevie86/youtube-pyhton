import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Accessing variables.
#status = os.getenv('STATUS')
api_key = os.getenv('APIKEY')

# Using variables.
print(status)
print(api_key)

