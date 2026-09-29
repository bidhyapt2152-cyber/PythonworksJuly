from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass
    def get_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self):
        self.length=int(input("Enter length"))
        self.breadth=int(input("Enter breadth"))

    def get_area(self):
        print("Area",self.length*self.breadth)

    def get_perimeter(self):
        print("Perimeter",2*(self.length*self.breadth))

r=Rectangle()
r.get_area()
r.get_perimeter()



class Square(Shape):

    def __init__(self):
        self.side = int(input("Enter side: "))

    def get_area(self):
        print("Area:", self.side * self.side)

    def get_perimeter(self):
        print("Perimeter:", 4 * self.side)


s = Square()
s.get_area()
s.get_perimeter()





