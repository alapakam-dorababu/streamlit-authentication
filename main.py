import yaml 
import streamlit as st
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader

# Load configuration
with open('credentials.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Initialize authenticator
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['key'],
    config['cookie']['name'],
    config['cookie']['expiry_days'],
)



try:
    authenticator.login()
except Exception as e:
    st.error(e)
    
    
if st.session_state["authentication_status"]:
    st.write('___')
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')    
    st.write('___')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
    
