from tkinter import *
import tkinter.messagebox                               # for messagebox
from tkinter import StringVar                           # for stringvariable 
from tkinter import ttk                                 # for combobox
import random                                           # for reference
import time
import datetime
import os

def main():
    root=Tk()
    root.attributes('-fullscreen',True)
    app=window_1(root)
    
class window_1:
    def __init__(self,master):
        self.master=master
        self.master.title("LOGIN")
        self.master.wm_state('zoomed')
        self.master.config(bg='lightyellow')

        self.username=StringVar()  # x=StrVar() holds a string; default value is " "
        self.password=StringVar()

        self.label_title=Label(master,text='LOGIN FORM',font=('aerial',40,'bold'),bg='palegoldenrod',width=13,relief='solid',borderwidth=5)
        self.label_title.grid(row=0,column=0,padx=450,pady=40)
        
        self.log_in_frame1=LabelFrame(master,width=1000,height=200,bg='palegoldenrod',relief='solid',font=('aerial',20,'bold'))
        self.log_in_frame1.grid(row=1,column=0,pady=50,padx=500)
        
        self.log_in_frame2=LabelFrame(master,width=600,height=70,bg='palegoldenrod',relief='solid',font=('aerial',20,'bold'))
        self.log_in_frame2.grid(row=2,column=0)


#=================================labels and entries=======================================================================
        self.label_username=Label(self.log_in_frame1,text='Username',font=('aerial',20,'bold'),bg='lightyellow',width=14)
        self.label_username.grid(row=1,column=1,padx=60,pady=20)
        self.text_username=Entry(self.log_in_frame1,textvariable=self.username,width=30)
        self.text_username.grid(row=1,column=2,padx=60,pady=20)
        self.label_password=Label(self.log_in_frame1,text='Password',font=('aerial',20,'bold'),bg='lightyellow',width=14)
        self.label_password.grid(row=2,column=1,padx=60,pady=20)
        self.text_password=Entry(self.log_in_frame1,textvariable=self.password,show='*',width=30)
        self.text_password.grid(row=2,column=2,padx=60,pady=20)

#========================================Buttons===========================================================================
        self.btnlogin=Button(self.log_in_frame2,text='Login',width=10,font=('aerial',17,'bold'),command=self.Login,bg='lightyellow',relief='raised',borderwidth=3)
        self.btnlogin.grid(row=3,column=0,padx=10,pady=20)

        self.btnreset=Button(self.log_in_frame2,text='Reset',width=10,font=('aerial',17,'bold'),command=self.Reset,bg='lightyellow',relief='raised',borderwidth=3)
        self.btnreset.grid(row=3,column=1,padx=10,pady=20)

        self.btnexit=Button(self.log_in_frame2,text='Exit',width=10,font=('aerial',17,'bold'),command=self.Exit,bg='lightyellow',relief='raised',borderwidth=3)
        self.btnexit.grid(row=3,column=2,padx=10,pady=20)

#====================================coding for login=================================================================================
    def Login(self):
        u = (self.username.get())
        p = (self.password.get())

        if u == str('sibusharma') and p == str("12345"):
            filename='menu.py'
            os.system(filename)
            os.system('notepad'+filename)
        else:
            tkinter.messagebox.askyesno("Login","Error : Wrong Password")
            self.username.set("")
            self.password.set("")
            #self.text_username.focus()

        
#======================================================Code for Reset Button==================================================================
    def Reset(self):
         self.username.set("")
         self.password.set("")
         #self.text_username.focus()

#======================================================Code for Exit Button==================================================================

    def Exit(self):
        self.exit = tkinter.messagebox.askokcancel("Login System", "Confirm if you want to Exit")
        if self.exit > 0:
            self.master.destroy()
            return

        
#if __name__ == '__main__':                                    # https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
main()                                              

