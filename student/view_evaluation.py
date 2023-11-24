import pandas as pd
import streamlit as st

from student.database import view_evaluation_db


def view_evaluation(srn):
    result = view_evaluation_db(srn)
    df = pd.DataFrame(result, columns=['Semester', 'SRN', 'Faculty ID', 'ISA1', 'ISA2', 'ISA3', 'ESA'])
    st.divider()
    if df.empty:
        st.text('You dont have any ongoing project')
        return 
    st.dataframe(df)