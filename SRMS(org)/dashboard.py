from tkinter import*
from PIL import Image,ImageTk #=====pip  install pillow
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from login import login_system
from tkinter import messagebox
import sqlite3
import time
import os
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("School Result Managment System")
        self.root.geometry("1300x700+0+0")
        self.root.config(bg="white")

        #===Icons===
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")

        # ===title====
        title=Label(self.root,text="School Result Managment System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)

        # ====Menu====
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=70,y=70,width=1200,height=80)
        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=50,y=5,width=150,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=150,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=440,y=5,width=150,height=40)
        btn_view=Button(M_Frame,text="View",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=640,y=5,width=150,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=840,y=5,width=150,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1040,y=5,width=150,height=40)

        # === Digital Clock ===
        self.clock_label = Label(self.root, font=("times new roman", 15, "bold"), bg="#033054", fg="white")
        self.clock_label.place(x=1150, y=10, width=150, height=30)
        self.update_clock()

        # =====Content_Window=====

        self.bg_img=Image.open(r"images/bg.png")
        self.bg_img=self.bg_img.resize((920,350),Image.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

        # =====Update_details====

        self.lbl_course=(Label(self.root,text="Totle Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white"))
        self.lbl_course.place(x=400,y=530,width=300,height=100)

        self.lbl_student=(Label(self.root,text="Total Student\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white"))
        self.lbl_student.place(x=710,y=530,width=300,height=100)

        self.lbl_result=(Label(self.root,text="Totle Results\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white"))
        self.lbl_result.place(x=1020,y=530,width=300,height=100)
        # ===footer====
        footer=Label(self.root,text="SRMS - School Result Managment System\nContact us for any Technical Issue:9741685837",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

        self.update_details()

# ====================================================================================

    def update_clock(self):
        """Updates the clock label with the current time."""
        current_time = time.strftime("%H:%M:%S")  # Get the current time in HH:MM:SS format
        self.clock_label.config(text=current_time)
        self.clock_label.after(1000, self.update_clock)

    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")

            cur.execute("SELECT * FROM student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Student\n[{str(len(cr))}]")

            cur.execute("SELECT * FROM result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")

            self.lbl_course.after(200,self.update_details)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def add_login(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = login_system(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Do You Really Want to Logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op=messagebox.askyesno("Do You Really Want to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()