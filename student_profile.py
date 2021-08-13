import stud_backend

def All(event):  #all is user defined function
    try:
        index=List2.curselection()[0]
        global stands #st is global variable
        stands=List2.get(index)
        text_name1.delete(0,END)
        text_name1.insert(END,stands[1]) #st[1] is tuple
        text_father.delete(0,END)
        text_father.insert(END,stands[2]) #st[2] is tuple
        text_mother.delete(0,END)
        text_mother.insert(END,stands[3])
        text_address.delete(0,END)
        text_address.insert(END,stands[4])
        text_mobno.delete(0,END)
        text_mobno.insert(END,stands[5])
        text_email.delete(0,END)
        text_email.insert(END,stands[6])
        text_sem2.delete(0,END)
        text_sem2.insert(END,stands[7]) 
        text_branch2.delete(0,END)
        text_branch2.insert(END,stands[8])
    except IndexError:
        pass
       
#connecting functions
def insert_command():
    stud_backend.insert(name.get(),fname.get(),mname.get(),address.get(),mob.get(),email.get(),sem.get(),branch.get())
    List2.delete(0,END)
    List2.insert(END,(name.get(),fname.get(),mname.get(),address.get(),mob.get(),email.get(),sem.get(),branch.get()))

def View_command():
    List2.delete(0,END)
    for row in stud_backend.view():
        List2.insert(END,row)

def Delete_command():
    stud_backend.delete(stands[0])
    View_command()

def Update_command():
    '''library_management_backend.delete()
    library_management_backend.save(label_bookid_text.get(),label_booktitle_text.get(),label_bookauthor_text.get(),
                                    label_bookstudent_text.get(),label_cardno_text.get(),label_borrowdate_text.get(),label_returndate_text.get(),label_latefee_text.get())
    List1.delete(0,END)
    List1.save(END,(label_bookid_text.get(),label_booktitle_text.get(),label_bookauthor_text.get(),label_bookstudent_text.get(),
                   label_cardno_text.get(),label_borrowdate_text.get(),label_returndate_text.get(),label_latefee_text.get()))'''
    stud_backend.update(name.get(),fname.get(),mname.get(),address.get(),mob.get(),email.get(),sem.get(),branch.get())
    View_command()

def reset():
    name.set(' ')
    fname.set(' ')
    mname.set(' ')
    address.set(' ')
    mob.set(' ')
    email.set(' ')
    sem.set(' ')
    branch.set(' ')
    return 
    
    
def exit():
    root.destroy()


from tkinter import*

root=Tk()
root.attributes('-fullscreen',True)
root.config(bg='lightyellow')
root.title('STUDENT PROFILE')


#=============================================Frames=======================================================================
frame1=LabelFrame(root,width=1500,height=30,relief='ridge',font=('aerial',20,'bold'),bg='lightyellow')
frame1.grid(row=1,column=0,pady=15)
frame2=LabelFrame(root,width=1500,height=30,relief='ridge',font=('aerial',20,'bold'),bg='lightyellow')
frame2.grid(row=9,column=0,pady=15)

#============================================Labels=======================================================================

label_studinfo=Label(root,text='STUDENT PROFILE',font=('aerial',30,'bold'),bg='palegoldenrod',width=30,relief='solid',borderwidth=5)
label_studinfo.grid(row=0,column=0,padx=410,pady=30)
label_database=Label(frame1,text='DATABASE',font=('aerial',20,'bold'),bg='palegoldenrod',width=13,relief='solid')
label_database.grid(row=2,column=2,padx=200,pady=15)

