class Parrot:
    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")

    
class Fish:
    def fly(self):
        print("Fish can't fly")

    def swim(self):
        print("Fish can swim")

p1=Parrot()
f1=Fish()
p1.fly()
p1.swim()
f1.fly()
f1.swim()

