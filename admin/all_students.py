import streamlit as st
import pandas as pd

from admin.database import all_students_db

def all_students():
    result = all_students_db()
    df = pd.DataFrame(result, columns=["Name", "SRN", "Sem", "Gender", "CGPA", "Email", "Project ID"])
    st.dataframe(df)