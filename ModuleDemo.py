import UDF

while True:
    print("1. pattern")
    print("2. maxoftwo")
    print("3. maxofthree")
    print("4. oddeven")
    print("5. fibonacci")
    print("6. prime")
    print("7. Exit")

    choice=int(input("enter choice:"))

    if choice==1:
        a=int(input("enter value:"))
        UDF.pattern(a)

    elif choice==2:
        a=int(input("enter value:"))
        b=int(input("enter value:"))
        UDF.maxoftwo(a,b)
    elif choice==3:
        a=int(input("enter value:"))
        b=int(input("enter value:"))
        c=int(input("enter value:"))
        UDF.maxofthree(a,b,c)
    elif choice==4:
        a=int(input("enter value:"))
        UDF.oddeven(a)
    elif choice==5:
        a=int(input("enter value:"))
        UDF.fibonacci(a)
    elif choice==6:
        a=int(input("enter value:"))
        UDF.prime(a)
    else:
        break
     
