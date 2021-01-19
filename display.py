from tkinter import *
import sqlite3
import pyttsx3
import tkinter.messagebox

#connecting the database
conn=sqlite3.connect('database.db')
c=conn.cursor()

#empty lists to append later
number =[]
patients=[]

sql="SELECT * FROM appoinments"
res= c.execute(sql)
for r in res:
    ids=r[0]
    name=r[1]
    number.append(ids)
    patients.append(name)

class Application:
    def __init__(self,master):
        self.master=master

        self.x=0

        self.heading=Label(self.master,text="Appointments",font=("arial 60 bold"),fg="green")
        self.heading.place(x=350,y=0)

        #button for change patient's
        self.change=Button(self.master,text="Next Patient", width=25,height=2,bg='steelblue',command=self.fun)
        self.change.place(x=500,y=600)

        self.n=Label(self.master,text="10",font=("arial 150 bold"))
        self.n.place(x=500,y=200)

        self.pname = Label(self.master, text="gourav kumar", font=("arial 80 bold"))
        self.pname.place(x=300, y=400)

    def fun(self):
        self.n.config(text=str(number[self.x]))
        self.pname.config(text=str(patients[self.x]))
        self.x+=1
        if(len(patients)==self.x):
            tkinter.messagebox.showinfo("Finished","All Apointments done for the day")

root=Tk()
b=Application(root)
root.geometry("1200x720+0+0")
root.resizable(False,False)
root.mainloop()
