import os
from dotenv import load_dotenv
from homeassistant_api import Client, State

load_dotenv()

url = os.getenv('URL')
token = os.getenv('TOKEN')

client = Client(url, token)
domains = client.get_domains()

light = domains.light
switch = domains.switch

print('Done loading')

light.turn_on(entity_id='light.living_room_lamp')
