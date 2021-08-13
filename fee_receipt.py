import fee_backend

def All(event):  #all is user defined function
    try:
        index=List1.curselection()[0]
        global stan #st is global variable
        stan=List1.get(index)
        text_receiptno.delete(0,END)
        text_receiptno.insert(END,stan[1]) #st[1] is tuple
        text_studentname.delete(0,END)
        text_studentname.insert(END,stan[2]) #st[2] is tuple
        text_admissionno.delete(0,END)
        text_admissionno.insert(END,stan[3])
        text_date.delete(0,END)
        text_date.insert(END,stan[4])
        text_branch.delete(0,END)
        text_branch.insert(END,stan[5]) 
        text_sem.delete(0,END)
        text_sem.insert(END,stan[6])
        text_totamt.delete(0,END)
        text_totamt.insert(END,stan[7])
        text_paidamt.delete(0,END)
        text_paidamt.insert(END,stan[8])
        text_balance.delete(0,END)
        text_balance.insert(END,stan[9])
    except IndexError:
        pass
       
#connecting functions
def Insert_command():
    fee_backend.insert(rno.get(),sname.get(),admno.get(),dates.get(),branch.get(),sem.get(),totamt.get(),paidamt.get(),balance.get())
    List1.delete(0,END)
    List1.insert(END,(rno.get(),sname.get(),admno.get(),dates.get(),branch.get(),sem.get(),totamt.get(),paidamt.get(),balance.get()))

def View_command():
    List1.delete(0,END)
    for row in fee_backend.view():
        List1.insert(END,row)

def Delete_command():
    fee_backend.delete(stan[0])
    View_command()

def Update_command():
    '''fee_backend.delete(stan[0])
    fee_backend.insert(rno.get(),sname.get(),admno.get(),dates.get(),branch.get(),sem.get(),totamt.get(),paidamt.get(),balance.get())
    List1.delete(0,END)
    List1.insert(END,(rno.get(),sname.get(),admno.get(),dates.get(),branch.get(),sem.get(),totamt.get(),paidamt.get(),balance.get()))'''
    fee_backend.update(rno.get(),sname.get(),admno.get(),dates.get(),branch.get(),sem.get(),totamt.get(),paidamt.get(),balance.get())
    View_command()


def exit():
    root.destroy()
    
from tkinter import*

root=Tk()
root.attributes('-fullscreen',True)
root.config(bg='lightyellow')
root.title('FEE REPORT')
#==========================================Frame================================================================

frame3=LabelFrame(root,width=700,height=30,relief='ridge',font=('aerial',20,'bold'),bg='lightyellow')
frame3.grid(row=1,column=2,pady=100,rowspan=9,padx=50)
frame4=LabelFrame(frame3,width=700,height=30,relief='ridge',font=('aerial',20,'bold'),bg='lightyellow')
frame4.grid(row=9,column=0,pady=15,rowspan=3,padx=50,columnspan=2)


#=======================================================Labels==================================================
label_database1=Label(root,text='DATABASE',font=('aerial',25,'bold'),bg='palegoldenrod',width=15)
label_database1.grid(row=1,column=2,padx=2,pady=15)

label_feereceipt=Label(root,text='FEE REPORT',font=('aerial',30,'bold'),bg='palegoldenrod',width=30,relief='solid',borderwidth=5)
label_feereceipt.grid(row=0,column=2,padx=50,pady=15)

