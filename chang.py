import streamlit as st
from components.fireworks_html import fireworks_display
from components.scrolling_text import scrolling_message
from datetime import datetime

st.set_page_config(layout="wide", page_title="Toàn 🎉", page_icon="🎂")

query_params = st.query_params

# Nếu chưa mở thư
if query_params.get("open") != "true":
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    body {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
        animation: gradientShift 8s ease infinite alternate;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }

    .envelope-container {
        text-align: center;
        margin-top: 25vh;
        cursor: pointer;
        transition: transform 0.3s ease;
    }

    .envelope-container:hover {
        transform: scale(1.05);
    }

    .envelope-emoji {
        font-size: 100px;
        animation: float 2.5s ease-in-out infinite;
        filter: drop-shadow(0px 4px 6px rgba(0,0,0,0.2));
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }

    .envelope-text {
        margin-top: 20px;
        font-size: 22px;
        color: white;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(6px);
        display: inline-block;
        padding: 10px 25px;
        border-radius: 25px;
        transition: background 0.3s ease;
    }

    .envelope-text:hover {
        background: rgba(255, 255, 255, 0.3);
    }

    a {
        text-decoration: none;
    }
    </style>

    <div class="envelope-container">
        <a href="?open=true">
            <div class="envelope-emoji">📨</div>
            <div class="envelope-text">Bấm để mở 🎁</div>
        </a>
    </div>
    """, unsafe_allow_html=True)

# Nếu đã mở thư
else:
    scrolling_message("""
    <h1 style='text-align: center; 
               color: #FF4B91; 
               font-family: Poppins, sans-serif;
               font-size: 2.8em;
               animation: fadeIn 1.5s ease;'>
        🎉 Chúc Mừng Sinh Nhật Lăng Quốc Toàn 💖
    </h1>
    """)
    
    fireworks_display()

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <p style='text-align: center; 
                  color: #ffffffaa; 
                  font-family: Poppins, sans-serif; 
                  font-size: 16px;'>
            © {datetime.now().year} | Made with 💗 by những người bạn ✨
        </p>
        """,
        unsafe_allow_html=True
    )
