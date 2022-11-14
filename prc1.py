import random
l=[]
lucky=[]
for i in range(1,101):
    l.append(i)
for i in range(10):
    num=random.choice(l)
    lucky.append(num)
    l.remove(num)
print("main list:",l)
print("lucky number:",lucky)


    
