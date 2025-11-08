import streamlit as st
from datetime import datetime
from components.fireworks_html import fireworks_display

st.set_page_config(layout="wide", page_title="Quỳnh Trang 🎂", page_icon="🎉")

query_params = st.query_params

if query_params.get("open") != "true":
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    body {
        background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
        font-family: 'Poppins', sans-serif;
        height: 100vh;
    }

    .envelope-container {
        text-align: center;
        margin-top: 35vh;
        cursor: pointer;
        transition: transform 0.3s ease;
    }

    .envelope-container:hover {
        transform: scale(1.05);
    }

    .envelope-emoji {
        font-size: 90px;
        animation: float 2.5s ease-in-out infinite;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }

    .envelope-text {
        margin-top: 20px;
        font-size: 20px;
        color: white;
        background: rgba(255,255,255,0.15);
        padding: 10px 25px;
        border-radius: 25px;
        display: inline-block;
    }

    a { text-decoration: none; }
    </style>

    <div class="envelope-container">
        <a href="?open=true">
            <div class="envelope-emoji">💌</div>
            <div class="envelope-text">Bấm để mở 🎁</div>
        </a>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    body {
        background: linear-gradient(120deg, #ffecd2 0%, #fcb69f 100%);
        font-family: 'Poppins', sans-serif;
        overflow: hidden;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .message-box {
        text-align: center;
        color: #FF4B91;
        font-size: clamp(20px, 4vw, 40px);
        line-height: 1.4em;
        font-weight: 600;
        animation: fadeIn 1s ease;
        padding: 20px;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeOut {
        from { opacity: 1; transform: translateY(0); }
        to { opacity: 0; transform: translateY(-20px); }
    }
    </style>

    <div class="message-box" id="message-box"></div>

    <script>
    const messages = [
        "Hôm nay nhân ngày kỉ niệm 2 thập kỉ và 2 năm ngày bạn Chang xuất hiện 💫",
        "Tớ chúc cậu luôn luôn hạnh phúc và yêu đời 💖",
        "Cậu lúc nào cũng xinh hết 🌸",
        "🎉 HAPPY BIRTHDAY QUỲNH TRANG 💗"
    ];

    const box = document.getElementById("message-box");
    let index = 0;

    function showMessage() {
        box.style.animation = "fadeIn 1s ease forwards";
        box.innerHTML = messages[index];
        setTimeout(() => {
            box.style.animation = "fadeOut 1s ease forwards";
            setTimeout(() => {
                index = (index + 1) % messages.length;
                showMessage();
            }, 1000);
        }, 2800); // thời gian hiển thị mỗi câu
    }

    showMessage();
    </script>
    """, unsafe_allow_html=True)

    # Hiệu ứng pháo hoa nhẹ phía sau
    fireworks_display()

    st.markdown(
        f"""
        <p style='text-align:center; color:#00000070; font-family:Poppins,sans-serif; font-size:14px; margin-top:40px;'>
            © {datetime.now().year} | Made with 💗 for Quỳnh Trang
        </p>
        """,
        unsafe_allow_html=True
    )
