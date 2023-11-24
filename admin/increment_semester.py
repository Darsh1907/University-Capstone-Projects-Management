import streamlit as st
from admin.database import increment_semester_db

def increment_semester():
    if st.button("Increment!!"):
        increment_semester_db()
        st.success("Successfully incremented Semester for Each Student")