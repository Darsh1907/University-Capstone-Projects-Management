import pandas as pd
import streamlit as st

from student.database import view_domains_db


def view_domains():
    result = view_domains_db()
    df = pd.DataFrame(result, columns=['Domain ID', 'Domain Name'])
    st.dataframe(df)