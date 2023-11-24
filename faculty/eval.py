import streamlit as st
import pandas as pd

from faculty.database import eval_db
from faculty.database import see_eval
from faculty.database import find_students

def eval(email_id):
    students = find_students(email_id)
    students = [item[0] for item in students]
    if len(students)==0:
        st.divider()
        st.text("You don't have any student under your mentorship")
        return
    student_srn = st.selectbox("Select Student:", students)
    student_sem = st.selectbox("Sem:", [5,6,7,8])
    eval_state = see_eval(student_srn, student_sem)
    df = pd.DataFrame(eval_state, columns=['Sem', 'SRN', 'Faculty ID', 'ISA1', 'ISA2', 'ISA3', 'ESA'])
    if df.empty:
        st.text("Evaluation not available for Student:{} and Semester:{}".format(student_srn, student_sem))
        return
    st.dataframe(df)
    isa1 = st.number_input("ISA1:", min_value=0, max_value=30, step=1, key=1)
    isa2 = st.number_input("ISA2:", min_value=0, max_value=30, step=1, key=2)
    isa3 = st.number_input("ISA3:", min_value=0, max_value=30, step=1, key=3)
    esa = st.number_input("ESA:", min_value=0, max_value=100, step=1, key=4)
    if st.button("Update"):
        eval_db(isa1, isa2, isa3, esa, student_srn, student_sem)
        st.success("Successfully Updated Marks for: {}".format(student_srn))