import numpy as np

class weather_analtic():
    def __init__(self):
        self.weatherreport = np.random.randint(1,50,(7,3))
        self.days=(["sunday","Monday","Tuesday", "Wednesday", "thursday", "Friday", "Saturday"])
        self.grid=(["weather","Rainfall","humidity"])
    
    def display_weather(self):
        print(self.weatherreport)
    
   
    def analyse_weather(self):
    # Get the index of the day with highest temperature for each grid
        highest_all_grid = self.weatherreport.argmax(axis=0)
        print("Highest temp indices per grid:", highest_all_grid)

    # Loop over each day and grid
        for day, grid1 in zip(self.days, self.grid):
            day_index = highest_all_grid[grid1]  # Use the current grid, not self.grid
            print(f"Highest temp at grid {grid1}: {self.weatherreport[day_index, grid1]} on {self.days[day_index]}")

        # If you have other weather metrics (like rainfall, humidity), you can do similar:
        # print("Highest Rainfall", highest_rainfall[grid])
        # print("Highest Humidity", highest_humidity[grid])



wa = weather_analtic()
wa.display_weather()
wa.analyse_weather()