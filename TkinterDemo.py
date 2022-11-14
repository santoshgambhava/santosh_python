from tkinter import *
import mysql.connector

import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_30"
        )

def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert Status","all filds are mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        quary="insert into student(fname,lname,email,mobile)value(%s,%s,%s,%s)"
        args(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(queary,args)
        conn.close()

root=Tk()
root.title("my tkinter example")
root.geometry("340x400")
root.resizable(width="False",height="False")

l_id=Label(root,text="ID")
l_id.place(x=50,y=50)

l_fname=Label(root,text="FIRST NAME")
l_fname.place(x=50,y=100)

l_lname=Label(root,text="LAST NAME")
l_lname.place(x=50,y=150)

l_email=Label(root,text="EMAIL")
l_email.place(x=50,y=200)

l_mobile=Label(root,text="MOBILE")
l_mobile.place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

e_email=Entry(root)
e_email.place(x=150,y=200)

e_mobile=Entry(root)
e_mobile.place(x=150,y=250)

insert=Button(root,text="INSERT",bg="black",fg="white",command=insert_data)
insert.place(x=50,y=300)

serch=Button(root,text="SERCH",bg="black",fg="white")
serch.place(x=100,y=300)

update=Button(root,text="UPDATE",bg="black",fg="white")
update.place(x=148,y=300)

delete=Button(root,text="DELETE",bg="black",fg="white")
delete.place(x=205,y=300)










