import sqlite3
import streamlit as st
import streamlit_authenticator as stauth

# DB setup (create table if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        name TEXT,
        password TEXT
    )
''')
conn.commit()

# Fetch credentials from DB
cursor.execute("SELECT username, name, password FROM users")
rows = cursor.fetchall()

credentials = {
    "usernames": {
        row[0]: {"name": row[1], "password": row[2]}
        for row in rows
    }
}

cookie_config = {
    'key': 'auth_key',
    'name': 'auth_cookie',
    'expiry_days': 30
}

authenticator = stauth.Authenticate(
    credentials,
    cookie_config['key'],
    cookie_config['name'],
    cookie_config['expiry_days'],
)


try:
    authenticator.login()
except Exception as e:
    st.error(e)
    
    
if not st.session_state.get("authentication_status"):
    st.subheader("Register New User")
    new_name = st.text_input("Name", key="reg_name")
    new_username = st.text_input("Username", key="reg_user")
    new_password = st.text_input("Password", type="password", key="reg_pass")

    if st.button("Register"):
        cursor.execute("SELECT * FROM users WHERE username=?", (new_username,))
        if cursor.fetchone():
            st.warning("Username already exists.")
        elif not (new_name and new_username and new_password):
            st.warning("Please fill all fields.")
        else:
            # Optionally hash password
            # hashed_password = stauth.Hasher([new_password]).generate()
            cursor.execute(
                "INSERT INTO users (username, name, password) VALUES (?, ?, ?)",
                (new_username, new_name, new_password)
            )
            conn.commit()
            st.success("User registered successfully!")


# --- Main UI logic ---
if st.session_state.get("authentication_status"):
    st.write('___')
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
    st.write('___')


     
