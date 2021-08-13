def connect():
    con=sqlite3.connect('fee.db') #con and cur are variables and book.db means book->name of library and db->database
    cur=con.cursor() #cursor connects frontend to backend
    cur.execute('CREATE TABLE IF NOT EXISTS fee(id INTEGER PRIMARY KEY,rno ,sname TEXT,admno INTEGER,date INTEGER, \
                branch TEXT,sem INTEGER, totamt INTEGER,paidamt INTEGER,balance INTEGER)')
    con.commit()  #save
    con.close

def insert(rno='',sname='',admno='',date='',branch='',sem='',totamt='',paidamt='',balance=''):
    con=sqlite3.connect('fee.db')
    cur=con.cursor()
    cur.execute('INSERT INTO fee VALUES(NULL,?,?,?,?,?,?,?,?,?)',(rno,sname,
    admno,date,branch,sem,totamt,paidamt,balance))  #NULL means initialization for primary key
    con.commit()
    con.close()

def view():
    con=sqlite3.connect('fee.db')
    cur=con.cursor()
    cur.execute('SELECT * FROM fee')  # '*' means all
    rows=cur.fetchall()
    return rows
    
def delete(i=" "):
    con=sqlite3.connect('fee.db')
    cur=con.cursor()
    cur.execute('DELETE FROM fee WHERE (id=?)',(i,))
    con.commit()
    con.close()

def update(rno=' ',sname=' ',admno=' ',date=' ',branch=' ',sem=' ',totamt=' ',paidamt=' ',balance=' '):
    con=sqlite3.connect('fee.db')
    cur=con.cursor()
    
    cur.execute('UPDATE fee SET sname=?,admno=?,date=?,branch=?,sem=?,totamt=?,paidamt=?,balance=? WHERE rno=?',
                (sname,admno,date,branch,sem,totamt,paidamt,balance,rno,))

    con.commit()
    con.close()
    

   
    
    
import sqlite3
connect()
"""insert('ABC123','C++','Rishita Rathore','2019')
print(view())"""
