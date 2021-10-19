class Finance:
    def __init__(self):
        self.income=10000000
        self.__branch="Pune"

f=Finance()

class HRD:
    def __init__(self,f):
        self.head="shantanu"
        self.f=f
    def display(self):
        print("income is:",self.f.income)
        self.f.__branch="Mumbai"

h=HRD(f)
h.display()
print(f.__branch)
