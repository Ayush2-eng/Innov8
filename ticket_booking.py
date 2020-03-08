import cv2
import os
import numpy as np
import mysql.connector
from tabulate import tabulate
from texttable import Texttable
import datetime
#from PIL import Image
import PIL.Image
from tkinter import *
import tkinter as tk

# Path for face image database
path = 'dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

page2 = Tk() # Opens new window
page2.title('Ticket Booking')
page2.geometry('1000x1000')
page2.configure(background="light pink")
page2.grid_rowconfigure(0, weight=1)
page2.grid_columnconfigure(0, weight=1)

# function to get the images and label data
def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:
        PIL_img = PIL.Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="facial ticket"
)
mycursor = mydb.cursor()
#def logged(station_id,station_name):
 # print ("welcome",station_name)


def logged(station_id,station_name):
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height

    flag=0

    while(flag==0):

        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        # For each person, enter one numeric face id
        #while True:

        def callback():
            #print ('Submitted')
            ourMessage1 ='Submitted'
            messageVar = Message(page2, text = ourMessage1) 
            messageVar.config(bg='white') 
            messageVar.pack( )
            
            face_name=textbox.get()
            print(face_name)            

            to_station=v.get()

            print(str(v.get()))

            mycursor = mydb.cursor()
            dest="SELECT name from station where id=%s"
            de=(to_station,)
            mycursor.execute(dest, de)
            myresult = mycursor.fetchall()

            for xy in myresult:
                to_station_name = xy[0]
            mycursor = mydb.cursor()
            date1=str(datetime.datetime.today())

            sql = "INSERT INTO customer(name, fromstation,tostation, date, status) VALUES (%s, %s, %s, %s, %s)"
            val = (face_name, station_id, to_station,date1,1)
            mycursor.execute(sql, val)
            mydb.commit()

            
            #print(mycursor.rowcount, "record inserted.")
            face_id=mycursor.lastrowid
            #a=int(station_id)
            #b=int(to_station)
            no=abs(int(station_id)-int(to_station))
            fare=str(no*10)
            t = Texttable()
            t.add_rows([['WELCOME TO Bombay Central STATION \n\n '+station_name+' Station \t'], ['Id: STATION00'+str(face_id)+'\t\tDate : '+date1], ['\nName : '+face_name.capitalize()+'  \n\nTo Station : '+str(to_station_name)+'\n'], ['Total Fare   \t:  '+fare+' Rs' ]])
            #print (t.draw())

            #main = Tk() 
            ourMessage =t.draw()
            messageVar = Message(page2, text = ourMessage) 
            messageVar.config(bg='white') 
            messageVar.pack( ) 

            #return textbox.get()

        lbl=Label(page2, text="Enter name",width=10  ,height=1  ,fg="white"  ,bg="grey" ,font=('times', 15, ' bold ') )
        lbl.place(x=50, y=100)

        textbox = Entry(page2,width=20  ,bg="white" ,fg="green",font=('times', 15))
        textbox.place(x=180, y=100)

        #face_name = str(textbox.get())
        #print(face_name)
        #face_name=str(callback)

        MyButton1 = Button(page2, text="Submit", width=10, command=callback)
        MyButton1.place(x=200, y=540)
        #MyButton1.pack()

        button =Button(page2, text='Exit', width=10, command=page2.destroy) 
        button.pack()

        #face_name = input('\n Enter Name : ')
        '''
        if face_name.isalpha():
            break
            
        else:      
          main3 = Tk() 
          ourMessage ='Please enter valid name'
          messageVar = Message(main3, text = ourMessage) 
          messageVar.config(bg='white') 
          messageVar.pack( ) 
          main3.mainloop( )
          #print ("\n[INFO] Please enter valid name")'''
        
        #print("\n")
        #if station_id!=12:

        #print("To North :\n")
        ''' mycursor = mydb.cursor()
        sql3 = "SELECT * FROM station where id!=%s"
        station=(station_id,)
        mycursor.execute(sql3,station)
        myresult = mycursor.fetchall()
        '''
        #for i in range(a,12):
        '''for x in myresult:
            #list.append("->")
            print("("+str(x[0])+")" +x[1], end=" -> ")
            #break'''

        def go_foward():
              
            '''print("**Finished**", end=" ")
            print("\n")'''
    
            '''
            if station_id!=1:
              print("To South :\n")
              mycursor = mydb.cursor()
              sql3 = "SELECT * FROM station where id<=%s"
              station=(station_id,)
              mycursor.execute(sql3,station)
              myresult = mycursor.fetchall()
              #for i in range(a,12):
              for x in reversed(myresult):
                #list.append("->")
                print("("+str(x[0])+")" +x[1], end=" -> ")
                  #break
              print("**Finished**", end=" ")
              '''
            ''' 
            while(True):
                to_station = input('\n\nEnter To Station : ')
                if to_station.isdigit()and int(to_station)<=12:
                    if int(to_station)==int(station_id):
                        print("\n[INFO] Both Source And Destination Cannot Be Same")
                    else:
                        break
                else:
                    print("\n[INFO] Please enter valid station id")
                    '''

            #print("\n [INFO] Initializing face capture. Look the camera and wait ...")
            
            #main = Tk() 
            ourMessage ='Initializing face capture. Look the camera and wait ...'
            messageVar = Message(page2, text = ourMessage) 
            messageVar.config(bg='lightgreen') 
            messageVar.pack( ) 

            # Initialize individual sampling face count
            count = 0

            #page2.after(2000, function=go_foward1())

            #def go_foward1():
             
            flag1=0              

            while(flag1==0):

                ret, img = cam.read()
                img = cv2.flip(img, 1) # flip video image vertically
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_detector.detectMultiScale(gray, 1.3, 5)

                face_id=mycursor.lastrowid

                for (x,y,w,h) in faces:

                    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
                    count += 1

                    # Save the captured image into the datasets folder
                    cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

                    cv2.imshow('image', img)

                k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
                #print(k)
                if k == 27:
                    flag1=1
                    #break
                elif count >= 10: # Take 10 face sample and stop video
                    flag1=1
                    #break
            
            #print("\n [INFO] Image Captured Successfully")
            #cam.release()

            #main1 = Tk() 
            ourMessage ='Image Captured Successfully. Training faces. It will take a few seconds. Wait ...'
            messageVar = Message(page2, text = ourMessage) 
            messageVar.config(bg='lightgreen') 
            messageVar.pack( ) 
            #main1.mainloop( ) 
            
            #print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
            faces,ids = getImagesAndLabels(path)
            recognizer.train(faces, np.array(ids))

            # Save the model into trainer/trainer.yml
            recognizer.write('trainer/trainer.yml')
            # Print the numer of faces trained and end program
            
            #print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
            
            #main2 = Tk() 
            ourMessage =str(len(np.unique(ids)))+' faces trained. Exiting Program'
            messageVar = Message(page2, text = ourMessage) 
            messageVar.config(bg='lightgreen') 
            messageVar.pack( ) 

            #exit_key=input("Press Enter to continue or q to loggout...")
            
            #if exit_key=='q':
                #print("You have been successfully logged out successfully!")
                
            cam.release()
            cv2.destroyAllWindows()
            flag=1
            #break

        f=Frame(page2, bg="light blue").place(x=100,y=100)
        v = IntVar() 
        Radiobutton(f, text="Borivali", variable=v, value=3,bg="pink", command=go_foward).pack(side="left")
        Radiobutton(f, text='Malad', variable=v, value=5,bg="pink", command=go_foward).pack(side="left")
        Radiobutton(f, text='Santacruz', variable=v, value=7, bg="pink", command=go_foward).pack(side="left")
        Radiobutton(f, text='Goregaon', variable=v, value=6, bg="pink", command=go_foward).pack(side="left")
        Radiobutton(f, text='Kandivali', variable=v, value=4, bg="pink", command=go_foward).pack(side="left")
        Radiobutton(f, text='Mira Road', variable=v, value=1, bg="pink", command=go_foward).pack(side="left")
        mainloop()


print("***********************WELCOME TO Bombay Central STATION***********************")
while(True):
    user_name = input('\n Enter user name :  ')
    password = input('\n Enter password :  ')
    sql3 = "SELECT * FROM station WHERE user_name = %s and password=%s"
    login = (user_name,password,)
    mycursor.execute(sql3, login)
    myresult = mycursor.fetchall()
    validate=len(myresult)
    if validate==1:
      for x in myresult:
        station_id=x[0]
        station_name=x[1]
        print ("\n***********************Welcome",station_name,"***********************")
        logged(station_id,station_name)
      break
    else:
      print("\n[INFO] Please enter valid username or password")










