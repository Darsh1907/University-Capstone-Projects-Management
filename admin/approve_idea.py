import pandas as pd
import streamlit as st

from admin.database import not_approved_ids
from admin.database import not_approved_team_data
from admin.database import not_approved_students
from admin.database import approve_team
from admin.database import reject_team
from admin.database import mentor_ids_db
from admin.database import avail_panels_db

def approve_idea():
    result = not_approved_ids()
    result = [item[0] for item in result]
    if len(result) == 0:
        st.divider()
        st.text("No new ideas to approve")
        return

    project_id = st.selectbox("Select Project ID:", result)

    col1, col2 = st.columns(2)
    with col1:
        st.text("Project Data:")
        data1 = not_approved_team_data(project_id)
        df1 = pd.DataFrame(data1, columns=['Project ID', 'Project Name', 'Project Desc', 'Domain ID'])
        st.dataframe(df1)
    with col2:
        st.text("Student Details:")
        data2 = not_approved_students(project_id)
        df2 = pd.DataFrame(data2, columns=['SRN', 'Sem', 'Gender', 'CGPA'])
        st.dataframe(df2)

    st.divider()

    col1, col2 == st.columns(2)
    with col1:
        st.text("Available Mentors:")
        mentors_data = mentor_ids_db()
        mentors_df = pd.DataFrame(mentors_data, columns=["Mentor ID", 'Name', 'Domain ID'])
        st.dataframe(mentors_df)
    with col2:
        st.text("Available Panels:")
        avail_panels = avail_panels_db()
        avail_panels_df = pd.DataFrame(avail_panels, columns=["ID", "Panel Head", "Domain"])
        st.dataframe(avail_panels_df)

    mentor_id = st.number_input("Mentor ID:", min_value=0, max_value=30, step=1, key=1)
    panel_id = st.number_input("Panel ID:", min_value=0, max_value=30, step=1, key=2)

    if st.button("Approve"):
        approve_team(project_id, mentor_id, panel_id)
        st.success("Successfully Approved Project ID: {}".format(project_id))
    
    if st.button("Reject"):
        reject_team(project_id)
        st.success("Rejected Team ID: {}".format(project_id))