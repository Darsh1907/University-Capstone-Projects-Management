import pandas as pd
import streamlit as st

from student.database import view_status_db


def view_status(srn):
    st.divider()
    result = view_status_db(srn)
    df = pd.DataFrame(result, columns=['Name', 'SRN', 'Project ID', 'Mentor', 'Approved?', 'Project Name', 'Panel ID', 'project_desc', 'Domain'])
    if len(result)==0:
        st.warning("No Projects Found")
        return 
    if result[0][4]==1:
        st.subheader("Your Project is Approved!!")
        st.text("Mentor Name: {}".format(result[0][3]))
        st.text("Panel ID: {}".format(result[0][6]))
    else:
        st.subheader("Your Project is waiting to be Approved!!")
    st.text("Project ID: {}".format(result[0][2]))
    st.text("Project Name: {}".format(result[0][5]))
    st.text("Project Description: {}".format(result[0][7]))
    st.text("Domain ID: {}".format(result[0][8]))