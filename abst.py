from abc import ABC,abstractmethod
class Defence(ABC):
    @abstractmethod
    def Area(self):
        pass
    def Gun(self):
        print("AK47")
    
class Army(Defence):
    def Area(self):
        print("land")

class Navy(Defence):
    def Area(self):
        print("Sea")

class AirForce(Defence):
    def Area(self):
        print("Air")

a=AirForce()
a.Area()
a.Gun()
n=Navy()
n.Area()
n.Gun()
a1=Army()
a1.Area()
a1.Gun()
