import pandas as pd
import streamlit as st

from admin.database import add_domain_db
from admin.database import view_domains_db

def add_domain():
    st.text("Available domains")
    result = view_domains_db()
    df = pd.DataFrame(result, columns=['Domain ID', 'Domain Name'])
    st.dataframe(df)
    st.divider()
    st.text("Add new domain:")
    domain_name = st.text_input("Domain Name:")
    if st.button("Add Domain"):
        add_domain_db(domain_name)
        st.success("Successfully added Domain: {}".format(domain_name))
    