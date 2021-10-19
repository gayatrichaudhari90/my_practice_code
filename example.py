class Employee(object):
    company_name="infosis"
    @classmethod
    def get_company_name(cls):
        print("Company name is:",cls.company_name)
    @staticmethod
    def setbonus(b):
        print("Bonus is:",b)

class Manager(Employee):
    batch_id=1000
    

e1=Employee()
m1=Manager()
print(m1.company_name)
m1.get_company_name()
m1.setbonus(2000)
print(e1.batch_id)