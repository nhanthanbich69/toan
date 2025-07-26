import streamlit as st
from components.fireworks_html import fireworks_display
from components.scrolling_text import scrolling_message
from datetime import datetime

st.set_page_config(layout="wide", page_title="Chúc mừng sinh nhật Lăng Quốc Toàn", page_icon="🎉")

st.markdown("<h1 style='text-align: center; color: #FF4081;'>🎂 Chúc Mừng Sinh Nhật Lăng Quốc Toàn 🎂</h1>", unsafe_allow_html=True)

fireworks_display()

st.audio("assets/music.mp3", autoplay=True)

st.image("assets/birthday.gif", use_column_width=True)

scrolling_message("Chúc Toàn luôn vui vẻ, sự nghiệp như diều gặp gió, tiền vào như nước, ế bớt lại giúp tụi tao với 😤")

# Thơ chúc mừng
poem = """
Nay sinh nhật bạn Toàn đây,  
Chúc bạn lương lậu mỗi ngày tiến tới.  
Công nợ khớp đúng từng nơi,  
Deadline kịp lúc, thảnh thơi buổi chiều.  

Tiền vô chẳng thiếu, chẳng nhầm,  
Hạch toán chính xác, chẳng cần lo chi.  
Tuổi này sống khỏe, sống chill,  
Tình duyên nườm nượp - chẳng lo kiếm tìm.
"""

st.markdown(f"<p style='font-size: 20px; color: #00BCD4; text-align: center;'>{poem}</p>", unsafe_allow_html=True)

with st.expander("👾 Bấm vào nếu bạn là người tò mò..."):
    st.markdown("Tạm thời chưa có game, nhưng biết đâu mai Toàn lại làm dev game 😎")

st.markdown("---")
st.markdown(f"<p style='text-align: center;'>© {datetime.now().year} | Made with 💖 by những người yêu Toàn</p>", unsafe_allow_html=True)