import requests
import json

url = "https://api.meraki.com/api/v1/networks/L_609674799555294825/groupPolicies"

payload = json.dumps({
  "groupPolicyId": "107",
  "name": "Warehouse3",
  "scheduling": {
    "enabled": False,
    "monday": {
      "active": True,
      "from": "00:00",
      "to": "24:00"
    },
    "tuesday": {
      "active": True,
      "from": "00:00",
      "to": "24:00"
    },
    "wednesday": {
      "active": True,
      "from": "00:00",
      "to": "24:00"
    },
    "thursday": {
      "active": True,
      "from": "00:00",
      "to": "24:00"
    },
    "friday": {
      "active": True,
      "from": "00:00",
      "to": "24:00"
    },
    "saturday": {
      "active": True,
      "from": "00:00",
      "to": "24:00"
    },
    "sunday": {
      "active": True,
      "from": "00:00",
      "to": "24:00"
    }
  },
  "bandwidth": {
    "settings": "custom",
    "bandwidthLimits": {
      "limitUp": 51200,
      "limitDown": 51200
    }
  },
  "firewallAndTrafficShaping": {
    "settings": "custom",
    "trafficShapingRules": [],
    "l3FirewallRules": [],
    "l7FirewallRules": [
      {
        "policy": "deny",
        "type": "applicationCategory",
        "value": {
          "id": "meraki:layer7/category/27",
          "name": "Advertising"
        }
      },
      {
        "policy": "deny",
        "type": "applicationCategory",
        "value": {
          "id": "meraki:layer7/category/13",
          "name": "Video & music"
        }
      },
      {
        "policy": "deny",
        "type": "application",
        "value": {
          "id": "meraki:layer7/application/4",
          "name": "Gmail"
        }
      },
      {
        "policy": "deny",
        "type": "application",
        "value": {
          "id": "meraki:layer7/application/39",
          "name": "Hotmail"
        }
      },
      {
        "policy": "deny",
        "type": "application",
        "value": {
          "id": "meraki:layer7/application/130",
          "name": "Yahoo Mail"
        }
      },
      {
        "policy": "deny",
        "type": "application",
        "value": {
          "id": "meraki:layer7/application/106",
          "name": "Apple file sharing"
        }
      },
      {
        "policy": "deny",
        "type": "application",
        "value": {
          "id": "meraki:layer7/application/9",
          "name": "Dropbox"
        }
      },
      {
        "policy": "deny",
        "type": "application",
        "value": {
          "id": "meraki:layer7/application/185",
          "name": "Mega"
        }
      },
      {
        "policy": "deny",
        "type": "application",
        "value": {
          "id": "meraki:layer7/application/168",
          "name": "PutLocker.com"
        }
      },
      {
        "policy": "deny",
        "type": "applicationCategory",
        "value": {
          "id": "meraki:layer7/category/6",
          "name": "Gaming"
        }
      },
      {
        "policy": "deny",
        "type": "applicationCategory",
        "value": {
          "id": "meraki:layer7/category/7",
          "name": "Online backup"
        }
      },
      {
        "policy": "deny",
        "type": "applicationCategory",
        "value": {
          "id": "meraki:layer7/category/8",
          "name": "Peer-to-peer (P2P)"
        }
      },
      {
        "policy": "deny",
        "type": "applicationCategory",
        "value": {
          "id": "meraki:layer7/category/9",
          "name": "Social web & photo sharing"
        }
      },
      {
        "policy": "deny",
        "type": "applicationCategory",
        "value": {
          "id": "meraki:layer7/category/17",
          "name": "Web file sharing"
        }
      },
      {
        "policy": "deny",
        "type": "applicationCategory",
        "value": {
          "id": "meraki:layer7/category/2",
          "name": "Blogging"
        }
      }
    ]
  },
  "splashAuthSettings": "network default",
  "vlanTagging": {
    "settings": "network default"
  },
  "bonjourForwarding": {
    "settings": "network default",
    "rules": []
  }
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
