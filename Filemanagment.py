file=open("zara.txt","w")
file.write("this is file managment demo using by python.")
file.close()

file=open("zara.txt","r")
print(file.read())
file.close()

file=open("zara.txt","a")
file.write("\nNow this file is open.")
file.close()
file=open("zara.txt","r")
print(file.read())
file.close()

file=open("amzone.txt","w+")
print("this is a huge online shopping platform.")
file.tell()
file.seek(0)
print(file.read())
file.close()