import streamlit as st
from components.fireworks_html import fireworks_display
from components.scrolling_text import scrolling_message
from datetime import datetime

st.set_page_config(layout="wide", page_title="🎉 Toàn", page_icon="💌")

if "opened" not in st.session_state:
    st.session_state.opened = False

# Nếu chưa mở, hiển thị icon thư làm nút bấm
if not st.session_state.opened:
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

    <div class="envelope-container" onclick="fetch('/?open=true').then(() => window.location.reload())">
        <div class="envelope-emoji">💌</div>
        <div class="envelope-text">Ấn để mở</div>
    </div>
    """, unsafe_allow_html=True)

    # Trick để cập nhật trạng thái
    query_params = st.experimental_get_query_params()
    if "open" in query_params:
        st.session_state.opened = True
        st.experimental_set_query_params()  # Clear param
        st.rerun()

# Nội dung khi đã mở thư
else:
    scrolling_message("<h1 style='text-align: center; color: #FF4081;'>💖 Chúc Mừng Sinh Nhật Lăng Quốc Toàn 💸</h1>")
    fireworks_display()
    st.markdown("---")
    st.markdown(
        f"<p style='text-align: center;'>© {datetime.now().year} | Made with 💖 by những người bạn</p>",
        unsafe_allow_html=True
    )
