import streamlit as st

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

    else:
        st.write("You are already logged in.")


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
        button_login()
