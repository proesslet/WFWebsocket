import tkinter as tk
import websocket
import json
from datetime import datetime
from threading import *
from Settings import Settings

# Create variables to store token and device ID
token = "e5d5edf0-8840-4cd4-9858-53d141db817c"
tempest_ID = '136821'

# Create web socket object and connect to WF api using token
ws = websocket.WebSocket()
ws.connect("wss://ws.weatherflow.com/swd/data?token=" + token)
result = ws.recv()

# Default Settings
temp_unit = "F"
wind_unit = "mph"
pressure_unit = "inHg"
rain_unit = "in"

# Setup main window
window = tk.Tk()
window.title("Weatherflow Data Viewer")
window.minsize(500, 500)

# Configure the grid
window.columnconfigure(0, minsize=250, weight=1)
window.columnconfigure(1, minsize=250, weight=1)

# Create a title for the dataviewer
label = tk.Label(master=window, text="Preston's WX", font="Arial 24")
label.grid(row=0, column=0, columnspan=2)
# Last update time
last_update = tk.Label(master=window, text="Last Updated: 00:00:00", font="Arial 12")
last_update.grid(row=1, column=0, columnspan=2)

# Create a frame to hold the data
frame = tk.Frame(master=window, width=500, height=500)
frame.grid(row=2, column=0, columnspan=2)

# Temperature data
temp_frame = tk.Frame(master=frame, width=150, height=150)
temp_frame.grid(row=2, column=0, padx=10, pady=10)
temp_label = tk.Label(master=temp_frame, text="Temperature", font="Arial 16 underline")
temp_label.grid(row=0, column=0)
temp_data = tk.Label(master=temp_frame, text="0", font="Arial 20")
temp_data.grid(row=1, column=0)

# Wind Speed data
wind_frame = tk.Frame(master=frame, width=100, height=100)
wind_frame.grid(row=2, column=1, padx=10, pady=10)
wind_label = tk.Label(master=wind_frame, text="Wind Speed", font="Arial 16 underline")
wind_label.grid(row=0, column=0)
wind_data = tk.Label(master=wind_frame, text="0", font="Arial 20")
wind_data.grid(row=1, column=0)

# Pressure data
pressure_frame = tk.Frame(master=frame, width=100, height=100)
pressure_frame.grid(row=2, column=3, padx=10, pady=10)
pressure_label = tk.Label(master=pressure_frame, text="Pressure", font="Arial 16 underline")
pressure_label.grid(row=0, column=0)
pressure_data = tk.Label(master=pressure_frame, text="0", font="Arial 20")
pressure_data.grid(row=1, column=0)

# Humidity data
humidity_frame = tk.Frame(master=frame, width=100, height=100)
humidity_frame.grid(row=3, column=0, padx=10, pady=10)
humidity_label = tk.Label(master=humidity_frame, text="Humidity", font="Arial 16 underline")
humidity_label.grid(row=0, column=0)
humidity_data = tk.Label(master=humidity_frame, text="0", font="Arial 20")
humidity_data.grid(row=1, column=0)

# Rain data
rain_frame = tk.Frame(master=frame, width=100, height=100)
rain_frame.grid(row=3, column=1, padx=10, pady=10)
rain_label = tk.Label(master=rain_frame, text="Rain", font="Arial 16 underline")
rain_label.grid(row=0, column=0)
rain_data = tk.Label(master=rain_frame, text="0", font="Arial 20")
rain_data.grid(row=1, column=0)

#Solar Radiation data
solar_frame = tk.Frame(master=frame, width=100, height=100)
solar_frame.grid(row=3, column=3, padx=10, pady=10)
solar_label = tk.Label(master=solar_frame, text="Solar Radiation", font="Arial 16 underline")
solar_label.grid(row=0, column=0)
solar_data = tk.Label(master=solar_frame, text="0", font="Arial 20")
solar_data.grid(row=1, column=0)

# if window closed, close the websocket
def on_closing():
    ws.send('{"type":"listen_stop","device_id":' + tempest_ID + ',"id":"2098388936"}')
    ws.close()
    print("Websocket closed")
    window.destroy()
    return



