def fireworks_display():
    with open("assets/fireworks.js", "r") as js_file:
        js_code = js_file.read()
    import streamlit.components.v1 as components
    components.html(f"""
    <canvas id='canvas'></canvas>
    <script>{js_code}</script>
    """, height=600)