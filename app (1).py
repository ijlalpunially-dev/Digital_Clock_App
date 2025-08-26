import streamlit as st
import time
from datetime import datetime

# Page config
st.set_page_config(page_title="Digital Clock", page_icon="⏰", layout="centered")

st.title("🕒 Updated Digital Clock")

# Keep updating the clock in real-time
clock_placeholder = st.empty()

while True:
    now = datetime.now().strftime("%H:%M:%S")
    clock_placeholder.markdown(
        f"<h1 style='text-align: center; font-size: 80px;'>{now}</h1>",
        unsafe_allow_html=True,
    )
    time.sleep(1)
