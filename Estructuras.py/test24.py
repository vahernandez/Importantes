import requests
import json
from pprint import pprint



payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '52b19659b5f9972c710e319137072ab88a33da0a'
}

"""
sw= int(input("De que switch quieres saber? : \n"))

switches= [
    {1: ["Switch_1",	"Q2KW-M4XJ-UXPJ"]},
    {2: ["Switch_4",	"Q2KW-Q9SK-N6L9"]}
    
]

for i in switches:
    for j in i:
        if sw==j:
            SW=i[j][1]
   

def Puerto(SW):
    for puerto in range(1, 60):
        url = f"https://api.meraki.com/api/v1/devices/{SW}/switch/ports/{puerto}"

        llamadaApi = requests.get(url, headers=headers, data=payload)
        #convertir a json
        if llamadaApi.status_code==200:
            datos=llamadaApi.json()
            print("Puertos: ", datos['portId'], " Modo: ", datos['type'], " Vlan", datos['vlan'])
        else:
            break
    return llamadaApi
Puerto(SW)
[

sw = int(input( "De que switch quieres obtener información?: \n"))

switches = [
    {1: {"Switch_1", "Q2KW-M4XJ-UXPJ"}},
    {2: {"Switch_4", "Q2KW-Q9SK-N6L9"}}
]

for i in switches:
    for j in i:
        print(i[j])

"""

switches= [
    {1: ["Switch_1", "Q2KW-M4XJ-UXPJ"]},
    {2: ["Switch_4", "Q2KW-Q9SK-N6L9"]}
    
]

sw = int(input("De que switch necesitas información? \n"))

for i in switches:
    for j in i:
        if sw == j:
            SW= i[j][1]

def Puerto(SW):
    for puerto in range(1, 60):
        url = f"https://api.meraki.com/api/v1/devices/{SW}/switch/ports/{puerto}"
        llamadaApi = requests.get(url, headers = headers, data = payload)
        if llamadaApi.status_code == 200:
            datos = llamadaApi.json()
            print('Puerto: ', datos['portId'], ' Vlan: ',datos['vlan'], ' Modo: ',datos['type'])
        else:
            break
    return llamadaApi
Puerto(SW)
