from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root    
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="black",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)


// first image
         img_top=Image.open(r"C:\Users\Hp\Desktop\facerec2\college images\students-in-classroom.jpg")
//insert a new photo in the above line---------         
        img_top=img_top.resize((1530,325), Image.ANTIALIAS) 
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)

//second image
         img_bottom=Image.open(r"C:\Users\Hp\Desktop\facerec2\college images\students-in-classroom.jpg")
         // change image
        img_bottom=img_top.resize((1530,325), Image.ANTIALIAS) 
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=440,width=1530,height=325)
        //change x and y,width and height according to the placement of image(650)

//button
         b1_1=Button(f_lbl,text="FACE RECOGNITION",cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)
//CHANGE X,Y WIDTH AND HEIGHT AND TEXT 


//---------------FACE RECOGNITION----=-------------


    def face_recog(self): 
         def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
         gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
         features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

         coord=[]
         
         for (x,y,w,h) in features:
         cv2.rectangle(img(x,y),(x+w,y+h),(0,255,0),3)
         id,predict=clf.predict(gray_image[y:y+h,x:x+w])
         confidence=int((100*(1-predict/300)))
 
        //update func
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("Select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                 my_cursor.execute("Select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                 my_cursor.execute("Select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)



                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else: 
                   cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)
                   cv2.PutText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]

            return coord

        def recognize(img,clf,faceCascade):
             coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"FACE",clf)
             return img 

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier)                


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()         