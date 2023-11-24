import pandas as pd
import streamlit as st

from admin.database import avail_for_panel_db


def avail_for_panel():
    result = avail_for_panel_db()
    df = pd.DataFrame(result, columns=['ID', 'Name', 'Domain ID'])
    st.dataframe(df)