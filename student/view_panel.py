import pandas as pd
import streamlit as st

from student.database import view_panel_db
from student.database import get_panel_head


def view_panel(srn):
    st.divider()
    result = view_panel_db(srn)
    df = pd.DataFrame(result, columns=['ID', 'name', 'email_id', 'Domain Name'])
    if df.empty:
        st.text("You dont have any ongoing Project")
        return
    st.dataframe(df)
    st.divider()
    if df.empty:
        return
    head_id = get_panel_head(srn)
    if(head_id) :
        st.text("Panel Head (ID): {}".format(head_id))