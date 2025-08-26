import streamlit as st
import time
from datetime import datetime, timedelta

# Page config
st.set_page_config(page_title="Digital Clock", page_icon="⏰", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #0f172a;
        color: white;
    }
    .clock {
        text-align: center;
        font-size: 100px;
        font-weight: bold;
        color: #00ffcc;
        text-shadow: 2px 2px 10px #00ffcc;
    }
    .date {
        text-align: center;
        font-size: 30px;
        color: #facc15;
        margin-top: -20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("⏰ Stylish Digital Clock")

# Session state
if "paused" not in st.session_state:
    st.session_state.paused = False
if "custom_time" not in st.session_state:
    st.session_state.custom_time = None

# Mode selector
mode = st.radio("Select Clock Mode:", ["System Time", "Custom Time"])

if mode == "Custom Time":
    set_time = st.time_input("Set a custom start time:")
    if st.button("Start Custom Clock"):
        st.session_state.custom_time = datetime.combine(datetime.today(), set_time)
        st.session_state.paused = False

# Buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⏸ Pause"):
        st.session_state.paused = True
with col2:
    if st.button("▶ Resume"):
        st.session_state.paused = False
with col3:
    if st.button("🔄 Reset"):
        st.session_state.custom_time = None
        st.session_state.paused = False

# Clock placeholder
clock_placeholder = st.empty()
date_placeholder = st.empty()

# Update loop
while True:
    if not st.session_state.paused:
        if mode == "System Time" or st.session_state.custom_time is None:
            now = datetime.now()
        else:
            st.session_state.custom_time += timedelta(seconds=1)
            now = st.session_state.custom_time

        # Display clock
        clock_placeholder.markdown(f"<div class='clock'>{now.strftime('%H:%M:%S')}</div>", unsafe_allow_html=True)
        date_placeholder.markdown(f"<div class='date'>{now.strftime('%A, %d %B %Y')}</div>", unsafe_allow_html=True)

    time.sleep(1)
