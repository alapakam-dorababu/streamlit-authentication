# Streamlit Authentication App

This project implements user authentication in a Streamlit application using streamlit-authenticator. Users can log in with predefined credentials stored in a YAML file. The app provides a secure login mechanism, session management, and dynamic content display based on authentication status.

## Features
- User login with bcrypt-hashed passwords

- Cookie-based session management

- Customizable user credentials and authentication settings

- Simple login/logout flow with error and status handling

## Getting Started

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Generate password hashes using the hash.py utility.

3. Update credentials.yaml with the generated hashed password(s).

4. Run the app:

```bash
streamlit run main.py
```