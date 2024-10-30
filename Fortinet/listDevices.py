import requests
import json

# Primera llamada para obtener el token de sesión
url_login = "https://192.168.0.163/jsonrpc"
payload_login = json.dumps({
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
headers_login = {
  'Content-Type': 'application/json'
}

response_login = requests.request("POST", url_login, headers=headers_login, data=payload_login, verify=False)
token = response_login.json()['session']

# Segunda llamada usando el token de sesión
url_data = "https://192.168.0.163/jsonrpc"
payload_data = json.dumps({
  "method": "get",
  "params": [
    {
      "url": "/dvmdb/device"
    }
  ],
  "session": token,  # Usando el token de sesión obtenido en la primera llamada
  "verbose": 1,
  "id": 1
})
headers_data = {
  'Content-Type': 'application/json'
}

response_data = requests.request("POST", url_data, headers=headers_data, data=payload_data)

print(response_data.text)