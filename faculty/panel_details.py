import streamlit as st
import pandas as pd

from faculty.database import view_panel
from faculty.database import get_panel_head
from faculty.database import view_teams_db

def panel_details(email_id):
    panel = view_panel(email_id)
    df1 = pd.DataFrame(panel, columns=['ID', 'name', 'email_id', 'Domain Name'])
    if df1.empty:
        st.divider()
        st.text("You are not a part of any panel yet")
        return
    st.text('Your Panel')
    st.dataframe(df1)
    head_id = get_panel_head(email_id)
    if(head_id):
        st.text("Panel Head (ID): {}".format(head_id))
    st.divider()
    st.text('Teams under your Panel:')
    teams = view_teams_db(email_id)
    df2 = pd.DataFrame(teams, columns=['ID', 'Project Name', 'Project Desc', 'Domain Name'])
    st.dataframe(df2)

