import os
def stud_profile():
    filename='student_profile.py'
    os.system(filename)
    os.system('notepad'+filename)

def fee_receipt():
    filename='fee_receipt.py'
    os.system(filename)
    os.system('notepad'+filename)

def marksheet():
    filename='marksheet1.py'
    os.system(filename)
    os.system('notepad'+filename)

def library():
    filename='library_management.py'
    os.system(filename)
    os.system('notepad'+filename)

def exit():
    root.destroy()

from tkinter import *


root=Tk()
root.config(bg='lightyellow')
root.attributes('-fullscreen',True)
root.title('MENU')

#======================================Label=========================================================================================
label_title=Label(root,text='MENU',font=('aerial',40,'bold'),width=15,bg='palegoldenrod',relief='solid',borderwidth=5)
label_title.grid(row=0,column=0,padx=500,pady=15)

#======================================Button========================================================================================

btn_studentprofile=Button(root,text='Student Profile',font=('aerial',20,'bold'),width=25,bg='palegoldenrod',relief='raised',borderwidth=6,command=stud_profile)
btn_studentprofile.grid(row=1,column=0,padx=500,pady=20)

btn_feereport=Button(root,text='Fee Report',font=('aerial',20,'bold'),width=25,bg='palegoldenrod',relief='raised',borderwidth=6,command=fee_receipt)
btn_feereport.grid(row=2,column=0,padx=500,pady=20)

btn_marksheet=Button(root,text='Marksheet',font=('aerial',20,'bold'),width=25,bg='palegoldenrod',relief='raised',borderwidth=6,command=marksheet)
btn_marksheet.grid(row=4,column=0,padx=500,pady=20)
            
btn_librarymanagement=Button(root,text='Library Management',font=('aerial',20,'bold'),width=25,bg='palegoldenrod',relief='raised',borderwidth=6,command=library)
btn_librarymanagement.grid(row=5,column=0,padx=500,pady=20)
         
btn_exit=Button(root,text='Exit',font=('aerial',20,'bold'),width=25,bg='palegoldenrod',relief='raised',borderwidth=6,command=exit)
btn_exit.grid(row=6,column=0,padx=500,pady=20)                     
                     
                     
            

root.mainloop()
