import requests
import json
from pprint import pprint

url = "https://api.meraki.com/api/v1/devices/Q2LW-89GD-FL29/switch/routing/interfaces"

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers)

pprint(response.json())