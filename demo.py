class Demo:
    def __init__(self):
        self.a=20
        self.__a=30
d=Demo()
print(d.a)
# print(d.__a)
print(d.__dict__)

print(d._Demo__a)