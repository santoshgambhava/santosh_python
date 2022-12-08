'''
Write python program that swap two number with temp variable and
without temp variable.
'''
print("with temp")
x=int(input("enter x:"))
y=int(input("enter y:"))
temp=x
x=y
y=temp
print("x after swap:",x)
print("y after swap:",y)

print("without temp")
x=int(input("enter x:"))
y=int(input("entey y:"))
x,y=y,x
print("x after swap:",x)
print("y after swap:",y)
