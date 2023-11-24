import pandas as pd
import streamlit as st

from admin.database import delete_domain_db
from admin.database import view_domains_db

def delete_domain():
    st.text("Available domains")
    result = view_domains_db()
    df = pd.DataFrame(result, columns=['Domain ID', 'Domain Name'])
    st.dataframe(df)
    st.divider()
    st.text("Delete a Domain:")
    domain_id = st.number_input("Domain ID:", min_value=1, step=1, key=1)
    if st.button("Delete Domain"):
        delete_domain_db(domain_id)
        st.success("Successfully deleted Domain: {}".format(domain_id))