label_receiptno=Label(root,text='Receipt No.',font=('aerial',15,'bold'),bg='palegoldenrod',width=13)
label_receiptno.grid(row=1,column=0,padx=30,pady=15)
rno=StringVar()
text_receiptno=Entry(root,textvariable=rno)
text_receiptno.grid(row=1,column=1,padx=30)
label_studentname=Label(root,text='Student Name',font=('aerial',15,'bold'),bg='palegoldenrod',width=13)
label_studentname.grid(row=2,column=0,padx=30,pady=15)
sname=StringVar()
text_studentname=Entry(root,textvariable=sname)
text_studentname.grid(row=2,column=1,padx=30)
label_admissionno=Label(root,text='Admission No.',font=('aerial',15,'bold'),bg='palegoldenrod',width=13)
label_admissionno.grid(row=3,column=0,padx=30,pady=15)
admno=StringVar()
text_admissionno=Entry(root,textvariable=admno)
text_admissionno.grid(row=3,column=1,padx=30)
label_date=Label(root,text='Date',font=('aerial',15,'bold'),bg='palegoldenrod',width=13)
label_date.grid(row=4,column=0,padx=30,pady=15)
dates=StringVar()
text_date=Entry(root,textvariable=dates)
text_date.grid(row=4,column=1,padx=30)
label_branch=Label(root,text='Branch',font=('aerial',15,'bold'),bg='palegoldenrod',width=13)
label_branch.grid(row=5,column=0,padx=30,pady=15)
branch=StringVar()
text_branch=Entry(root,textvariable=branch)
text_branch.grid(row=5,column=1,padx=30)
label_sem=Label(root,text='Semester',font=('aerial',15,'bold'),bg='palegoldenrod',width=13)
label_sem.grid(row=6,column=0,padx=30,pady=15)
sem=StringVar()
text_sem=Entry(root,textvariable=sem)
text_sem.grid(row=6,column=1,padx=30)
label_totamt=Label(root,text='Total Amount',font=('aerial',15,'bold'),bg='palegoldenrod',width=13)
label_totamt.grid(row=7,column=0,padx=30,pady=15)
totamt=StringVar()
text_totamt=Entry(root,textvariable=totamt)
text_totamt.grid(row=7,column=1,padx=30)
label_paidamt=Label(root,text='Paid Amount',font=('aerial',15,'bold'),bg='palegoldenrod',width=13)
label_paidamt.grid(row=8,column=0,padx=30,pady=15)
paidamt=StringVar()
text_paidamt=Entry(root,textvariable=paidamt)
text_paidamt.grid(row=8,column=1,padx=30)
label_balance=Label(root,text='Balance',font=('aerial',15,'bold'),bg='palegoldenrod',width=13)
label_balance.grid(row=9,column=0,padx=30,pady=15)
balance=StringVar()
text_balance=Entry(root,textvariable=balance)
text_balance.grid(row=9,column=1,padx=30)

#==============================================Buttons===========================================

btn_save1=Button(frame4,text='SAVE',font=('aerial',15,'bold'),bg='palegoldenrod',width=9,relief='sunken',borderwidth=4,command=Insert_command)
btn_save1.grid(row=9,column=1,padx=10,pady=8)
btn_view1=Button(frame4,text='VIEW',font=('aerial',15,'bold'),bg='palegoldenrod',width=9,relief='sunken',borderwidth=4,command=View_command)
btn_view1.grid(row=9,column=2,padx=10,pady=8)
btn_update1=Button(frame4,text='UPDATE',font=('aerial',15,'bold'),bg='palegoldenrod',width=9,relief='sunken',borderwidth=4,command=Update_command)
btn_update1.grid(row=9,column=3,padx=10,pady=8)
btn_delete1=Button(frame4,text='DELETE',font=('aerial',15,'bold'),bg='palegoldenrod',width=9,relief='sunken',borderwidth=4,command=Delete_command)
btn_delete1.grid(row=9,column=4,padx=10,pady=8)
btn_exit=Button(frame4,text='EXIT',font=('aerial',15,'bold'),bg='palegoldenrod',width=9,relief='sunken',borderwidth=4,command=exit)
btn_exit.grid(row=9,column=5,padx=10,pady=8)

#================================================Lists===========================================

List1=Listbox(frame3,width=100,height=10,relief='solid',borderwidth=3)
List1.grid(row=1,column=0,rowspan=7,columnspan=2,padx=1,pady=50) #list padding colspan and rowspan
List1.bind("<<ListboxSelect>>",All)

sb1=Scrollbar(frame3)
sb1.grid(row=2,column=2,rowspan=7,padx=10)
List1.config(yscrollcommand=sb1.set)
sb1.config(command=List1.yview)









root.mainloop()
