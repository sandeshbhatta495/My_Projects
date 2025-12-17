from tkinter import*
from PIL import Image,ImageTk #=====pip  install pillow
from tkinter import ttk,messagebox
import sqlite3
import os
# from login import login_system
# import pymysql

class registerClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Managment System")
        self.root.geometry("1200x800+80+50")
        self.root.config(bg="white")
        self.root.focus_force()
        # ===title====
        # title = Label(self.root, text="Register Here",font=("goudy old style", 20, "bold"), bg="orange", fg="black").place(x=10, y=15,width=1180,height=35)

    # ==========BG Image==========
        self.bg=ImageTk.PhotoImage(file="images/b2.jpg")
        bg=Label(self.root,image=self.bg).place(x=1,y=0,relwidth=1,relheight=1)


    # =========Animation Images============
        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2=ImageTk.PhotoImage(file="images/im2.png")
        self.im3=ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=245,y=100,width=240,height=500)
        self.animate()

    # ============Register Frame========================

        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        # ====================================Row1===
        f_name=Label(frame1,text="Frist Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_f_name=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_f_name.place(x=50,y=130,width=250)

        f_l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_l_name=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_l_name.place(x=370,y=130,width=250)
    # ====================================Row2===
        contact=Label(frame1,text="Contact Number",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)

    # ==================================Row3=====
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)

        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify='center')
        self.cmb_quest['values']=("Select","Your frist Pet Name","Your Birth Place","Your best friend Name")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)


        # ====================================Row4===

        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=50, y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)

        c_password = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370,y=310)
        self.txt_c_password = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_c_password.place(x=370, y=340, width=250)


    # ===============Terms-===============
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms And Conditions",bg='white',variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",12)).place(x=30,y=380)

        self.btn_img=ImageTk.PhotoImage(file="images/register.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor='hand2',command=self.register_data).place(x=50,y=440)

        btn_login=Button(self.root,text="Sign In",command=self.login_window,bg="gray",font=("times new roman",20),bd=0,cursor='hand2').place(x=290,y=543,width=200,height=34)


    # ======================================================================

    # def open_login_window(self):
    #     try:
    #         self.root.withdraw()  # Hide the registration window
    #         self.root.master.deiconify()  # Restore the main login window
    #     except Exception as ex:
    #         messagebox.showerror("Error", f"Error: {str(ex)}")


    def login_window(self):
        self.root.destroy()
        os.system("python login.py")

    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)

    def clear(self):
        self.txt_f_name.delete(0,END)
        self.txt_l_name.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_c_password.delete(0,END)
        self.txt_answer.delete(0,END)
        self.cmb_quest.current(0)

    def register_data(self):
        if self.txt_f_name.get()==""or self.txt_email.get()=="" or  self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_c_password.get()==""or self.txt_contact.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_password.get()!=self.txt_c_password.get():
            messagebox.showerror("Error","Password and Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0 :
            messagebox.showerror("Error","Please Agree Our Terms & Conditions",parent=self.root)

        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from rms_name where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                # print(row)
                if row!=None:
                    messagebox.showerror("Error", "User already Exists,Please try with another email ", parent=self.root)
                else:
                    cur.execute("insert into rms_name(f_name,l_name,contact,email,question,answer,password) values (?,?,?,?,?,?,?)",
                            (
                              self.txt_f_name.get(),
                              self.txt_l_name.get(),
                              self.txt_contact.get(),
                              self.txt_email.get(),
                              self.cmb_quest.get(),
                              self.txt_answer.get(),
                              self.txt_password.get()
                            ))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Register Successful ",parent=self.root)
                self.clear()
                self.login_window()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)} ",parent=self.root)




if __name__=="__main__":
    root=Tk()
    obj=registerClass(root)
    root.mainloop()