from tkinter import*
from PIL import Image,ImageTk,ImageDraw #=====pip  install pillow
from tkinter import ttk,messagebox
from datetime import *
import time
from math import *
import sqlite3
import os


class login_system:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1200x800+80+50")
        self.root.config(bg="#fafafa")

        # ==========Variables==================
        self.email = StringVar()
        self.password = StringVar()

        # ==============Frames============
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=650, y=135, width=350, height=460)

        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="white").place(x=0,y=30,relwidth=1)

        email = Label(login_frame, text="EMAIL ADDRESS", font=("Andalus", 15), bg="white", fg="#767171").place(x=50,y=100)
        self.txt_email = Entry(login_frame, textvariable=self.email, font=("times new roman", 15), bg="#ECECEC")
        self.txt_email.place(x=50, y=140, width=250)

        pass_ = Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171").place(x=50,y=200)
        self.txt_pass_ =Entry(login_frame, textvariable=self.password, show="*", font=("times new roman", 15),bg="#ECECEC")
        self.txt_pass_.place(x=50, y=240, width=250)

        #===Icons===
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")

        # ===title====
        title=Label(self.root,text="Login / Sign Up",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)

    # =============Images===============
        self.phone_Image=ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_Phone_image=Label(self.root,image=self.phone_Image,bd=0).place(x=200,y=90)


  # ======buttons==================
        self.btn_login=Button(login_frame,text='Log In',font=("Arial Rounded MY Bold ",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2",command=self.login)
        self.btn_login.place(x=50,y=300,width=250,height=35)

        hr= Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=355)

        self.btn_forget=Button(login_frame,text="Forget Password?",font=("times new roman",13),bg="white",fg="#00759E",cursor="hand2",bd=0,activebackground="white",activeforeground="#00759E",command=self.forget_password_window)
        self.btn_forget.place(x=100,y=390)

   # ==============Frame 2============
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=600,width=350,height=60)

        lbl_reg=Label(register_frame,text="Don't have any account ?",font=("times new roman",13),bg="white").place(x=40,y=20)
        btn_signup= Button(register_frame,command=self.register_window,text="Sign Up", font=("times new roman", 15,"bold"), bg="white",fg="#00759E", cursor="hand2", bd=0, activebackground="white", activeforeground="#00759E")
        btn_signup.place(x=220, y=15)

    # =========Animation Images============
        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2=ImageTk.PhotoImage(file="images/im2.png")
        self.im3=ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=367,y=193,width=240,height=428)
        self.animate()
    # ======================================================================

    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)


    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass_.delete(0,END)
        self.txt_email.delete(0,END)


    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error ", "All fields are required",parent=self.root2)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from rms_name where email=? and question=? and answer=? ",
                            (self.email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please Select The Correct Security Question / Enter Answer",parent=self.root2)
                else:
                    cur.execute("update rms_name set password=? where email=?",(self.txt_new_pass.get(),self.email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Sucess","Your password has been reset,Please login with new password",parent=self.root2)
                    self.reset()
                    self.root2.destroy()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)



    def forget_password_window(self):
        if self.email.get()=="":
            messagebox.showerror("Error","Please enter the valid email address to reset your password",parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur= con.cursor()
                cur.execute("select * from rms_name where email=? ",(self.email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Please enter the valid email address to reset your password",parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("400x500+730+210")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), bg="white",fg="red").place(x=0, y=10, relwidth=1)

                    # ---------------------------------forget password

                    question = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"),bg="white", fg="gray").place(x=60, y=80)

                    self.cmb_quest = ttk.Combobox(self.root2, font=("times new roman", 13), state='readonly',justify='center')
                    self.cmb_quest['values'] = ("Select", "Your frist Pet Name", "Your Birth Place", "Your best friend Name")
                    self.cmb_quest.place(x=60, y=120, width=250)
                    self.cmb_quest.current(0)

                    answer = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=60, y=160)
                    self.txt_answer = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                    self.txt_answer.place(x=60, y=200, width=250)

                    new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"),bg="white", fg="gray").place(x=60, y=240)
                    self.txt_new_pass = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                    self.txt_new_pass.place(x=60, y=280, width=250)

                    btn_change_password = Button(self.root2, text="Reset Password",command=self.forget_password, bg="green", fg="white",font=("times new roman",15,"bold")).place(x = 90, y = 340)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)


    def register_window(self):
        self.root.destroy()
        os.system("python register.py")

    def login(self):
        if self.email.get()==""or self.password.get()=="":
            messagebox.showerror("Error", "All Feilds are required",parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur= con.cursor()
                cur.execute("select * from rms_name where email=? and password=?",(self.email.get(),self.password.get()),)
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid email or Password\n Try again",parent=self.root)
                else:
                    messagebox.showinfo("Sucess",f"Welcome:{self.email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=login_system(root)
    root.mainloop()