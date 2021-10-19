class Book:
    def __init__(self,pages):
        self.pages=pages 
    def __str__(self):
        return "no of total pages:"+str(self.pages)
    def __add__(self,other):
        total=self.pages+other.pages
        b=Book(total)
        return b

b1=Book(200)
b2=Book(300)
b3=Book(700)
b4=Book(1200)
print(b1+b2)
print(b1+b2+b3+b4)