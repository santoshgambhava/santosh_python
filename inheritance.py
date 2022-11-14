#single inheritance
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A:",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B:",self.b)
x=B()
x.getA(10)
x.putA()
x.getB(20)
x.putB()
print("*"*50)
#multilevel inheritance
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A:",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B:",self.b)
class C(B):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C:",self.c)
x=C()
x.getA(10)
x.putA()
x.getB(20)
x.putB()
x.getC(30)
x.putC()
print("*"*50)
#multiple inheritance
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A:",self.a)
class B:
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B:",self.b)
class C(A,B):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C:",self.c)
x=C()
x.getA(10)
x.putA()
x.getB(20)
x.putB()
x.getC(30)
x.putC()
print("*"*50)
#hierarchical inheritance
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A:",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B:",self.b)
class C(A):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C:",self.c)
x=C()
y=B()
x.getA(10)
x.putA()
y.getB(20)
y.putB()
x.getC(30)
x.putC()
print("*"*50)
#hybride inheritance
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A:",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B:",self.b)
class C(A):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C:",self.c)
class D(B,C):
    def getD(self,d):
        self.d=d
    def putD(self):
        print("D:",self.d)
x=D()

x.getA(10)
x.putA()
y.getB(20)
y.putB()
x.getC(30)
x.putC()
