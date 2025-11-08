import streamlit as st
from datetime import datetime
from components.fireworks_html import fireworks_display
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Quỳnh Trang 🎂", page_icon="🎉")

# Clear cache mỗi lần reload
st.cache_data.clear()
st.cache_resource.clear()

query_params = st.experimental_get_query_params()
is_open = query_params.get("open", ["false"])[0].lower() == "true"

placeholder = st.empty()

if not is_open:
    with placeholder:
        components.html("""
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
        body {
            background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
            font-family: 'Poppins', sans-serif;
            margin: 0;
            height: 100vh;
            overflow: hidden;
            text-align: center;
        }
        .envelope-emoji { font-size: 90px; animation: float 2.5s ease-in-out infinite; }
        @keyframes float { 0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)} }
        .envelope-text {
            font-size: clamp(16px, 4vw, 22px);
            color: white;
            background: rgba(255,255,255,0.2);
            padding: 10px 25px;
            border-radius: 25px;
            display: inline-block;
        }
        </style>

        <div id="envelope-stage" style="margin-top:35vh;">
            <button onclick="window.location.href='?open=true&v='+new Date().getTime()"
                style="background:none;border:none;cursor:pointer;">
                <div class="envelope-emoji">💌</div>
                <div class="envelope-text">Bấm để mở 🎁</div>
            </button>
        </div>
        """, height=800)

else:
    placeholder.empty()  # xoá phần cũ
    fireworks_display()
    components.html("""
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    body {
        background: linear-gradient(120deg, #ffecd2 0%, #fcb69f 100%);
        font-family: 'Poppins', sans-serif;
        margin: 0;
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
        animation: fadeIn 1s ease forwards;
    }
    @keyframes fadeIn { from{opacity:0;transform:translateY(20px)} to{opacity:1;transform:translateY(0)} }
    @keyframes fadeOut { from{opacity:1} to{opacity:0;transform:translateY(-20px)} }
    </style>

    <div class="message-box" id="message-stage"></div>
    <script>
    const messages = [
        "Hôm nay nhân ngày kỉ niệm 2 thập kỉ và 2 năm ngày bạn Chang xuất hiện 💫",
        "Tớ chúc cậu luôn luôn hạnh phúc và yêu đời 💖",
        "Cậu lúc nào cũng xinh hết 🌸",
        "🎉 HAPPY BIRTHDAY QUỲNH TRANG 💗"
    ];
    const box = document.getElementById("message-stage");
    let index = 0;
    function showMessage() {
        box.style.animation = "fadeIn 1s ease forwards";
        box.innerHTML = messages[index];
        setTimeout(() => {
            box.style.animation = "fadeOut 1s ease forwards";
            setTimeout(() => {
                index++;
                if (index < messages.length) showMessage();
                else { box.style.animation = "fadeIn 1s ease forwards"; box.innerHTML = messages[messages.length - 1]; }
            }, 1000);
        }, 2800);
    }
    showMessage();
    </script>
    """, height=800)

    st.markdown(
        f"<p style='text-align:center;color:#00000070;font-family:Poppins;font-size:14px;margin-top:40px;'>© {datetime.now().year} | Made with 💗 for Quỳnh Trang</p>",
        unsafe_allow_html=True
    )
