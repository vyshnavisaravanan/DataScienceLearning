import numpy as ny

class StudentMarkRegister():
    def __init__ (self,students, subject):
        self.students=ny.array(students)
        self.subject=ny.array(subject)
        self.studentMarkList = None
        self.total = None
        self.rank = None
    
    def displayMark(self, low=0, high=101, no_of_student=5, no_of_subject=4):
        self.studentMarkList =ny.random.randint(low,high, (no_of_student,no_of_subject))
        print("Student Mark List", self.studentMarkList)

    def calculateTotal(self,students):
        self.total=self.studentMarkList.sum(axis=1)
        print("----Total Marks of Students ----")
        for i in range(len(self.students)):
            print(f"  {students[i]}     is    {self.total[i]}")

    def calculateRank(self, students):
        sortedList = ny.argsort(-self.total)
        self.rank=ny.empty_like(sortedList)
        self.rank[sortedList]= ny.arange(1,len(self.total)+1)

        print("-------Student Ranking---------")
        for i in range(len(self.students)):
            print(f"{self.students[i]} - Total: {self.total[i]} - Rank: {self.rank[i]}")

    def subjectTopper(self, students):
        topperIndices=self.studentMarkList.argmax(axis=0)
        print("------Subject Toppers --------")
        for i,sub in enumerate(self.subject):
            print(f"Topper in {sub}: {self.students[topperIndices[i]]} with mark {self.studentMarkList[topperIndices[i],i]}")   


students = ny.array(["Anu","vys","asd","WEW","dff"])
subjects = ny.array(["eng","tam","adre"])

SMR = StudentMarkRegister(students,subjects)

SMR.displayMark()
SMR.calculateTotal(students)
SMR.calculateRank(students)
SMR.subjectTopper(students)