def on_error(ws, message):
    print("Error: " + str(message))
    return
def on_message(ws, message):
    
    result = json.loads(message)
    obs_type = result['type']
    if obs_type == 'obs_st':
        timestamp = datetime.utcfromtimestamp(result['obs'][0][0]).strftime('%Y-%m-%d %H:%M:%S')
        localtime = datetime.fromtimestamp(result['obs'][0][0]).strftime('%Y-%m-%d %H:%M:%S')
        localtime_readable = datetime.fromtimestamp(result['obs'][0][0]).strftime('%b %-d %Y %-I:%M %p')
        # Get data from the message
        temp = result['obs'][0][7]
        windspeed = result['obs'][0][2]
        wind_direction = result['obs'][0][4]
        pressure = result['obs'][0][6]
        humidity = result['obs'][0][8]
        rain_accumulation = result['obs'][0][18]
        solar_radiation = result['obs'][0][11]


        # Data Conversions
        if temp_unit == "F":
            temp = round((temp * 9/5) + 32, 2)
        else:
            temp = round(temp, 2)
        windspeed = round(windspeed * 2.23694, 1)
        rain_accumulation = round(rain_accumulation * 0.0393701, 2)

        #wind direction calculation
        wind_compass = "N"
        if wind_direction >= 348.75 or wind_direction < 11.25:
            wind_compass = "N"
        elif wind_direction >= 11.25 and wind_direction < 33.75:
            wind_compass = "NNE"
        elif wind_direction >= 33.75 and wind_direction < 56.25:
            wind_compass = "NE"
        elif wind_direction >= 56.25 and wind_direction < 78.75:
            wind_compass = "ENE"
        elif wind_direction >= 78.75 and wind_direction < 101.25:
            wind_compass = "E"
        elif wind_direction >= 101.25 and wind_direction < 123.75:
            wind_compass = "ESE"
        elif wind_direction >= 123.75 and wind_direction < 146.25:
            wind_compass = "SE"
        elif wind_direction >= 146.25 and wind_direction < 168.75:
            wind_compass = "SSE"
        elif wind_direction >= 168.75 and wind_direction < 191.25:
            wind_compass = "S"
        elif wind_direction >= 191.25 and wind_direction < 213.75:
            wind_compass = "SSW"
        elif wind_direction >= 213.75 and wind_direction < 236.25:
            wind_compass = "SW"
        elif wind_direction >= 236.25 and wind_direction < 258.75:
            wind_compass = "WSW"
        elif wind_direction >= 258.75 and wind_direction < 281.25:
            wind_compass = "W"
        elif wind_direction >= 281.25 and wind_direction < 303.75:
            wind_compass = "WNW"
        elif wind_direction >= 303.75 and wind_direction < 326.25:
            wind_compass = "NW"
        elif wind_direction >= 326.25 and wind_direction < 348.75:
            wind_compass = "NNW"


        
        # Save temperature data to file
        with open('tempest_data.txt', 'a') as f:
            f.write(timestamp + "," + str(temp))

        # Print data to console
        #print("Temp: " + str(temp))
        #print("Wind Speed: " + str(windspeed))

        # Update data on GUI
        last_update.config(text="Last Updated: " + localtime_readable)
        temp_data.config(text=str(temp) + " " + temp_unit)
        wind_data.config(text=str(windspeed) + " " + wind_unit + " " + wind_compass)
        pressure_data.config(text=str(pressure))
        humidity_data.config(text=str(humidity) + "%")
        rain_data.config(text=str(rain_accumulation) + ' inches')
        solar_data.config(text=str(solar_radiation) + " W/m^2")

    return

def on_open(ws):
    ws.send('{"type":"listen_start","device_id":' + tempest_ID + ',"id":"2098388936"}')
def connection():
    ws = websocket.WebSocketApp("wss://ws.weatherflow.com/swd/data?token=" + token, on_message = on_message, on_error = on_error)
    ws.on_open = on_open
    ws.run_forever()
    return

t = Thread(target=connection)
t.start()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()


