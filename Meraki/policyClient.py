import requests
import json

url = "https://api.meraki.com/api/v1/networks/L_609674799555294825/clients/k5a5627/policy"

payload = json.dumps({
  "devicePolicy": "Normal",
  "groupPolicyId": "null"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)