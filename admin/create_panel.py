import streamlit as st
import pandas as pd

from admin.database import create_panel_db
from admin.database import avail_for_panel_id
from admin.database import view_domains_db


def create_panel():
    col1, col2 = st.columns(2)
    avail_for_panel = avail_for_panel_id()
    avail_for_panel = [item[0] for item in avail_for_panel]
    with col1:
        id1 = st.selectbox("Select Faculty1 (ID):", avail_for_panel, key=1)
        id2 = st.selectbox("Select Faculty2 (ID):", avail_for_panel, key=2)
        id3 = st.selectbox("Select Faculty2 (ID):", avail_for_panel, key=3)
        head_options = [id1, id2, id3]
    with col2:
        head_id = st.selectbox("Select Panel Head (ID):", head_options)
        domain_id = st.number_input("Domain ID:", min_value=0, step=1)
    if id1==id2 or id2==id3 or id3==id1:
        st.warning("Please select 3 unique faculty ID")
    if st.button("Add Panel"):
        if id1==id2 or id2==id3 or id3==id1:
            st.error("Please select 3 unique faculty ID", icon="🙏")
            return
        create_panel_db(id1, id2, id3, head_id, domain_id)
        st.success("Successfully added Panel headed by: {}".format(head_id))