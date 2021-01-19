import sqlite3
from tkinter import *
import tkinter.messagebox
from update import *

#connect to the database
conn = sqlite3.connect('database.db')

#curser to move arround the database
c=conn.cursor()

#empty lists to later append the ids from the database
ids=[]

#tkinter window

class Application:
    def __init__(self,master):
        self.master=master

        #creating the frames of the master
        self.left=Frame(master,width=800,height=720,bg='lightgreen')
        self.left.pack(side=LEFT)

        self.right=Frame(master,width=400,height=720,bg='steelblue')
        self.right.pack()

        #labels for the wimdows
        self.heading=Label(self.left,text="CITY HOSPITAL APOINTMENT",font=('arial 40 bold'), fg='black', bg='lightgreen')
        self.heading.place(x=0,y=0)

        #labels for the patient's name
        self.name=Label(self.left,text="Patient's Name", font=('arial 18 bold'), fg='black',bg='lightgreen')
        self.name.place(x=0,y=100)

        # labels for the patient's age
        self.name = Label(self.left, text="Age", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.name.place(x=0, y=150)

        # labels for the patient's Gender
        self.name = Label(self.left, text="Gender", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.name.place(x=0, y=200)

        # labels for the patient's location
        self.name = Label(self.left, text="Address", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.name.place(x=0, y=250)

        # labels for the Appoinment time
        self.name = Label(self.left, text="Appoinment time", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.name.place(x=0, y=300)

        #labels for the phone number
        self.phone=Label(self.left,text="Phone Number", font=('arial 18 bold'), fg='black',bg='lightgreen')
        self.phone.place(x=0,y=350)

        # Entries for all labels
        self.name_ent=Entry(self.left,width=30)
        self.name_ent.place(x=250,y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=150)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=200)

        self.address_ent = Entry(self.left, width=30)
        self.address_ent.place(x=250, y=250)

        self.appoinment_time_ent = Entry(self.left, width=30)
        self.appoinment_time_ent.place(x=250, y=300)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=350)

        #button to submit the Entries
        self.submit=Button(self.left, text="Submit",width=20,height=2,bg='steelblue',command=self.add_appoinments)
        self.submit.place(x=250,y=400)

        # getting the number of appoinments fixed to view from the log
        sql2 = "SELECT ID FROM appoinments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        # ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids) - 1]

        # displaying the logs in the right frame
        self.log=Label(self.right,text="Logs :",font=('arial 20 bold'),fg='white',bg='steelblue')
        self.log.place(x=0,y=0)

        self.box = Text(self.right, width=45, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END,"Total Appointments till now : "+ str(self.final_id)+'\n')

    def add_appoinments(self):
        #getting the user input
        self.val1=self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.address_ent.get()
        self.val5 = self.appoinment_time_ent.get()
        self.val6= self.phone_ent.get()

        #checking if the user input is empty
        if(self.val1=='' or self.val2=='' or self.val3=='' or self.val4=='' or self.val5=='' or self.val6==''):
            tkinter.messagebox.showinfo("Warning","Please Fill up All Boxes")
        else:
            sql="INSERT INTO 'appoinments' (name,age,gender,location,scheduled_time,phone) VALUES(?,?,?,?,?,?)"
            c.execute(sql, (self.val1,self.val2,self.val3,self.val4,self.val5,self.val6))
            conn.commit()
            tkinter.messagebox.showinfo("Success","Appointment for "+self.val1+" has been created")

            self.box.insert(END,'Appoinment Fixed for '+str(self.val1)+ ' at '+ str(self.val5)+'\n')


#creating the object
root=Tk()


#resolution of the window
root.geometry("1200x720+0+0")

#preventing from resizing
root.resizable(False,False)

b=Application(root)

#mainloop
root.mainloop()
