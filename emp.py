class Employee:
    def __init__(self,name,sal,dept):
        self.name=name
        self.salary=sal
        self.department=dept
    def get_data(self):
        print(self.salary)
        
emp1=Employee('sachin',10000,'computer')
emp2=Employee('akshay',12000,'mechanical')
print("employee1 salary is:",emp1.salary)
print(f"{emp1.name} salary is:{emp1.salary}")