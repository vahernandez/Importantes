import requests
import json

url = "https://api.meraki.com/api/v1/devices/Q2LW-89GD-FL29/switch/routing/interfaces"

payload = json.dumps({
  "name": "NPSRadiusDummie",
  "subnet": "192.168.24.0/24",
  "interfaceIp": "192.168.24.2",
  "multicastRouting": "disabled",
  "vlanId": "24",
  "ospfSettings": {
    "area": "ospfDisabled"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

