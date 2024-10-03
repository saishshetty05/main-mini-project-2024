from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root    
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

            # --------------------------Variables-----------video3-------
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        

        img=Image.open(r"C:\Users\Hp\Desktop\facerec2\college images\sies.jpg")
        width, height=1530, 790
        img=img.resize((1530,790), Image.LANCZOS) 
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=790)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)



        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=130,width=1480,height=600)


        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)

        img_left=Image.open(r"C:\Users\Hp\Desktop\facerec2\college images\students-in-classroom.jpg")
        width, height=740, 130
        img_left=img_left.resize((740,130), Image.LANCZOS) 
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        bg_img=Label(Left_frame,image=self.photoimg_left)
        bg_img.place(x=5,y=0,width=740,height=130)

        #current course information frame
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=740,height=115)

        # department
        dep_label=Label(current_course_frame, text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        # course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #year
        year_label=Label(current_course_frame, text="Course",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2023-24","2024-25","2025-26","2026-27")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #sem
        semester_label=Label(current_course_frame, text="Course",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","sem-1","sem-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #class student information frame
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=740,height=300)

        # student id
        student_id_label=Label(class_student_frame, text="Student_ID:",font=("times new roman",13,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        student_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # student name
        student_name_label=Label(class_student_frame, text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # class division 
        class_div_label=Label(class_student_frame, text="Class Divison:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Roll no
        roll_no_label=Label(class_student_frame, text="Roll_No:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # gender
        gender_label=Label(class_student_frame, text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # email
        email_label=Label(class_student_frame, text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # phone no
        phone_no_label=Label(class_student_frame, text="Phone_NO:",font=("times new roman",13,"bold"),bg="white")
        phone_no_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        phone_no_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        # radio Buttons
        radionbtn1=ttk.Radiobutton(class_student_frame,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0)

        radionbtn2=ttk.Radiobutton (class_student_frame,text="No Photo Sample",value="Yes") 
        radionbtn2.grid(row=6,column=1)

        #bbuttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white") 
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)
        
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)




        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=800,y=10,width=660,height=580)

        # //Search system
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=730,height=70)

        Search_label=Label(Search_frame, text="Search By:",font=("times new roman",13,"bold"),bg="red",fg="white")
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Search_combo=ttk.Combobox(Search_frame,font=("times new roman",13,"bold"),state="readonly",width=20)
        Search_combo["values"]=("Select ","Roll_no","Phone_No")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        Search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        Search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=4)

        
        showALL_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showALL_btn.grid(row=0,column=4,padx=4)

    #    ==================================table frame==========================
       
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=730,height=350)


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","DOB","email","Phone","Address")).xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=BOTTOM,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table["show"]="headings"

        self.student_table.coloumn("dep",width=100)
        self.student_table.coloumn("course",width=100)
        self.student_table.coloumn("year",width=100)
        self.student_table.coloumn("sem",width=100)
        self.student_table.coloumn("id",width=100)
        self.student_table.coloumn("name",width=100)
        self.student_table.coloumn("div",width=100)
        self.student_table.coloumn("gender",width=100)
        self.student_table.coloumn("dob",width=100)
        self.student_table.coloumn("email",width=100)
        self.student_table.coloumn("Phone",width=100)
        self.student_table.coloumn("Address",width=100)

        self.student_table.pack(fill=BOTH,expand=1)


        # ---------------------------------student declaration ----------------video 3

        def add_data(self):
             pass







reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop() 