'''
x=open("myntra.txt","r")
print(x.read())
x.close()
y=open("xyz.txt","w")
y.write("hello, my name is Santosh.")
y.close()
z=open("xyz.txt","a")
z.write("\nNice to meet you.")
z.close()
x=open("myntra.txt","r")
z=open("xyz.txt","w")
z.write(x.read())
x.close()
z.close()

import csv
with open("abc.csv","w")as x:
    file=csv.writer(x,delimiter="\t")
    file.writerow([1,"santosh"])
    file.writerow([2,"Dhara"])
    x.close()
'''
import csv
with open("abc.csv","r")as x:
    file=csv.reader(x)
    for i in file:
        print(i)
    x.close()
