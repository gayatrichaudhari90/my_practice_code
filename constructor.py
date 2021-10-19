class Student(object):
    def __init__(self,nm,r):
        self.name=nm
        self.roll=r
    def getdata(self):
        print(self.name,self.roll)

class Teacher(Student):
    pass
t=Teacher("Rohan",101)
print(t.name)
print(t.roll)
t.getdata()
s=Student("Prem",102)
s.getdata()