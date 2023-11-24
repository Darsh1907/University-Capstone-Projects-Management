import streamlit as st
import pandas as pd
from student.database import add_team
from student.database import view_status_db

def add_proj(srn):
    is_team = view_status_db(srn)
    is_team_df = pd.DataFrame(is_team)
    if(is_team_df.empty):
        col1, col2 = st.columns(2)
        with col1:
            mate1 = st.text_input("SRN of Team Mate 1:")
            mate2 = st.text_input("SRN of Team Mate 2:")
        with col2:
            proj_name = st.text_input("Project Name:")
            proj_desc = st.text_input("Project Description:")
        domain_id = st.number_input("Domain ID:", min_value=0, step=1)
        if st.button("Add Project"):
            if(srn==mate1 or srn==mate2 or mate1==mate2):
                st.warning("Please Dont Repeat SRNs")
            else:
                add_team(srn, mate1, mate2, proj_name, proj_desc, domain_id)
                st.success("Successfully added Team/Project: {}".format(proj_name))
    else:
        st.subheader("You already have a Team")