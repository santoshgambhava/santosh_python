class Point:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("init called")
    def __str__(self):
        print("string called")
        return"{0},{1}".format(self.a,self.b)
    def __add__(self,obj):
        x=self.a+obj.a
        y=self.b+obj.b
        print("add called")
        return Point(x,y)
p1=Point(100,200)
print(p1)
p2=Point(300,400)
print(p2)
print("addition:",p1+p2)
