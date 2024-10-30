"""import requests
import json

url = "https://api.meraki.com/api/v1/devices/Q2LW-45P5-F593/switch/routing/interfaces/3677189095748011147/dhcp"

payload = "{\n    \"dhcpMode\": \"dhcpServer\",\n    \"dhcpLeaseTime\": \"1 day\",\n    \"dnsNameserversOption\": \"custom\",\n    \"dnsCustomNameservers\": [\n        \"10.0.5.6\",\n        \"10.0.5.7\",\n        \"10.0.8.4\"\n    ],\n    \"bootOptionsEnabled\": \"false\",\n    \"dhcpOptions\": [\n        {\n            \"code\": \"42\",\n            \"type\": \"ip\",\n            \"value\": \"10.0.5.2\"\n        },\n        {\n            \"code\": \"15\",\n            \"type\": \"text\",\n            \"value\": \"nps.intranet\"\n        }\n        {\n            \"code\": \"4\",\n            \"type\": \"text\",\n            \"value\": \"10.0.5.6\"\n        }\n    ],\n    \"reservedIpRanges\": [\n        {\n            \"start\": \"10.65.21.2\",\n            \"end\": \"10.65.21.50\",\n            \"comment\": \"exclude\"\n        },\n        {\n            \"start\": \"10.65.21.51\",\n            \"end\": \"10.65.21.100\",\n            \"comment\": \"exclude2\"\n        }\n    ],\n    \"fixedIpAssignments\": [\n        {\n            \"name\": \"lapTest\",\n            \"mac\": \"bc:e9:2f:e7:79:c2\",\n            \"ip\": \"10.65.21.101\"\n        }\n    ]\n}"
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
"""


import requests
import json

url = "https://api.meraki.com/api/v1/devices/Q2LW-45P5-F593/switch/routing/interfaces/3677189095748011147/dhcp"

payload = {
    "reservedIpRanges": [
        {
            "start": "10.65.21.2",
            "end": "10.65.21.50",
            "comment": "exclude"
        },
        {
            "start": "10.65.21.51",
            "end": "10.65.21.100",
            "comment": "exclude2"
        }
    ],
    "fixedIpAssignments": [
        {
            "name": "lapTest",
            "mac": "bc:e9:2f:e7:79:c2",
            "ip": "10.65.21.101"
        }
    ]
}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=json.dumps(payload))

print(response.text)
