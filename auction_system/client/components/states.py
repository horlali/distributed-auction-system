import streamlit as st
from Pyro4.errors import CommunicationError

from auction_system.client.components.connections import auth_object


def initiate_st_state_vars():
    if "user_id" not in st.session_state:
        st.session_state["user_id"] = ""

    if "first_name" not in st.session_state:
        st.session_state["first_name"] = ""

    if "user_type" not in st.session_state:
        st.session_state["user_type"] = ""

    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False


def button_login():
    if not st.session_state["authenticated"]:
        form = st.form(key="login_form")
        email = form.text_input("Email")
        password = form.text_input("Password", type="password")

        if form.form_submit_button(label="Login"):
            try:
                user_id, user_type, first_name = auth_object.login(email, password)
                st.session_state["user_id"] = user_id
                st.session_state["first_name"] = first_name
                st.session_state["user_type"] = user_type
                st.session_state["authenticated"] = True
                st.experimental_rerun()

            except TypeError:
                st.error("Incorrect email or password")

            except CommunicationError:
                st.error("Could not connect to server")

    else:
        st.write("You are already logged in.")


def button_signup():
    if not st.session_state["authenticated"]:
        form = st.form(key="signup_form")
        first_name = form.text_input("First Name")
        last_name = form.text_input("Last Name")
        email = form.text_input("Email")
        phone = form.text_input("Phone")
        password = form.text_input("Password", type="password")
        user_type = form.selectbox("User Type", ["seller", "buyer"])

        if form.form_submit_button(label="Sign Up"):
            try:
                user_data = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "phone": phone,
                    "password": password,
                    "user_type": user_type,
                }
                user_id, user_option, fname = auth_object.register(**user_data)
                st.session_state["user_id"] = user_id
                st.session_state["first_name"] = fname
                st.session_state["user_type"] = user_option
                st.session_state["authenticated"] = True
                st.experimental_rerun()

            except TypeError:
                st.error("Error signing up. Please try again.")

            except CommunicationError:
                st.error("Could not connect to server")

    else:
        st.write("You are already logged in / sign up.")


def button_logout():
    if st.sidebar.button("Logout"):
        st.session_state["user_id"] = ""
        st.session_state["first_name"] = ""
        st.session_state["user_type"] = ""
        st.session_state["authenticated"] = False
        st.experimental_rerun()


def authentication_state():
    initiate_st_state_vars()

    if st.session_state["authenticated"]:
        button_logout()

    else:
        col1, col2 = st.columns(2)
        with col1:
            st.header("Login")
            button_signup()

        with col2:
            st.header("Sign Up")
            button_login()