#============================================Labels in frame===============================================================
label_name1=Label(frame1,text='Name',font=('aerial',14,'bold'),bg='palegoldenrod',width=13)
label_name1.grid(row=1,column=0,padx=30,pady=15)
name=StringVar()
text_name1=Entry(frame1,textvariable=name)
text_name1.grid(row=1,column=1,padx=30)
label_father=Label(frame1,text="Father's Name",font=('aerial',14,'bold'),bg='palegoldenrod',width=13)
label_father.grid(row=2,column=0,padx=30,pady=15)
fname=StringVar()
text_father=Entry(frame1,textvariable=fname)
text_father.grid(row=2,column=1)
label_mother=Label(frame1,text="Mother's Name",font=('aerial',14,'bold'),bg='palegoldenrod',width=13)
label_mother.grid(row=3,column=0,padx=30,pady=15)
mname=StringVar()
text_mother=Entry(frame1,textvariable=mname)
text_mother.grid(row=3,column=1)
label_address=Label(frame1,text="Address",font=('aerial',14,'bold'),bg='palegoldenrod',width=13)
label_address.grid(row=4,column=0,padx=30,pady=15)
address=StringVar()
text_address=Entry(frame1,textvariable=address)
text_address.grid(row=4,column=1)
label_mobno=Label(frame1,text="Mobile Number",font=('aerial',14,'bold'),bg='palegoldenrod',width=13)
label_mobno.grid(row=5,column=0,padx=30,pady=15)
mob=StringVar()
text_mobno=Entry(frame1,textvariable=mob)
text_mobno.grid(row=5,column=1)
label_email=Label(frame1,text="Email ID",font=('aerial',14,'bold'),bg='palegoldenrod',width=13)
label_email.grid(row=6,column=0,padx=30,pady=15)
email=StringVar()
text_email=Entry(frame1,textvariable=email)
text_email.grid(row=6,column=1)
label_sem2=Label(frame1,text="Semester",font=('aerial',14,'bold'),bg='palegoldenrod',width=13)
label_sem2.grid(row=7,column=0,padx=30,pady=15)
sem=StringVar()
text_sem2=Entry(frame1,textvariable=sem)
text_sem2.grid(row=7,column=1)
label_branch2=Label(frame1,text="Branch",font=('aerial',14,'bold'),bg='palegoldenrod',width=13)
label_branch2.grid(row=8,column=0,padx=30,pady=15)
branch=StringVar()
text_branch2=Entry(frame1,textvariable=branch)
text_branch2.grid(row=8,column=1)

#========================================buttons======================================================

btn_save2=Button(frame2,text='SAVE',font=('aerial',17,'bold'),relief='raised',borderwidth=4,bg='palegoldenrod',width=9,command=insert_command)
btn_save2.grid(row=9,column=1,padx=20,pady=15)
btn_reset=Button(frame2,text='RESET',font=('aerial',17,'bold'),relief='raised',borderwidth=4,bg='palegoldenrod',width=9,command=reset)
btn_reset.grid(row=9,column=2,padx=20,pady=15)
btn_update2=Button(frame2,text='UPDATE',font=('aerial',17,'bold'),relief='raised',borderwidth=4,bg='palegoldenrod',width=9,command=Update_command)
btn_update2.grid(row=9,column=3,padx=20,pady=15)
btn_delete2=Button(frame2,text='DELETE',font=('aerial',17,'bold'),relief='raised',borderwidth=4,bg='palegoldenrod',width=9,command=Delete_command)
btn_delete2.grid(row=9,column=4,padx=20,pady=15)
btn_search=Button(frame2,text='VIEW',font=('aerial',17,'bold'),relief='raised',borderwidth=4,bg='palegoldenrod',width=9,command=View_command)
btn_search.grid(row=9,column=5,padx=20,pady=15)
btn_exit1=Button(frame2,text='EXIT',font=('aerial',17,'bold'),relief='raised',borderwidth=4,bg='palegoldenrod',width=9,command=exit)
btn_exit1.grid(row=9,column=6,padx=20,pady=15)

#=================================listbox=============================================================

List2=Listbox(frame1,width=90,relief='solid',borderwidth=3)
List2.grid(row=1,column=2,rowspan=9,columnspan=2) #list padding colspan and rowspan
List2.bind("<<ListboxSelect>>",All)

sb2=Scrollbar(frame1)
sb2.grid(row=1,column=4,rowspan=9,padx=20)
List2.config(yscrollcommand=sb2.set)
sb2.config(command=List2.yview)




root.mainloop()




















































root.mainloop()
