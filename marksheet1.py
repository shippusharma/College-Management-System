import mark_backend

def All(event):  #all is user defined function
    try:
        index=List.curselection()[0]
        global stands #st is global variable
        stands=List.get(index)
        text_roll.delete(0,END)
        text_roll.insert(END,stands[1]) #st[1] is tuple
        text_name.delete(0,END)
        text_name.insert(END,stands[2]) #st[2] is tuple
        text_fathers.delete(0,END)
        text_fathers.insert(END,stands[3])
        text_mothers.delete(0,END)
        text_mothers.insert(END,stands[4])
        text_college.delete(0,END)
        text_college.insert(END,stands[5])
        text_session.delete(0,END)
        text_session.insert(END,stands[6])
        text_branch.delete(0,END)
        text_branch.insert(END,stands[7]) 
        text_sem.delete(0,END)
        text_sem.insert(END,stands[8])
        text_ada.delete(0,END)
        text_ada.insert(END,stands[9])
        text_dbms.delete(0,END)
        text_dbms.insert(END,stands[10])
        text_mp.delete(0,END)
        text_mp.insert(END,stands[11])
        text_unix.delete(0,END)
        text_unix.insert(END,stands[12])
        text_java.delete(0,END)
        text_java.insert(END,stands[13])
        text_toc.delete(0,END)
        text_toc.insert(END,stands[14])
        text_per.delete(0,END)
        text_per.insert(END,stands[15])
        text_result.delete(0,END)
        text_result.insert(END,stands[16])
        text_grade.delete(0,END)
        text_grade.insert(END,stands[17])
        
        
        
    except IndexError:
        pass
       
#connecting functions
def Insert_command():
    mark_backend.insert(rno.get(),name.get(),fname.get(),mname.get(),cname.get(),session.get(),branch.get(),
                        sem.get(),ada.get(),dbms.get(),mp.get(),unix.get(),java.get(),toc.get())
    List.delete(0,END)
    List.insert(END,(rno.get(),name.get(),fname.get(),mname.get(),cname.get(),session.get(),branch.get(),
                        sem.get(),ada.get(),dbms.get(),mp.get(),unix.get(),java.get(),toc.get()))

def View_command():
    List.delete(0,END)
    for row in mark_backend.view():
        List.insert(END,row)

def Delete_command():
    mark_backend.delete(stands[0])
    View_command()

def Update_command():
    '''library_management_backend.delete()
    library_management_backend.save(label_bookid_text.get(),label_booktitle_text.get(),label_bookauthor_text.get(),
                                    label_bookstudent_text.get(),label_cardno_text.get(),label_borrowdate_text.get(),label_returndate_text.get(),label_latefee_text.get())
    List1.delete(0,END)
    List1.save(END,(label_bookid_text.get(),label_booktitle_text.get(),label_bookauthor_text.get(),label_bookstudent_text.get(),
                   label_cardno_text.get(),label_borrowdate_text.get(),label_returndate_text.get(),label_latefee_text.get()))'''
    mark_backend.update(rno.get(),name.get(),fname.get(),mname.get(),cname.get(),session.get(),branch.get(),
                        sem.get(),ada.get(),dbms.get(),mp.get(),unix.get(),java.get(),toc.get())
    View_command()

def reset():
    rno.set(' ')
    name.set(' ')
    fname.set(' ')
    mname.set(' ')
    cname.set(' ')
    session.set(' ')
    branch.set(' ')
    sem.set(' ')
    per.set(' ')
    result.set(' ')
    grade.set(' ')
    ada.set(' ')
    dbms.set(' ')
    mp.set(' ')
    unix.set(' ')
    java.set(' ')
    toc.set(' ')
    return 
'''def calc():

    tot=int(ada.get())+int(dbms.get())+int(mp.get())+int(unix.get())+int(java.get())+int(toc.get())
    per=(tot*1000)/600

    if per>50 :
        res='PASS'
    else:
        res='FAIL'
    

    if perc>=90:
        g='A'
    elif perc>=80:
        g='B'
    elif perc>=70:
        g='C'
    elif perc>=60:
        g='D'
    elif perc>=50:
        g='E'
    else:
        g='F'
    answer.set(per)
    text_per=Entry(root, text= "%s" %(answer) ).grid(row=10,column=1)
    ans1.set(res)    
    text_result=Entry(root, text= "%s" %(ans1) )
    text_result.grid(row=11,column=1)

    ans2.set(g)
    text_grade=Entry(root, text= "%s" %(ans2) )
    text_grade.grid(row=10,column=1)

def perc():
    tot=int(ada.get())+int(dbms.get())+int(mp.get())+int(unix.get())+int(java.get())+int(toc.get())
    percentage=(tot*100)/600
    .set(percentage)
    Entry(root,text= "%s" %(ans) ).grid(row=10,column=1)'''




def exit():
    root.destroy()
from tkinter import*

root=Tk()
root.attributes('-fullscreen',True)
root.config(bg='lightyellow')
root.title('MARKSHEET')

