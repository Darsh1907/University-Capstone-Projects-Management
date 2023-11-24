import mysql.connector

#set your mysql password
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql@dbms@123",
    database="capstones"
)

c = mydb.cursor()

def get_panel_head(srn):
    c.execute("SELECT head_id from panel where panel_id=(SELECT panel_id from team where project_id=(SELECT project_id from student WHERE SRN=%s));", (srn, ))
    head_id = c.fetchall()[0][0]
    return head_id

def add_team(srn, mate1, mate2, proj_name, proj_desc, domain_id):
    c.execute('INSERT INTO team (project_name, project_desc, domain_id) VALUES (%s,%s,%s);', (proj_name, proj_desc, domain_id))
    mydb.commit()
    c.execute('UPDATE student SET project_id=(SELECT project_id FROM team WHERE (project_name=%s AND project_desc=%s AND domain_id=%s)) WHERE SRN IN (%s,%s,%s);', (proj_name, proj_desc, domain_id, srn, mate1, mate2))
    mydb.commit()

def view_status_db(srn):
    # c.execute('select s.Name, s.SRN, s.project_id, t.faculty_id, is_approved, t.project_name, t.panel_id, t.project_desc, t.domain_id from student as s, team as t WHERE s.project_id=t.project_id AND s.SRN=%s;', (srn,))
    c.execute('SELECT is_approved from student as s, team as t WHERE s.project_id=t.project_id AND s.SRN=%s;', (srn,))
    is_approved = -1
    data = c.fetchall()
    # return data
    if len(data)>0:
        is_approved = data[0][0]
    if is_approved == 0 or is_approved == -1:
        c.execute('select s.Name, s.SRN, s.project_id, t.faculty_id, is_approved, t.project_name, t.panel_id, t.project_desc, t.domain_id from student as s, team as t WHERE s.project_id=t.project_id AND s.SRN=%s;', (srn,))
        ans = c.fetchall()
        return ans
    elif is_approved == 1:
        c.execute('select s.Name, s.SRN, s.project_id, f.name, is_approved, t.project_name, t.panel_id, t.project_desc, t.domain_id from student as s, team as t, faculty as f WHERE s.project_id=t.project_id AND t.faculty_id=f.ID AND s.SRN=%s;', (srn,))
        ans = c.fetchall()
        return ans
    

def view_domains_db():
    # c.execute('CALL get_all_domains();')
    c.execute('SELECT * FROM domain ORDER BY DomainID ASC;')
    data = c.fetchall()
    return data

def view_evaluation_db(srn):
    c.execute('INSERT IGNORE INTO evaluation (`Semester`, `SRN`, `Faculty_ID`) VALUES ((SELECT Sem from student where SRN=%s),%s, (SELECT faculty_id from team where project_id=(SELECT project_id from student where SRN=%s)));', (srn, srn, srn))
    mydb.commit()
    c.execute('SELECT * FROM evaluation WHERE SRN=%s;', (srn,))
    data = c.fetchall()
    return data

def view_panel_db(srn):
    c.execute('SELECT ID, name, email_id, d.`Domain Name` FROM faculty as f, domain as d WHERE panel_id=(SELECT panel_id FROM team where project_id=(SELECT project_id FROM student WHERE SRN=%s)) AND d.DomainID=f.domain_id;', (srn,))
    data = c.fetchall()
    return data

def close():
    c.close()
    mydb.close()