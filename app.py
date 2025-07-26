import streamlit as st
import os
from components.fireworks_html import fireworks_display
from components.scrolling_text import scrolling_message
from datetime import datetime

st.set_page_config(layout="wide", page_title="Chúc mừng sinh nhật Lăng Quốc Toàn", page_icon="🎉")

st.markdown("<h1 style='text-align: center; color: #FF4081;'>🎂 Chúc Mừng Sinh Nhật Lăng Quốc Toàn 🎂</h1>", unsafe_allow_html=True)

fireworks_display()

# Kiểm tra file audio có tồn tại không trước khi phát
music_path = "assets/music.mp3"
if os.path.exists(music_path):
    st.audio(music_path, autoplay=True)
else:
    st.warning("🎵 File nhạc không tồn tại, bỏ qua phần nhạc nhé!")

# Hiển thị ảnh gif nếu có
gif_path = "assets/birthday.gif"
if os.path.exists(gif_path):
    st.image(gif_path, use_column_width=True)
else:
    st.warning("🎁 Ảnh gif chúc mừng chưa có, bạn có thể thêm vào thư mục 'assets'.")

# Text chạy ngang cực "bling bling"
scrolling_message("💖 Chúc Toàn luôn vui vẻ, sự nghiệp như diều gặp gió, tiền vào như nước 💸")

# Thơ chúc mừng — chuyển \n thành <br> để hiển thị đúng dòng
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

poem_html = poem.strip().replace('\n', '<br>')
st.markdown(
    f"<p style='font-size: 20px; color: #00BCD4; text-align: center;'>{poem_html}</p>",
    unsafe_allow_html=True
)

st.markdown("---")
st.markdown(
    f"<p style='text-align: center;'>© {datetime.now().year} | Made with 💖 by những người yêu Toàn</p>",
    unsafe_allow_html=True
)
