import sqlite3
def connect():
    con=sqlite3.connect('student.db') #con and cur are variables and book.db means book->name of library and db->database
    cur=con.cursor() #cursor connects frontend to backend
    cur.execute('CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,name TEXT ,fname TEXT,mname TEXT,address TEXT,mob INTEGER,email TEXT,sem INTEGER,branch TEXT)')
    con.commit()  #save
    con.close

def insert(name='',fname='',mname='',address='',mob='',email='',sem='',branch=''):
    con=sqlite3.connect('student.db')
    cur=con.cursor()
    cur.execute('INSERT INTO student VALUES(NULL,?,?,?,?,?,?,?,?)',(name,fname,mname,address,mob,email,sem,branch))  #NULL means initialization for primary key
    con.commit()
    con.close()

def view():
    con=sqlite3.connect('student.db')
    cur=con.cursor()
    cur.execute('SELECT * FROM student')  # '*' means all
    rows=cur.fetchall()
    return rows
    
def delete(i=" "):
    con=sqlite3.connect('student.db')
    cur=con.cursor()
    cur.execute('DELETE FROM student WHERE (id=?)',(i,))
    con.commit()
    con.close()

def update(name='',fname='',mname='',address='',mob='',email='',sem='',branch=''):
    con=sqlite3.connect('student.db')
    cur=con.cursor()
    
    cur.execute('UPDATE student SET name=?,fname=?,mname=?,address=?,mob=?,sem=?,branch=? WHERE email=? ',
                (name,fname,mname,address,mob,sem,branch,email))

    con.commit()
    con.close()


    
    
    

connect()
"""insert('ABC123','C++','Rishita Rathore','2019')
print(view())"""
