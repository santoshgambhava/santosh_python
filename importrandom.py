import random
data=open("data.txt","w")
for i in range(10):
    data.write(str(random.randint(1,100))+",")
data.close()
data=open("data.txt","r")
odd=open("odd.txt","w")
even=open("even.txt","w")
prime=open("prime.txt","w")
sqare=open("sqare.txt","w")
cube=open("cube.txt","w")
l=data.read().split(",")[:-1]
for i in l:
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")
for i in l:
    if int(i)%2!=0:
        for j in range(3,int((int(i))/2)+1,2):
            if  (int(i))%j==0:
                break
        else:
            prime.write(i+",")
    else:
            print("is not prime")
for i in l: 
    sq=int(i)
    print(sq*sq)
    sqare.write(str(sq*sq)+",")
for i in l:
    cq=int(i)
    print(cq**(1/3))
    cube.write(str(cq**(1/3))+",")
data.close()
even.close()
odd.close()
prime.close()
sqare.close()
cube.close()
print("data file cotent")
data=open("data.txt","r")
print(data.read())
data.close()
print("even file content")
even=open("even.txt","r")
print(even.read())
even.close()
print("odd file content")
odd=open("odd.txt","r")
print(odd.read())
odd.close()
print("prime file content")
prime=open("prime.txt","r")
print(prime.read())
prime.close()
print("sqare file content")
sqare=open("sqare.txt","r")
print(sqare.read())
sqare.close()
print("cube file content")
cube=open("cube.txt","r")
print(cube.read())
cube.close()

