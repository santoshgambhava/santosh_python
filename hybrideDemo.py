class Shape:
    def Shape(self):
        print("shape:")

    def getS(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
    def putS(self):
        print("lengh:",self.l)
        print("base:",self.b)
        print("height:",self.h)
class Sqare(Shape):
    def sqare(self):
        print("sqare:")

    def areaofsqare(self):
        print("sqare is:",4*self.l)

class Rectangle(Shape):
    def rectangle(self):
        print("rectangle:")

    def areaofreactangle(self):
        print("reactangle is:",2*self.l*self.b)

class Box(Sqare,Rectangle):
    def box(self):
        print("box")
    def areaofbox(self):
        print("box is:",self.h*self.b*self.l)
b1=Box()
b1.Shape()
b1.getS(6,7,8)
b1.putS()
b1.sqare()
b1.areaofsqare()
b1.rectangle()
b1.areaofreactangle()
b1.box()
b1.areaofbox()
