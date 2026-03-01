import numpy as np

class StudentRank():

    def studentmark(self):
        studentMarkList=np.random.randint(1,101,(5,3))
        print(f"Student Marklist {studentMarkList}")
        return studentMarkList
    
    def studentMarkCal(self, studentMarkList, students, subjects):
        self.total = studentMarkList.sum(axis=1)
        for i in range(len(students)):
            print("Total Marks of ", students[i],self.total[i])
            

    def studentRank(self,students):
        sortedTotal = np.argsort(-self.total)
        ranks=np.empty_like(sortedTotal)
        ranks[sortedTotal]=np.arange(1,len(self.total)+1)
        print("Ranking")
        for i in range(len(students)):
            print(f"{students[i]} - Total Mark - {self.total[i]} Rank - {ranks[i]}")




StudentRank_Obj=StudentRank()

students = np.array(["Anu","vys","asd","WEW","dff"])
subjects = np.array(["eng","tam","adre"])

StudentMarkList=StudentRank_Obj.studentmark()
StudentRank_Obj.studentMarkCal(StudentMarkList, students, subjects)
StudentRank_Obj.studentRank(students)

    