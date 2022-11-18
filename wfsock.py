import websocket
import json

token = "e5d5edf0-8840-4cd4-9858-53d141db817c"
tempest_ID = '136821'

ws = websocket.WebSocket()
ws.connect("wss://ws.weatherflow.com/swd/data?token=" + token)
result = ws.recv()

print("Connecting to WF Tempest...")
ws.send('{"type":"listen_start","device_id":' + tempest_ID + ',"id":"2098388936"}')
result = ws.recv()
result = json.loads(result)
print(result)
while (ws.connected):
    x=0
    while (x < 3):
        result = ws.recv()
        result = json.loads(result)

        print(result['type'])
        print(result['obs'][0][0])
        
        x=x+1
    ws.send('{"type":"listen_stop","device_id":' + tempest_ID + ',"id":"2098388936"}')
    ws.close()


