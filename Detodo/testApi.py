############# The Call ##################################

url = "https://api.meraki.com/api/v1/networks/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"



############# the response ##############################

{
    "message": null,
    "pageStartAt": "2023-03-18T23:26:59.000000Z",
    "pageEndAt": "2023-04-18T23:26:59.359179Z",
    "events": [
        {
            "occurredAt": "2023-04-18T11:28:10.308985Z",
            "networkId": "L_754915887537980170",
            "type": "loop_detected",                       <<<< I need this 
            "description": "Loop detected",
            "clientId": null,
            "clientDescription": null,
            "clientMac": "",
            "category": "switch_port",
            "deviceSerial": "Q2KW-YQGN-QZB2",
            "deviceName": "West IDF",                      <<<<< I need this
            "eventData": {                                 
                "port": "35"                               <<<<< I need this
            }
        },
    ]
}
 