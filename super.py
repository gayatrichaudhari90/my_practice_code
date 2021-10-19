class Student(object):
    def __init__(self,nm,r):
        self.name=nm
        self.roll=r
        print("Student constructor is called")
    def getdata(self):
        print(self.name,self.roll)

class Teacher(Student):
    def __init__(self,id,salary,nm,r):
        super().__init__(nm,r)
        self.id=id
        self.salary=salary
        print("Teacher constructor is called")

t=Teacher(1,salary=10000,nm="Rohan",r=101)
print(t.id)
print(t.salary)
print(t.name)
print(t.roll)