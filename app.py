import streamlit as st
from datetime import datetime
import os

# Import các component tuỳ chỉnh
from components.fireworks_html import fireworks_display
from components.scrolling_text import scrolling_message

# Thiết lập cấu hình trang
st.set_page_config(
    layout="wide",
    page_title="Chúc mừng sinh nhật Lăng Quốc Toàn",
    page_icon="🎉"
)

# Tiêu đề chính
st.markdown(
    "<h1 style='text-align: center; color: #FF4081;'>🎂 Chúc Mừng Sinh Nhật Lăng Quốc Toàn 🎂</h1>",
    unsafe_allow_html=True
)

# Hiệu ứng pháo hoa
fireworks_display()

# Nhạc nền nếu tồn tại
music_path = "assets/music.mp3"
if os.path.exists(music_path):
    st.audio(music_path, autoplay=True)

# Ảnh gif nếu tồn tại
gif_path = "assets/birthday.gif"
if os.path.exists(gif_path):
    st.image(gif_path, use_column_width=True)

# Dòng chữ cuộn
scrolling_message("Nay sinh nhật bạn Toàn đây, Chúc bạn lương lậu mỗi ngày tiến tới. Công nợ khớp đúng từng nơi, Deadline kịp lúc, thảnh thơi buổi chiều. 😤")

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

st.markdown(
    f"<p style='font-size: 20px; color: #00BCD4; text-align: center;'>{poem}</p>",
    unsafe_allow_html=True
)

# Vùng mở rộng - bất ngờ chưa?
with st.expander("👾 Bấm vào nếu bạn là người tò mò..."):
    st.markdown("Tạm thời chưa có game, nhưng biết đâu mai Toàn lại làm dev game 😎")

# Footer
st.markdown("---")
st.markdown(
    f"<p style='text-align: center;'>© {datetime.now().year} | Made with 💖 by những người yêu Toàn</p>",
    unsafe_allow_html=True
)
