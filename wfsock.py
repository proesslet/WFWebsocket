import websocket
import json
from datetime import datetime

# Create variables to store token and device ID
token = "e5d5edf0-8840-4cd4-9858-53d141db817c"
tempest_ID = '136821'

# Create web socket object and connect to WF api using token
ws = websocket.WebSocket()
ws.connect("wss://ws.weatherflow.com/swd/data?token=" + token)
result = ws.recv()

# Send request to start listening for data from device
print("Connecting to WF Tempest...")
ws.send('{"type":"listen_start","device_id":' + tempest_ID + ',"id":"2098388936"}')
# Receive initial response which should be 'ack'
result = ws.recv()
result = json.loads(result)
print(result)

# Create loop to continuously listen for data while the socket connection is open
while (ws.connected):
    x=0
    while (x < 5):
        result = ws.recv()
        result = json.loads(result)

        obs_type = result['type']
        timestamp = datetime.utcfromtimestamp(result['obs'][0][0]).strftime('%Y-%m-%d %H:%M:%S')
        temp = result['obs'][0][7]
        print("New Observation:")
        print("Type: " + obs_type + " Time: " + timestamp + " Temp: " + str(temp))

        string = "Type: " + obs_type + " Time: " + timestamp + " Temp: " + str(temp)
        with open("tempest.txt", "a") as data_file:
            data_file.write(string + '\n')
        
        x=x+1
    ws.send('{"type":"listen_stop","device_id":' + tempest_ID + ',"id":"2098388936"}')
    ws.close()


