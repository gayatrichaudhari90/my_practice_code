class Student:
    marks=95
    def __init__(self,nm,m):
        self.name=nm
        self.marks=m
    @staticmethod
    def give_bonus(bonus):
        print(Student.marks+bonus)
s1=Student("Kiran",95)
bonus=int(input("How much bonus you wanna give?:"))
s1.give_bonus(bonus)
    