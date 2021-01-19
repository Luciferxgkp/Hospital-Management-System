from tkinter import *
import tkinter.messagebox
import sqlite3

conn=sqlite3.connect('database.db')
c=conn.cursor()

class Application:
    def __init__(self,master):
        self.master=master

        #heading label
        self.heading=Label(master,text="Update Appointments",fg='steelblue',font=('arial 40 bold'))
        self.heading.place(x=150,y=0)

        #search criterian --> name
        self.name=Label(master, text="Enter the Patient's Name", font=("arial 10 bold"))
        self.name.place(x=0,y=70)

        #entry for the name
        self.name_ent=Entry(master,width=30)
        self.name_ent.place(x=300,y=70)

        #submit button
        self.search=Button(master,text="Search",width=12,height=1,bg="steelblue", command=self.search_db)
        self.search.place(x=350,y=102)

    #Function to search
    def search_db(self):
        self.input=self.name_ent.get()
        sql="SELECT * FROM appoinments WHERE name like ?"
        self.res=c.execute(sql,(self.input,))
        for self.row in self.res:
            self.name1=self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.time = self.row[6]
            self.phone = self.row[5]

        #creating the update form
        self.uname=Label(self.master,text="Patient's Name",font=("arial 18 bold"))
        self.uname.place(x=0,y=140)

        self.uage = Label(self.master, text="Age", font=("arial 18 bold"))
        self.uage.place(x=0, y=180)

        self.ugender = Label(self.master, text="Gender", font=("arial 18 bold"))
        self.ugender.place(x=0, y=220)

        self.ulocation = Label(self.master, text="Address", font=("arial 18 bold"))
        self.ulocation.place(x=0, y=260)

        self.utime = Label(self.master, text="Appintment Time", font=("arial 18 bold"))
        self.utime.place(x=0, y=300)

        self.uphone = Label(self.master, text="Phone Number ", font=("arial 18 bold"))
        self.uphone.place(x=0, y=340)

        #creating the entries for the details
        self.uname_ent=Entry(self.master, width=30)
        self.uname_ent.place(x=300,y=148)
        self.uname_ent.insert(END,str(self.name1))

        self.uage_ent = Entry(self.master, width=30)
        self.uage_ent.place(x=300, y=188)
        self.uage_ent.insert(END,str(self.age))

        self.ugender_ent = Entry(self.master, width=30)
        self.ugender_ent.place(x=300, y=228)
        self.ugender_ent.insert(END,str(self.gender))

        self.ulocation_ent = Entry(self.master, width=30)
        self.ulocation_ent.place(x=300, y=268)
        self.ulocation_ent.insert(END,str(self.location))

        self.utime_ent = Entry(self.master, width=30)
        self.utime_ent.place(x=300, y=308)
        self.utime_ent.insert(END,str(self.time))

        self.uphone_ent = Entry(self.master, width= 30)
        self.uphone_ent.place(x=300, y=348)
        self.uphone_ent.insert(END,str(self.phone))

        #buttom to update
        self.update=Button(self.master,text="Update",width=20,height=2,bg="steelblue",command=self.update_db)
        self.update.place(x=320,y=400)

        #button to delete
        self.delete = Button(self.master, text="Delete", width=20, height=2, bg="red", command=self.delete_db)
        self.delete.place(x=120, y=400)


    def update_db(self):
        self.var1=self.uname_ent.get()
        self.var2 = self.uage_ent.get()
        self.var3 = self.ugender_ent.get()
        self.var4 = self.ulocation_ent.get()
        self.var5 = self.utime_ent.get()
        self.var6 = self.uphone_ent.get()

        query="UPDATE appoinments SET name=?,age=? , gender=?, location=?, phone=?, scheduled_time=? WHERE name LIKE ?"
        c.execute(query,(self.var1,self.var2,self.var3,self.var4,self.var5,self.var6,self.name_ent.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Updated","Successfully Updated")

    def delete_db(self):
        #delete the appointments
        sql2="DELETE FROM appoinments WHERE name LIKE ?"
        c.execute(sql2,(self.name_ent.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Deleted","Deleted Successfully")
        self.uname_ent.destroy()
        self.uage_ent.destroy()
        self.ugender_ent.destroy()
        self.ulocation_ent.destroy()
        self.utime_ent.destroy()
        self.uphone_ent.destroy()



#creating the objects
root=Tk()
b=Application(root)
root.geometry("1200x720+0+0")
root.resizable(False,False)
root.mainloop()