import pandas as pd
import streamlit as st

from admin.database import not_approved_teams_db

def not_approved_teams():
    result = not_approved_teams_db()
    df = pd.DataFrame(result, columns=['Project ID', 'Project Name', 'Project Desc', 'Domain ID'])
    st.dataframe(df)