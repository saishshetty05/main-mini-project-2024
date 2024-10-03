from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root    
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        img=Image.open(r"C:\Users\Hp\Desktop\facerec2\college images\sies.jpg")
        width, height=1530, 790
        img=img.resize((1530,790), Image.LANCZOS) 
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=790)

        title_lbl=Label(bg_img,text="FACE RECOGNTION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #student Button
        img1=Image.open(r"C:\Users\Hp\Desktop\facerec2\college images\students.jpg")
        width, height=220, 220
        img1=img1.resize((220,220), Image.LANCZOS) 
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(bg_img,image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


        #detectface Button
        img2=Image.open(r"C:\Users\Hp\Desktop\facerec2\college images\facedetector.jpg")
        width, height=220, 220
        img2=img2.resize((220,220), Image.LANCZOS) 
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(bg_img,image=self.photoimg2,cursor="hand2")
        b1.place(x=600,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=600,y=300,width=220,height=40)


        #Attendance Button
        img3=Image.open(r"C:\Users\Hp\Desktop\facerec2\college images\attendance.jpg")
        width, height=220, 220
        img3=img3.resize((220,220), Image.LANCZOS) 
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(bg_img,image=self.photoimg3,cursor="hand2")
        b1.place(x=1000,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=300,width=220,height=40)


        #Trainface Button
        img4=Image.open(r"C:\Users\Hp\Desktop\facerec2\college images\traindata.jpg")
        width, height=220, 220
        img4=img4.resize((220,220), Image.LANCZOS) 
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="TrainFace",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=600,width=220,height=40)


        #Photos Button
        img5=Image.open(r"C:\Users\Hp\Desktop\facerec2\college images\photos.jpg")
        width, height=220, 220
        img5=img5.resize((220,220), Image.LANCZOS) 
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=600,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=600,y=600,width=220,height=40)


         #Exit Button
        img6=Image.open(r"C:\Users\Hp\Desktop\facerec2\college images\exit.jpeg")
        width, height=220, 220
        img6=img6.resize((220,220), Image.LANCZOS) 
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=1000,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=600,width=220,height=40)


        # ===============functions=============== video 3----------------------------

        def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)

    




    



        














if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()     











   



