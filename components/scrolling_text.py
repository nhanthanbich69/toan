def scrolling_message(text):
    import streamlit as st
    st.markdown(f"""
    <marquee behavior='scroll' direction='left' scrollamount='15' style='color:#FFEB3B; font-size:30px; font-weight:bold; background-color:black; padding:10px;'>
        {text}
    </marquee>
    """, unsafe_allow_html=True)
