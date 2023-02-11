import tkinter as tk

class Settings:

    # Settings options
    temp_unit_options = ["Fahrenheit", "Celsius"]
    wind_unit_options = ["MPH", "KPH"]
    pressure_unit_options = ["inHg", "hPa"]
    rain_unit_options = ["in", "mm"]
    
    

    # Constructor
    def __init__(self, temp_unit, wind_unit, pressure_unit, rain_unit):
        self.temp_unit = temp_unit
        self.wind_unit = wind_unit
        self.pressure_unit = pressure_unit
        self.rain_unit = rain_unit

        settings = tk.Toplevel()
        settings.title("Settings")
        settings.minsize(500, 500)
        settings_title = tk.Label(master=settings, text="Settings", font="Arial 24")
        settings_title.pack()

        # Create a frame to hold the settings options
        settings_frame = tk.Frame(master=settings, width=500, height=500)
        settings_frame.pack()

        # Temperature unit
        temp_label = tk.Label(master=settings_frame, text="Temperature Unit:")
        temp_label.pack()
        temp_selected = tk.StringVar()
        temp_selected.set(self.temp_unit)
        temp_unit_selector = tk.OptionMenu(settings_frame, temp_selected, *self.temp_unit_options)
        temp_unit_selector.pack()
        
        # Wind unit
        wind_label = tk.Label(master=settings_frame, text="Wind Unit:")
        wind_label.pack()
        wind_selected = tk.StringVar()
        wind_selected.set(self.wind_unit)
        wind_unit_selector = tk.OptionMenu(settings_frame, wind_selected, *self.wind_unit_options)
        wind_unit_selector.pack()
        
        # Pressure unit
        pressure_label = tk.Label(master=settings_frame, text="Pressure Unit:")
        pressure_label.pack()
        pressure_selected = tk.StringVar()
        pressure_selected.set(self.pressure_unit)
        pressure_unit_selector = tk.OptionMenu(settings_frame, pressure_selected, *self.pressure_unit_options)
        pressure_unit_selector.pack()

        # Rain unit
        rain_label = tk.Label(master=settings_frame, text="Rain Unit:")
        rain_label.pack()
        rain_selected = tk.StringVar()
        rain_selected.set(self.rain_unit)
        rain_unit_selector = tk.OptionMenu(settings_frame, rain_selected, *self.rain_unit_options)
        rain_unit_selector.pack()

        def close_settings():
            settings.destroy()
        # Update settings
        def update_settings(temp_unit, wind_unit, pressure_unit, rain_unit):
            self.temp_unit = temp_unit
            self.wind_unit = wind_unit
            self.pressure_unit = pressure_unit
            self.rain_unit = rain_unit
            return self.temp_unit, self.wind_unit, self.pressure_unit, self.rain_unit
        def getSettings(self):
            return self.temp_unit, self.wind_unit, self.pressure_unit, self.rain_unit

            

        
        # Update button
        update_button = tk.Button(master=settings, text="Update", command=update_settings(temp_selected.get(), wind_selected.get(), pressure_selected.get(), rain_selected.get()))
        update_button.pack()
        # Close button
        close_button = tk.Button(master=settings, text="Close", command=close_settings)
        close_button.pack()
    
    def getSettings(self):
        return self.temp_unit, self.wind_unit, self.pressure_unit, self.rain_unit


        
        


        


        

    

