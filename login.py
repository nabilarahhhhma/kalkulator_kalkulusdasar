import streamlit as st

# Data user sederhana
USER = "bila"
PASSWORD = "cantik"

def login_ui():
    st.markdown(
        """
        <div style="text-align:center;">
            <img src="https://cdn-icons-png.flaticon.com/512/3064/3064197.png" width="100"/>
            <h2 style="color:#2E86C1;">Selamat Datang di Kalkulator Kalkulus</h2>
            <p style="color:#555;">Silakan login untuk melanjutkan</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")  # Spasi
    username = st.text_input("Username", placeholder="Masukkan username")
    password = st.text_input("Password", type="password", placeholder="Masukkan password")
    login_btn = st.button("Login", use_container_width=True)
    if login_btn:
        if username == USER and password == PASSWORD:
            st.session_state['login'] = True
        else:
            st.error("Username atau password salah! Coba lagi.")

# Inisialisasi status login
if 'login' not in st.session_state:
    st.session_state['login'] = False

if not st.session_state['login']:
    login_ui()
else:
    st.success("Login berhasil! Silakan lanjut ke menu kalkulator.")
