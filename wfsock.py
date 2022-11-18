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

    # Loop to limit how many times it runs for testing
    x=0
    while (x < 3):
        # Receive data from socket and store in result as dictionary
        result = ws.recv()
        result = json.loads(result)

        # Check obs type and get the corresponding data
        obs_type = result['type']
        # Precipitation Event
        if obs_type == 'evt_precip':
            # Print time and rain message
            raintime = datetime.now()
            raintime = raintime.strftime("%H:%M:%S")
            print("Type: " + obs_type + " Time: " + raintime + " Precipitation event detected")
        # Lightning Strike
        if obs_type == 'evt_strike':
            # Print time and lightning message
            lightningtime = datetime.now()
            lightningtime = lightningtime.strftime("%H:%M:%S")
            print("Type: " + obs_type + " Time: " + lightningtime + " Lightning strike detected")
        # Tempest Data
        if obs_type == 'obs_st':
            # Get the data we want to see from the dictionary
            timestamp = datetime.utcfromtimestamp(result['obs'][0][0]).strftime('%Y-%m-%d %H:%M:%S')
            localtime = datetime.fromtimestamp(result['obs'][0][0]).strftime('%Y-%m-%d %H:%M:%S')
            temp = result['obs'][0][7]

            # Print the results to the console as a single string
            print("New Observation:")
            print("Type: " + obs_type + " Time: " + localtime + " Temp: " + str(temp))

            # Create string and write it to a .txt file
            string = "Type: " + obs_type + " Time: " + timestamp + " Temp: " + str(temp)
            with open("tempest.txt", "a") as data_file:
                data_file.write(string + '\n')

        x=x+1
    # Stop listening and close the socket connection
    ws.send('{"type":"listen_stop","device_id":' + tempest_ID + ',"id":"2098388936"}')
    ws.close()
