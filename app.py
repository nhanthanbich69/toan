import streamlit as st
from components.fireworks_html import fireworks_display
from components.scrolling_text import scrolling_message
from datetime import datetime

st.set_page_config(layout="wide", page_title="🎉 Thư", page_icon="💌")

# Khởi tạo trạng thái
if "opened" not in st.session_state:
    st.session_state.opened = False

# Hiển thị bức thư nếu chưa mở
if not st.session_state.opened:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center;'>
            <h2 style="color: #FF4081;">💌 Ấn vào 💌</h2>
            <p>Click để mở 🎁</p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("📨 Mở thư sinh nhật", use_container_width=True):
        st.session_state.opened = True
        st.experimental_rerun()

# Nội dung khi đã mở thư
else:
    # Text chạy bling bling
    scrolling_message("<h1 style='text-align: center; color: #FF4081;'>💖 Chúc Mừng Sinh Nhật Lăng Quốc Toàn 💸</h1>")

    # Pháo hoa + thơ overlay đã gắn trong fireworks_display()
    fireworks_display()

    st.markdown("---")
    st.markdown(
        f"<p style='text-align: center;'>© {datetime.now().year} | Made with 💖 by những người bạn</p>",
        unsafe_allow_html=True
    )
