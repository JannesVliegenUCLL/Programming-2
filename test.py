class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # werkt als "getter", waneer je naar x vraagt, zal hij dit opvragen.
    @property
    def x(self):
        return self.__x

    @x.setter  # Waneer je x wilt zetten naar een getal, zal vsc refereren naar deze functie
    def x(self, value):
        if value < 0:
            raise ValueError("x mag niet niet negatief zijn.")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y mag niet negatief zijn.")
        self.__y = value


p = Point(10, 5)
print(p.x)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class Distance:
    def __init__(self, waarde_meter):
        self.waarde_meter = waarde_meter
    @staticmethod #         Staticmethod zorgt er voor dat je de functie kan gebruiken zonder een Object te definieren, door {Class}.{staticmethod}(value) te doen
    def meter(value):
        return value
    @staticmethod
    def milimeter(value):
        return value*1000
    @staticmethod
    def miles(value ):
        return value/1600
    
print(Distance.miles(800))
print(Distance.miles(700))
# d=Distance(800)
# print(d.milimeter())

# d2=Distance(700)
# print(d2.milimeter())
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age = age
    def print_information(self):
        return f'{self.name}, {self.age}'

class Dog(Animal): #de (Animal) zorgt er voor dat de functies van Animal geërft worden door de class Dog
    pass
    
class Cat(Animal):
    pass

class Bird(Animal):
    pass
d = Dog("Lassy",15)
d.print_information()