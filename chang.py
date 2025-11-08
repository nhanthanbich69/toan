import streamlit as st
from datetime import datetime
from components.fireworks_html import fireworks_display
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Quỳnh Trang 🎂", page_icon="🎉")

# 👉 FIX: Dùng API cũ để đảm bảo tương thích cloud
query_params = st.experimental_get_query_params()
is_open = query_params.get("open", ["false"])[0].lower() == "true"

# --- Nếu chưa mở thư ---
if not is_open:
    components.html("""
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    body {
        background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
        font-family: 'Poppins', sans-serif;
        margin: 0;
        padding: 0;
        height: 100vh;
        overflow: hidden;
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
        font-size: clamp(16px, 4vw, 22px);
        color: white;
        background: rgba(255,255,255,0.2);
        padding: 10px 25px;
        border-radius: 25px;
        display: inline-block;
        backdrop-filter: blur(6px);
    }

    button {
        background: none;
        border: none;
        cursor: pointer;
    }
    </style>

    <div class="envelope-container">
        <button onclick="window.location.href='?open=true'">
            <div class="envelope-emoji">💌</div>
            <div class="envelope-text">Bấm để mở 🎁</div>
        </button>
    </div>
    """, height=800)

# --- Nếu đã mở thư ---
else:
    fireworks_display()
    components.html("""
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    body {
        background: linear-gradient(120deg, #ffecd2 0%, #fcb69f 100%);
        font-family: 'Poppins', sans-serif;
        margin: 0;
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
        padding: 20px;
        max-width: 90%;
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
                index++;
                if (index < messages.length) {
                    showMessage();
                } else {
                    box.style.animation = "fadeIn 1s ease forwards";
                    box.innerHTML = messages[messages.length - 1];
                }
            }, 1000);
        }, 2800);
    }

    showMessage();
    </script>
    """, height=800)

    st.markdown(
        f"""
        <p style='text-align:center; color:#00000070; font-family:Poppins,sans-serif; font-size:14px; margin-top:40px;'>
            © {datetime.now().year} | Made with 💗 for Quỳnh Trang
        </p>
        """,
        unsafe_allow_html=True
    )
