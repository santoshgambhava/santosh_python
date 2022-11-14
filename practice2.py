import practice
while True:
    print("1. pattern")
    print("2. oddeven")
    print("3. maxoftwo")
    print("4. maxofthree")
    print("5. fibbonacci")
    print("6. prime")
    print("7. exit")

    choice=int(input("enter choice"))
    if choice==1:
        n=int(input("enter number"))
        practice.pattern(n)
    elif choice==2:
        a=int(input("enter number"))
        practice.oddeven(a)
    elif choice==3:
        c=int(input("enter number"))
        d=int(input("enter number"))
        practice.maxoftwo(c,d)
    elif choice==4:
        a=int(input("enter number"))
        b=int(input("enter number"))
        c=int(input("enter number"))
        practice.maxofthree(a,b,c)
    elif choice==5:
        n=int(input("enter number"))
        practice.fibbonacci(n)
    elif choice==6:
        a=int(input("enter number"))
        practice.prime(a)
    else:
        break
