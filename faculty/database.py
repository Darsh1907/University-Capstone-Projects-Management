import mysql.connector

#set your mysql password
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql@dbms@123",
    database="capstones"
)

c = mydb.cursor()

def your_students_db(email):
    c.execute("SELECT * FROM student where project_id IN (SELECT project_id FROM team WHERE faculty_id=(SELECT ID from faculty where email_id=%s))", (email,))
    data = c.fetchall()
    return data

def view_teams_db(email_id):
    c.execute('SELECT t.project_id, t.project_name, t.project_desc, d.`Domain Name` FROM team as t, domain as d WHERE t.panel_id=(SELECT panel_id FROM faculty where email_id=%s) AND t.domain_id=d.DomainID', (email_id,))
    data = c.fetchall()
    return data

def view_panel(email):
    c.execute('SELECT ID, name, email_id, domain_id from faculty WHERE panel_id=(SELECT panel_id FROM faculty WHERE email_id=%s);', (email,))
    data = c.fetchall()
    return data

def get_panel_head(email):
    c.execute('SELECT head_id from panel where panel_id=(SELECT panel_id FROM faculty WHERE email_id=%s);', (email,))
    data = c.fetchall()[0][0]
    return data

def see_eval(student_srn, student_sem):
    c.execute('INSERT IGNORE INTO evaluation (`Semester`, `SRN`, `Faculty_ID`) VALUES ((SELECT Sem from student where SRN=%s),%s, (SELECT faculty_id from team where project_id=(SELECT project_id from student where SRN=%s)));', (student_srn, student_srn, student_srn))
    mydb.commit()
    c.execute('SELECT * FROM evaluation where SRN=%s AND Semester=%s', (student_srn, student_sem))
    data=c.fetchall()
    return data

def eval_db(isa1, isa2, isa3, esa, student_srn, student_sem):
    c.execute('INSERT IGNORE INTO evaluation (`Semester`, `SRN`, `Faculty_ID`) VALUES ((SELECT Sem from student where SRN=%s),%s, (SELECT faculty_id from team where project_id=(SELECT project_id from student where SRN=%s)));', (student_srn, student_srn, student_srn))
    mydb.commit()
    c.execute('UPDATE evaluation SET ISA1=%s, ISA2=%s, ISA3=%s, ESA=%s WHERE SRN=%s AND Semester=%s;', (isa1, isa2, isa3, esa, student_srn, student_sem))
    mydb.commit()

def find_students(email_id):
    c.execute('SELECT SRN FROM student WHERE project_id IN (SELECT project_id FROM team where faculty_id=(SELECT ID FROM faculty WHERE email_id=%s));', (email_id,))
    # data = c.execute('CALL find_students(%s);', (email_id,))
    data=c.fetchall()
    return data

def close():
    c.close()
    mydb.close()