#==============================frame=========================================================
frame=LabelFrame(root,width=700,height=30,relief='ridge',font=('aerial',20,'bold'),bg='lightyellow')
frame.grid(row=1,column=2,pady=10,rowspan=9,padx=50)
frame1=LabelFrame(root,width=700,height=30,relief='ridge',font=('aerial',20,'bold'),bg='lightyellow')
frame1.grid(row=10,column=2,pady=10,rowspan=9,padx=100)



label_title=Label(root,text='MARKSHEET ENTRY',font=('aerial',25,'bold'),width=25,bg='palegoldenrod',borderwidth=5,relief='solid')
label_title.grid(row=0,column=2,pady=15)


label_roll=Label(root,text='Roll No.',font=('aerial',13,'bold'),bg='lightyellow')
label_roll.grid(row=2,column=0,padx=8,pady=8)
rno=StringVar()
text_roll=Entry(root,textvariable=rno)
text_roll.grid(row=2,column=1)
label_name=Label(root,text='Name',font=('aerial',13,'bold'),bg='lightyellow')
label_name.grid(row=3,column=0,padx=8,pady=8)
name=StringVar()
text_name=Entry(root,textvariable=name)
text_name.grid(row=3,column=1)
label_fathers=Label(root,text="Father's Name",font=('aerial',13,'bold'),bg='lightyellow')
label_fathers.grid(row=4,column=0,padx=8,pady=8)
fname=StringVar()
text_fathers=Entry(root,textvariable=fname)
text_fathers.grid(row=4,column=1)
label_mothers=Label(root,text="Mother's Name",font=('aerial',13,'bold'),bg='lightyellow')
label_mothers.grid(row=5,column=0,padx=8,pady=8)
mname=StringVar()
text_mothers=Entry(root,textvariable=mname)
text_mothers.grid(row=5,column=1)
label_college=Label(root,text='College Name',font=('aerial',13,'bold'),bg='lightyellow')
label_college.grid(row=6,column=0,padx=8,pady=8)
cname=StringVar()
text_college=Entry(root,textvariable=cname)
text_college.grid(row=6,column=1)
label_session=Label(root,text='Session',font=('aerial',13,'bold'),bg='lightyellow')
label_session.grid(row=7,column=0,padx=8,pady=8)
session=StringVar()
text_session=Entry(root,textvariable=session)
text_session.grid(row=7,column=1)
label_branch=Label(root,text='Branch',font=('aerial',13,'bold'),bg='lightyellow')
label_branch.grid(row=8,column=0,padx=8,pady=8)
branch=StringVar()
text_branch=Entry(root,textvariable=branch)
text_branch.grid(row=8,column=1)
label_sem=Label(root,text='Semester',font=('aerial',13,'bold'),bg='lightyellow')
label_sem.grid(row=9,column=0,padx=8,pady=8)
sem=StringVar()
text_sem=Entry(root,textvariable=sem)
text_sem.grid(row=9,column=1)

#=========================================Table rows==================================================
label_subject=Label(frame,text='SUBJECT',font=('aerial',14,'bold'),bg='palegoldenrod',width=10)
label_subject.grid(row=0,column=0,padx=15,pady=15)
label_marksobt=Label(frame,text='MARKS OBTAINED',font=('aerial',14,'bold'),bg='palegoldenrod',width=15)
label_marksobt.grid(row=0,column=1,padx=15,pady=15)
label_passing=Label(frame,text='PASSING MARKS',font=('aerial',14,'bold'),bg='palegoldenrod',width=15)
label_passing.grid(row=0,column=2,padx=15,pady=15)
label_total=Label(frame,text='TOTAL',font=('aerial',14,'bold'),bg='palegoldenrod',width=10)
label_total.grid(row=0,column=3,padx=15,pady=15)

#=======================================subject column of table================================================

ada=Label(frame,text='ADA',font=('aerial',13,'bold'),bg='lightyellow')
ada.grid(row=1,column=0,padx=15,pady=15)
dbms=Label(frame,text='DBMS',font=('aerial',13,'bold'),bg='lightyellow')
dbms.grid(row=2,column=0,padx=15,pady=15)
mp=Label(frame,text='MP',font=('aerial',13,'bold'),bg='lightyellow')
mp.grid(row=3,column=0,padx=15,pady=15)
unix=Label(frame,text='UNIX',font=('aerial',13,'bold'),bg='lightyellow')
unix.grid(row=4,column=0,padx=15,pady=15)
java=Label(frame,text='JAVA',font=('aerial',13,'bold'),bg='lightyellow')
java.grid(row=5,column=0,padx=15,pady=15)
toc=Label(frame,text='TOC',font=('aerial',13,'bold'),bg='lightyellow')
toc.grid(row=6,column=0,padx=15,pady=15)


