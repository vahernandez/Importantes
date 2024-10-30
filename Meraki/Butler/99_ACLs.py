import requests
import json
from pprint import pprint 

url = "https://api.meraki.com/api/v1/networks/L_754915887537980570/switch/accessControlLists"

payload = json.dumps({
  "rules": [
    {
      "policy": "deny",
      "protocol": "Any",
      "srcCidr": "10.21.9.128/25",
      "dstCidr": "10.21.1.0/24",
      "comment": "D Guest v91 to Radius v1",
      "ipVersion": "IPv4",
      "srcPort": "any",
      "dstPort": "any",
      "vlan": "1"
    },
    {
      "policy": "deny",
      "protocol": "Any",
      "srcCidr": "10.21.9.128/25",
      "dstCidr": "10.21.2.0/24",
      "comment": "D Guest v91 to Cabling v2",
      "ipVersion": "IPv4",
      "srcPort": "any",
      "dstPort": "any",
      "vlan": "2"
    },
        {
      "policy": "deny",
      "protocol": "Any",
      "srcCidr": "10.21.9.128/25",
      "dstCidr": "10.21.3.0/24",
      "comment": "D Guest v91 to Ware v3",
      "ipVersion": "IPv4",
      "srcPort": "any",
      "dstPort": "any",
      "vlan": "3"
    },
    {
      "policy": "deny",
      "protocol": "Any",
      "srcCidr": "10.21.9.128/25",
      "dstCidr": "10.21.4.0/24",
      "comment": "D Guest v91 to Iot v4",
      "ipVersion": "IPv4",
      "srcPort": "any",
      "dstPort": "any",
      "vlan": "4"
    },
    {
      "policy": "deny",
      "protocol": "Any",
      "srcCidr": "10.21.9.128/25",
      "dstCidr": "10.21.5.0/24",
      "comment": "D Guest v91 to Camaras v50",
      "ipVersion": "IPv4",
      "srcPort": "any",
      "dstPort": "any",
      "vlan": "50"
    },
    {
      "policy": "deny",
      "protocol": "Any",
      "srcCidr": "10.21.9.128/25",
      "dstCidr": "10.21.6.0/25",
      "comment": "D Guest v91 to Contrac v60",
      "ipVersion": "IPv4",
      "srcPort": "any",
      "dstPort": "any",
      "vlan": "60"
    },
    {
      "policy": "deny",
      "protocol": "Any",
      "srcCidr": "10.21.9.128/25",
      "dstCidr": "10.21.7.0/25",
      "comment": "D Guest v91 to Spare v70",
      "ipVersion": "IPv4",
      "srcPort": "any",
      "dstPort": "any",
      "vlan": "70"
    },
    {
      "policy": "deny",
      "protocol": "Any",
      "srcCidr": "10.21.9.128/25",
      "dstCidr": "10.21.7.128/25",
      "comment": "D Guest v91 to Unsed v71",
      "ipVersion": "IPv4",
      "srcPort": "any",
      "dstPort": "any",
      "vlan": "71"
    },
    {
      "policy": "deny",
      "protocol": "Any",
      "srcCidr": "10.21.9.128/25",
      "dstCidr": "10.21.0.0/24",
      "comment": "D Guest v91 to Print v100",
      "ipVersion": "IPv4",
      "srcPort": "any",
      "dstPort": "any",
      "vlan": "100"
    },
    {
      "policy": "deny",
      "protocol": "Any",
      "srcCidr": "10.21.9.128/25",
      "dstCidr": "10.21.50.0/25",
      "comment": "D Guest v91 to Mgmt v500",
      "ipVersion": "IPv4",
      "srcPort": "any",
      "dstPort": "any",
      "vlan": "500"
    },  
    {
      "policy": "deny",
      "protocol": "Any",
      "srcCidr": "10.21.9.128/25",
      "dstCidr": "10.0.0.0/8",
      "comment": "D Guest v91 to Intranet",
      "ipVersion": "IPv4",
      "srcPort": "any",
      "dstPort": "any",
      "vlan": "1000"
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("PUT", url, headers=headers, data=payload)

pprint(response.json())
