import requests
import json

url = "https://192.168.0.163/jsonrpc"

payload = json.dumps({
  "id": 1,
  "method": "exec",
  "params": [
    {
      "data": {
        "user": "admin",
        "passwd": "forti123"
      },
      "url": "/sys/login/user"
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

# Convertir la respuesta a JSON con formato vertical
json_response = response.json()
vertical_response = json.dumps(json_response, indent=4)

# Imprimir la respuesta en formato JSON vertical
print(vertical_response)