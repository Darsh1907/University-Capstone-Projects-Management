import mysql.connector
import pandas as pd
import streamlit as st

#set your mysql password
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql@dbms@123",
    database="capstones"
)

c = mydb.cursor()

def all_students_db():
    c.execute("SELECT * FROM student")
    data = c.fetchall()
    return data

def all_faculties_db():
    c.execute("SELECT * FROM faculty")
    data = c.fetchall()
    return data

def delete_domain_db(id):
    c.execute("DELETE from domain WHERE DomainID=%s", (id,))
    mydb.commit()

def view_toppers_db():
    c.execute('SELECT * from evaluation where ISA1+ISA2+ISA3+ESA >= (SELECT AVG(ISA1+ISA2+ISA3+ESA) from evaluation)')
    data = c.fetchall()
    return data

def avail_panels_db():
    c.execute("SELECT p.panel_id, f.ID, d.DomainID FROM panel as p, faculty as f, domain as d WHERE p.head_id=f.ID AND p.panel_id=d.DomainID AND p.panel_id=f.panel_id")
    data = c.fetchall()
    return data

def mentor_ids_db():
    c.execute("SELECT ID, name, domain_id FROM faculty")
    data = c.fetchall()
    return data

def reject_team(id):
    c.execute('UPDATE student SET project_id=NULL where project_id=%s', (id,))
    mydb.commit()
    c.execute('DELETE from team where project_id=%s', (id,))
    mydb.commit()

def view_domains_db():
    # c.callproc('get_all_domains')
    # c.nextset()
    c.execute('SELECT * FROM domain ORDER BY DomainID ASC;')
    data = c.fetchall()
    return data

def add_domain_db(domain_name):
    c.execute('INSERT into domain (`Domain Name`) VALUES (%s)', (domain_name, ))
    mydb.commit()

def approve_team(project_id, mentor_id, panel_id):
    c.execute('UPDATE team SET is_approved=1, faculty_id=%s, panel_id=%s WHERE project_id=%s', (mentor_id, panel_id, project_id))
    mydb.commit()

def not_approved_students(id):
    c.execute('SELECT SRN, Sem, Gender, CGPA from student WHERE project_id=%s', (id,))
    data = c.fetchall()
    return data

def not_approved_ids():
    c.execute("SELECT project_id FROM team where is_approved=0")
    data = c.fetchall()
    return data

def not_approved_team_data(id):
    c.execute('SELECT project_id, project_name, project_desc, domain_id from team where is_approved=0 && project_id=%s;', (id, ))
    data = c.fetchall()
    return data

def increment_semester_db():
    c.execute('SELECT capstones.increase_year();')
    data = c.fetchall()
    mydb.commit()
    return

def create_panel_db(id1, id2, id3, head_id, domain_id):
    c.execute('INSERT INTO panel (domain_id, head_id) VALUES (%s,%s)', (domain_id, head_id))
    mydb.commit()
    c.execute('UPDATE faculty SET panel_id=(SELECT panel_id FROM panel WHERE head_id = %s) WHERE ID IN (%s,%s,%s)', (head_id, id1, id2, id3))
    mydb.commit()

def avail_for_panel_db():
    c.execute('SELECT ID, name, domain_id FROM faculty where panel_id IS NULL ORDER BY ID ASC;')
    data = c.fetchall()
    return data

def avail_for_panel_id():
    c.execute('SELECT id FROM faculty where panel_id IS NULL ORDER BY ID ASC;')
    data = c.fetchall()
    return data

def close():
    c.close()
    mydb.close()