import requests
from pprint import pprint

url = "https://api.meraki.com/api/v1/networks/L_754915887537980170/events?productType=switch&deviceName=West IDF&perPage=500"

payload={}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)


pprint(response.json())
