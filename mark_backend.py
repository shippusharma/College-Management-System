import sqlite3
def connect():
    con=sqlite3.connect('marksheet.db') #con and cur are variables and book.db means book->name of library and db->database
    cur=con.cursor() #cursor connects frontend to backend
    cur.execute('CREATE TABLE IF NOT EXISTS marksheet(id INTEGER PRIMARY KEY,rno INTEGER ,name TEXT,fname TEXT,mname TEXT,cname TEXT, \
           session INTEGER,branch TEXT,sem INTEGER,per INTEGER,result TEXT,grade TEXT,ada INTEGER,dbms INTEGER,mp INTEGER, \
           unix INTEGER,java INTEGER,toc INTEGER)')
    con.commit()  #save
    con.close

def insert(rno='',name='',fname='',mname='',cname='',session='',branch='',sem='',per='',result='',grade='',ada='',dbms=''
           ,mp='',unix='',java='',toc=''):
    con=sqlite3.connect('marksheet.db')
    cur=con.cursor()
    cur.execute('INSERT INTO marksheet VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(rno,name,fname,mname,cname,session,branch,sem,
                                                                      per,result,grade,ada,dbms,mp,unix,java,toc))  #NULL means initialization for primary key
    con.commit()
    con.close()

def view():
    con=sqlite3.connect('marksheet.db')
    cur=con.cursor()
    cur.execute('SELECT * FROM marksheet')  # '*' means all
    rows=cur.fetchall()#fetch means Read Values
    return rows
    
def delete(i=" "):
    con=sqlite3.connect('marksheet.db')
    cur=con.cursor()
    cur.execute('DELETE FROM marksheet WHERE (id=?)',(i,))
    con.commit()
    con.close()

def update(rno='',name='',fname='',mname='',cname='',session='',branch='',sem='',ada='',dbms=''
           ,mp='',unix='',java='',toc=''):
    con=sqlite3.connect('marksheet.db')
    cur=con.cursor()
    
    cur.execute('UPDATE marksheet SET name=?,fname=?,mname=?,cname=?,session=?,branch=?,sem=?,ada=?,dbms=? \
           ,mp=?,unix=?,java=?,toc=? WHERE rno=? ',
                (name,fname,mname,cname,session,branch,sem,ada,dbms
           ,mp,unix,java,toc,rno))

    con.commit()
    con.close()    
    

connect()
"""insert('ABC123','C++','shippu sharma','2019')
print(view())"""
