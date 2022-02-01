import os
from dotenv import load_dotenv
from homeassistant_api import Client as CL

load_dotenv()

url = os.getenv('URL')
token = os.getenv('TOKEN')

client = CL(url, token)

domains = client.get_domains()

domains.light.turn_on(entity_id='light.rgbledstrip1')