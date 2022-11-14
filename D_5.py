#function with no argument & no return value

def printline():
    print("*"*35)
printline()    
print("welcom to home")
printline()

#function with argument & no return value
def add(a,b):
    print("addition:",a+b)
x=int(input("enter value:"))
y=int(input("enter value:"))
printline()
add(x,y)
printline()
printline()
add(x,y)
printline()
#function with argument & return value
def sub(a,b):
    return a-b
printline()
x=int(input("enter value:"))
y=int(input("enter value:"))
ans=sub(x,y)
print("substraction:",ans)
printline()
