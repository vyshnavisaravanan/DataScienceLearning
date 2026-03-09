import numpy as np

class WeatherAnalytic:
    def __init__(self):
        self.weatherreport = np.random.randint(1,50,(7,3))
        self.days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        self.grid = ["Temperature","Rainfall","Humidity"]

    def display_weather(self):
        print("📊 Weekly Weather Data (Temp, Rainfall, Humidity):")
        for day, data in zip(self.days, self.weatherreport):
            print(f"{day}: {data}")

    def analyse_weather(self):
        temp_col = self.weatherreport[:,0]
        rain_col = self.weatherreport[:,1]
        humidity_col = self.weatherreport[:,2]

        max_temp_index = temp_col.argmax()
        max_rain_index = rain_col.argmax()
        max_humidity_index = humidity_col.argmax()

        print("\n📈 Weather Analysis:")
        print("Highest Temperature:", temp_col[max_temp_index], "on", self.days[max_temp_index])
        print("Highest Rainfall:", rain_col[max_rain_index], "on", self.days[max_rain_index])
        print("Highest Humidity:", humidity_col[max_humidity_index], "on", self.days[max_humidity_index])

# Usage
wa = WeatherAnalytic()
wa.display_weather()
wa.analyse_weather()