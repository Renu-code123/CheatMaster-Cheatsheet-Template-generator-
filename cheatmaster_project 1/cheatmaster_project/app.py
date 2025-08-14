import streamlit as st
import os

# Page title and layout
st.set_page_config(page_title="CheatMaster", layout="wide")

# Read your HTML
html_file_path = os.path.join("cheatmaster_project", "index.html")
with open(html_file_path, "r", encoding="utf-8") as f:
    html_code = f.read()

# Display HTML in Streamlit
st.components.v1.html(html_code, height=900, scrolling=True)
