class Employee:
    def __init__(self,nm,sal):
        self.name=nm
        self.salary=sal
    def __lt__(self,other):
        return self.salary<other.salary

e1=Employee('Jay',10000)
e2=Employee('Viru',20000)
e3=Employee('Basanti',30000)
print(e1<e2)
print(e3<e2)

print(isinstance(e1,Employee))
print(isinstance(20.4,list))
if isinstance(20.4,Employee):
    print(e5.name)
else:
    print("no object exist")
