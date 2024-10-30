import requests
import json

url = "https://api.meraki.com/api/v1/networks/L_609674799555294825/wireless/ssids/5"

payload = json.dumps({
  "number": 5,
  "name": "sabinal",
  "enabled": True,
  "splashPage": "None",
  "ssidAdminAccessible": False,
  "authMode": "psk",
  "psk": "cisco123",
  "dot11w": {
    "enabled": False,
    "required": False
  },
  "dot11r": {
    "enabled": True,
    "adaptive": False
  },
  "encryptionMode": "wpa",
  "wpaEncryptionMode": "WPA1 and WPA2",
  "ipAssignmentMode": "Bridge mode",
  "useVlanTagging": True,
  "defaultVlanId": 21,
  "minBitrate": 11,
  "bandSelection": "Dual band operation",
  "perClientBandwidthLimitUp": 0,
  "perClientBandwidthLimitDown": 0,
  "perSsidBandwidthLimitUp": 0,
  "perSsidBandwidthLimitDown": 0,
  "mandatoryDhcpEnabled": False,
  "lanIsolationEnabled": False,
  "visible": True,
  "availableOnAllAps": False,
  "availabilityTags": [
    "sab"
  ],
  "speedBurst": {
    "enabled": False
  }
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
