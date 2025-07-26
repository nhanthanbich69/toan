import streamlit as st
import os
from components.fireworks_html import fireworks_display
from components.scrolling_text import scrolling_message
from datetime import datetime

st.set_page_config(layout="wide", page_title="Chúc mừng sinh nhật Lăng Quốc Toàn", page_icon="🎉")
# Text chạy ngang cực "bling bling"
scrolling_message("<h1 style='text-align: center; color: #FF4081;'>💖 Chúc Mừng Sinh Nhật Lăng Quốc Toàn 💸</h1>")
fireworks_display()

st.markdown("---")
st.markdown(
    f"<p style='text-align: center;'>© {datetime.now().year} | Made with 💖 by những người yêu Toàn</p>",
    unsafe_allow_html=True
)
