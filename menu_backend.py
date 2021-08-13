
#connecting frontend and backend
import sqlite3
def connect():
    con=sqlite3.connect() #con and cur are variables and book.db means book->name of library and db->database
    cur=con.cursor() #cursor connects frontend to backend
    cur.execute()
    con.commit()  #save
    con.close

def stud_profile():
    import student_profile
    student_profile.student_profile()
    
