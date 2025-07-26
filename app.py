import streamlit as st
from components.fireworks_html import fireworks_display
from components.scrolling_text import scrolling_message
from datetime import datetime

st.set_page_config(layout="wide", page_title="Toàn")

query_params = st.query_params

# Check nếu chưa mở
if query_params.get("open") != "true":

    st.markdown("""
    <style>
    .envelope-container {
        text-align: center;
        margin-top: 200px;
        cursor: pointer;
    }
    .envelope-emoji {
        font-size: 120px;
        transition: transform 0.3s ease;
    }
    .envelope-emoji:hover {
        transform: scale(1.1);
    }
    .envelope-text {
        font-size: 24px;
        color: #FF4081;
    }
    </style>

    <div class="envelope-container">
        <a href="?open=true" style="text-decoration: none;">
            <div class="envelope-emoji">💌</div>
            <div class="envelope-text">Ấn để mở</div>
        </a>
    </div>
    """, unsafe_allow_html=True)

else:
    scrolling_message("<h1 style='text-align: center; color: #FF4081;'>💖 Chúc Mừng Sinh Nhật Lăng Quốc Toàn 💸</h1>")
    fireworks_display()
    
    st.markdown("---")
    st.markdown(
        f"<p style='text-align: center;'>© {datetime.now().year} | Made with 💖 by những người bạn</p>",
        unsafe_allow_html=True
    )
