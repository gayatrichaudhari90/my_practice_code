class Student:
    def __init__(self,nm,roll):
        self.name=nm
        self.roll=roll
    def get_data(self):
        print("name of student is:",self.name)
s1=Student("Kiran",101)
s2=Student("Rohan",102)
s2.get_data()