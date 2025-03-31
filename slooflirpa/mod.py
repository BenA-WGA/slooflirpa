import streamlit as st
import time

st.set_page_config(layout="wide")

# Top row of buttons
top_buttons = ["Import", "Export", "Node", "Line", "LineLoad", "PointLoad", "Analyse"]
st.markdown("<style>div.stButton > button { width: 100%; }</style>", unsafe_allow_html=True)
top_cols = st.columns(7)
for i, btn in enumerate(top_buttons):
    with top_cols[i]:
        st.button(btn, disabled=True)

# Second row of buttons for Analysis
analysis_buttons = ["LOAD", "SFD", "BMD", "AFD", "DEF"]
analysis_cols = st.columns(5)
for i, btn in enumerate(analysis_buttons):
    with analysis_cols[i]:
        st.button(btn, disabled=True)

# Left Sidebar for Item Explorer
st.sidebar.title("Item Explorer")
st.sidebar.markdown("<p style='font-size: 18px;'>Create Some items to get started!</p>", unsafe_allow_html=True)

# Right Sidebar for Properties
st.sidebar.title("Properties")
st.sidebar.markdown("<p style='font-size: 18px;'>Select an item</p>", unsafe_allow_html=True)

# Main Layout
st.markdown("""
    <div style='border: 0px solid black; padding: 10px; height: 80vh; display: flex; justify-content: center; align-items: center;'>
        <h1 style='font-size: 50px;'>ALL LICENSES IN USE PLEASE RELEASE A LICENSE OR CONTACT YOUR NETWORK ADMIN</h1>
    </div>
""", unsafe_allow_html=True)
