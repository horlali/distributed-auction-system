import streamlit as st


def initiate_state():
    if "auth_code" not in st.session_state:
        st.session_state["auth_code"] = ""

    if "auth_code_valid" not in st.session_state:
        st.session_state["auth_code_valid"] = False

    if "user_type" not in st.session_state:
        st.session_state["user_type"] = ""

def get_auth_code():
    auth_query_query_params = st.experimental_get_query_params()
    # try:
    #     auth_code = st.session_state["auth_code"]
    # return st.session_state["auth_code"]
