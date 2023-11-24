import streamlit as st
import pandas as pd

from faculty.database import your_students_db

def your_students(email_id):
    students = your_students_db(email_id)
    df1 = pd.DataFrame(students, columns=["Name", "SRN", "Sem", "Gender", "CGPA", "email", "Project ID"])
    if df1.empty:
        st.divider()
        st.text("You dont have any students under your mentorship")
        return 
    st.dataframe(df1)