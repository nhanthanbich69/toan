import streamlit as st
from datetime import datetime
from components.fireworks_html import fireworks_display
from components.scrolling_text import scrolling_message

st.set_page_config(layout="wide", page_title="Chúc mừng sinh nhật Lăng Quốc Toàn", page_icon="🎉")

# Lấy query param
query_params = st.experimental_get_query_params()
if "open" in query_params and query_params["open"] == ["true"]:
    st.session_state.opened = True
    st.experimental_set_query_params()  # Xoá khỏi URL
    st.rerun()

# Nếu chưa mở thư thì hiển thị nút
if "opened" not in st.session_state or not st.session_state.opened:
    st.markdown(
        """
        <div style='display: flex; justify-content: center; align-items: center; height: 90vh;'>
            <a href='?open=true' style='
                background-color: #FF4081;
                padding: 20px 40px;
                font-size: 28px;
                color: white;
                text-decoration: none;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            '>
                📬 Ấn để mở
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.stop()

# Khi đã mở thư
scrolling_message("<h1 style='text-align: center; color: #FF4081;'>💖 Chúc Mừng Sinh Nhật Lăng Quốc Toàn 💸</h1>", unsafe_allow_html=True)
fireworks_display()

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

poem_html = poem.strip().replace('\n', '<br>')
st.markdown(
    f"<p style='font-size: 20px; color: #00BCD4; text-align: center; margin-top: 50px;'>{poem_html}</p>",
    unsafe_allow_html=True
)

st.markdown("---")
st.markdown(
    f"<p style='text-align: center;'>© {datetime.now().year} | Made with 💖 by những người yêu Toàn</p>",
    unsafe_allow_html=True
)
