
from tkinter import *
import tkinter as tk
import tkinter.messagebox as tm
#import pymysql
import mysql.connector


page2 = Tk() # Opens new window
page2.title('Ticket VIew')
page2.geometry('500x500')
page2.configure(background="light green")
page2.grid_rowconfigure(0, weight=1)
page2.grid_columnconfigure(0, weight=1)

lbl= tk.Label(page2, text="UserId",width=10  ,height=1  ,fg="white"  ,bg="grey" ,font=('times', 15, ' bold ') )
lbl.place(x=50, y=100)

textbox = tk.Entry(page2,width=20  ,bg="white" ,fg="green",font=('times', 15))
textbox.place(x=180, y=100)


def ticketview():
    #mydb = pymysql.connect("localhost","root","","python")
    mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="facial ticket"
    )
    mycursor = mydb.cursor()

    userid = int(textbox.get())
    print(userid)
    mycursor.execute("SELECT * FROM customer WHERE id = %d" %(userid))
    myresult = mycursor.fetchall()

    frame = Frame(page2)
    frame.pack(side="left")

    name=myresult[0][1]
    namehead=tk.Label(frame, text="Name", bg="green", fg="white").grid(row=0,column=0)
    namelbl=tk.Label(frame, text= name).grid(row=1,column=0)
    
    conct=myresult[0][2]
    concthead=tk.Label(frame, text="Contact Number", bg="green", fg="white").grid(row=0,column=1)
    conctlbl=tk.Label(frame, text= conct).grid(row=1,column=1)

    frms=myresult[0][3]
    frmshead=tk.Label(frame, text="From Station", bg="green", fg="white").grid(row=0,column=2)
    frmslbl=tk.Label(frame, text= frms).grid(row=1,column=2)

    tost=myresult[0][4]
    tosthead=tk.Label(frame, text="To Station", bg="green", fg="white").grid(row=0,column=3)
    tostlbl=tk.Label(frame, text= tost).grid(row=1,column=3)

    date=myresult[0][5]
    datehead=tk.Label(page2, text="Date and Time", bg="green", fg="white").grid(row=0,column=4)
    datelbl=tk.Label(page2, text= date).grid(row=1,column=4)


takedata = tk.Button(page2, text="Submit", command=ticketview ,fg="white"  ,bg="grey"  ,width=10  ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
takedata.place(x=50, y=150)
page2.mainloop()
