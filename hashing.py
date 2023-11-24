import streamlit_authenticator as stauth

hashed_passwords = stauth.Hasher(['blah']).generate()

print(hashed_passwords)