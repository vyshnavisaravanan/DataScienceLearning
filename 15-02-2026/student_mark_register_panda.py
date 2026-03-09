import numpy as np
import pandas as pd

class Student_Mark_Panda:
    def __init__(self):
        self.data = {
            "name" : ["name1", "name2", "name3", "name4"],
            "maths" : [66,44,24,55],
            "science" : [67,87,45,57],
            "computer":[3,84,78,89]}
        self.df = pd.DataFrame(self.data)
        
    def calculate_total(self):
        self.df["total"]= self.df["maths"] + self.df["science"] +self.df["computer"]
    
    def calculate_rank(self):
        self.df["rank"] = self.df["total"].rank(ascending=False).astype(int)
        
    def calculate_top3(self):
        self.top3 = self.df.sort_values("rank").head(2)
        print(self.top3)
        
    
    def display_report(self):
        print(self.df)
        


obj = Student_Mark_Panda()
obj.calculate_total()
obj.calculate_rank()
obj.calculate_top3()
obj.display_report()