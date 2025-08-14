import streamlit as st
import os

st.set_page_config(page_title="CheatMaster", layout="wide")

# Load CSS and JS as strings
def load_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

style_css = f"<style>{load_file('cheatmaster_project/style.css')}</style>"
prism_css = f"<style>{load_file('cheatmaster_project/prism.css')}</style>"
app_js = f"<script>{load_file('cheatmaster_project/app.js')}</script>"
prism_js = f"<script>{load_file('cheatmaster_project/prism.js')}</script>"

# Map page names to HTML files
pages = {
    "🏠 Home": "cheatmaster_project/index.html",
    "📄 HTML Cheatsheet": "cheatmaster_project/html_cheatsheet.html",
    "🎨 CSS Cheatsheet": "cheatmaster_project/css_cheatsheet.html",
    "⚙️ JS Cheatsheet": "cheatmaster_project/js_cheatsheet.html"
}

choice = st.sidebar.radio("Select a page:", list(pages.keys()))

# Load selected HTML
html_content = load_file(pages[choice])

# Inject CSS + HTML + JS
full_content = style_css + prism_css + html_content + prism_js + app_js

st.components.v1.html(full_content, height=900, scrolling=True)
