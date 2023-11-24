import streamlit as st
import pandas as pd

from admin.database import all_faculties_db

def all_faculties():
    result = all_faculties_db()
    df = pd.DataFrame(result, columns=["ID", "Name", "Email", "Panel ID", "Domain ID"])
    st.dataframe(df)