from pathlib import Path

import streamlit as st

from auction_system.utils.constants import BASE_DIR

st.set_page_config(page_title="About", page_icon="👋", layout="wide")

about_markdown = Path(BASE_DIR / "README.md").read_text()
st.markdown(about_markdown, unsafe_allow_html=True)
