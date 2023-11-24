import streamlit as st
import pandas as pd

from admin.database import view_toppers_db

def view_toppers():
    result = view_toppers_db()
    df = pd.DataFrame(result, columns=['Semester', 'SRN', 'Faculty Mentor ID','ISA1', 'ISA2', 'ISA3', 'ESA'])
    st.dataframe(df)