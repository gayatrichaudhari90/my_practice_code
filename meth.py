class Parent(object):
    def salary(self):
        sal=10000
        return sal+500

class Child(Parent):
    def salary(self):
        sal=10000
        return sal+1000

c=Child()
print(c.salary())