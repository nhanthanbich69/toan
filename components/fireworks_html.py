import streamlit as st
import os

def fireworks_display():
    # Đường dẫn tuyệt đối tới file assets
    base_path = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(base_path, "..", "assets")

    # Đọc file JS và CSS
    with open(os.path.join(assets_dir, "fireworks.js"), "r", encoding="utf-8") as js_file:
        fireworks_js = js_file.read()

    with open(os.path.join(assets_dir, "style.css"), "r", encoding="utf-8") as css_file:
        style_css = css_file.read()

    html_code = f"""
    <style>{style_css}</style>

    <canvas id="canvas"></canvas>

    <script>{fireworks_js}</script>
    """

    st.components.v1.html(html_code, height=0)