#=====================================Marks obtained Entry of table================================================
ada=StringVar()
text_ada=Entry(frame,textvariable=ada)
text_ada.grid(row=1,column=1)
dbms=StringVar()
text_dbms=Entry(frame,textvariable=dbms)
text_dbms.grid(row=2,column=1)
mp=StringVar()
text_mp=Entry(frame,textvariable=mp)
text_mp.grid(row=3,column=1)
unix=StringVar()
text_unix=Entry(frame,textvariable=unix)
text_unix.grid(row=4,column=1)
java=StringVar()
text_java=Entry(frame,textvariable=java)
text_java.grid(row=5,column=1)
toc=StringVar()
text_toc=Entry(frame,textvariable=toc)
text_toc.grid(row=6,column=1)

#===================================Label of Passing marks=======================================================

label_passingm1=Label(frame,text='28',font=('aerial',13,'bold'),bg='lightyellow')
label_passingm1.grid(row=1,column=2)
label_passingm2=Label(frame,text='28',font=('aerial',13,'bold'),bg='lightyellow')
label_passingm2.grid(row=2,column=2)
label_passingm3=Label(frame,text='28',font=('aerial',13,'bold'),bg='lightyellow')
label_passingm3.grid(row=3,column=2)
label_passingm4=Label(frame,text='28',font=('aerial',13,'bold'),bg='lightyellow')
label_passingm4.grid(row=4,column=2)
label_passingm5=Label(frame,text='28',font=('aerial',13,'bold'),bg='lightyellow')
label_passingm5.grid(row=5,column=2)
label_passingm6=Label(frame,text='28',font=('aerial',13,'bold'),bg='lightyellow')
label_passingm6.grid(row=6,column=2)

#=================================Label of total===============================================================

label_total1=Label(frame,text='80',font=('aerial',13,'bold'),bg='lightyellow')
label_total1.grid(row=1,column=3)
label_total2=Label(frame,text='80',font=('aerial',13,'bold'),bg='lightyellow')
label_total2.grid(row=2,column=3)
label_total3=Label(frame,text='80',font=('aerial',13,'bold'),bg='lightyellow')
label_total3.grid(row=3,column=3)
label_total4=Label(frame,text='80',font=('aerial',13,'bold'),bg='lightyellow')
label_total4.grid(row=4,column=3)
label_total5=Label(frame,text='80',font=('aerial',13,'bold'),bg='lightyellow')
label_total5.grid(row=5,column=3)
label_total6=Label(frame,text='80',font=('aerial',13,'bold'),bg='lightyellow')
label_total6.grid(row=6,column=3)

#=================================Buttons=======================================================================

save=Button(frame,text='SAVE',font=('aerial',14,'bold'),bg='palegoldenrod',width=13,command=Insert_command)
save.grid(row=1,column=4,padx=15,pady=10)          
reset=Button(frame,text='RESET',font=('aerial',14,'bold'),bg='palegoldenrod',width=13,command=reset)
reset.grid(row=2,column=4,padx=40,pady=10)
update=Button(frame,text='UPDATE',font=('aerial',14,'bold'),bg='palegoldenrod',width=13,command=Update_command)
update.grid(row=3,column=4,padx=15,pady=10)
calc=Button(root,text='CALCULATE',font=('aerial',14,'bold'),bg='palegoldenrod',width=13)
calc.grid(row=10,column=0,columnspan=2,padx=15,pady=10)
view=Button(frame,text='VIEW',font=('aerial',14,'bold'),bg='palegoldenrod',width=13,command=View_command)
view.grid(row=4,column=4,padx=15,pady=10)
delete=Button(frame,text='DELETE',font=('aerial',14,'bold'),bg='palegoldenrod',width=13,command=Delete_command)
delete.grid(row=5,column=4,padx=15,pady=10)
btn_exit=Button(frame,text='EXIT',font=('aerial',14,'bold'),bg='palegoldenrod',width=13,command=exit)
btn_exit.grid(row=6,column=4,padx=15,pady=10)
                
#================================Percentage and result-label and entry===========================================

label_per=Label(root,text='PERCENTAGE',font=('aerial',13,'bold'),bg='palegoldenrod',width=13)
label_per.grid(row=11,column=0,padx=15,pady=15)
per=StringVar()
text_per=Entry(root)
text_per.grid(row=11,column=1)
label_result=Label(root,text='RESULT',font=('aerial',13,'bold'),bg='palegoldenrod',width=13)
label_result.grid(row=12,column=0,padx=15,pady=15)
result=StringVar()
text_result=Entry(root)
text_result.grid(row=12,column=1)
label_grade=Label(root,text='GRADE',font=('aerial',13,'bold'),bg='palegoldenrod',width=13)
label_grade.grid(row=13,column=0,padx=15,pady=15)
grade=StringVar()
text_grade=Entry(root)
text_grade.grid(row=13,column=1)
#===========================listbox========================================================
List=Listbox(frame1,width=150,height=10,relief='solid',borderwidth=3)
List.grid(row=10,column=2,rowspan=7,columnspan=2,padx=20,pady=20) #list padding colspan and rowspan
List.bind("<<ListboxSelect>>",All)

sb=Scrollbar(frame1)
sb.grid(row=10,column=4,rowspan=7,padx=10)
List.config(yscrollcommand=sb.set)
sb.config(command=List.yview)




root.mainloop()



