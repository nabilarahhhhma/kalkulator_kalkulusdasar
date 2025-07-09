import streamlit as st
from sympy import symbols, diff, integrate, sympify

# Data user sederhana
USER = "user"
PASSWORD = "1234"

# Tambahkan gambar/logo jika ada
st.set_page_config(page_title="Kalkulator Kalkulus", page_icon="🧮", layout="centered")

def login_ui():
    st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🔒 Login Kalkulator Kalkulus</h1>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/3064/3064197.png", width=100)
    username = st.text_input("Username", placeholder="Masukkan username")
    password = st.text_input("Password", type="password", placeholder="Masukkan password")
    login_btn = st.button("Login", use_container_width=True)
    if login_btn:
        if username == USER and password == PASSWORD:
            st.session_state['login'] = True
        else:
            st.error("Username/password salah!")

def menu_ui():
    st.markdown("<h1 style='text-align: center; color: #27AE60;'>🧮 Kalkulator Integral & Turunan</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("## Menu")
    menu = st.sidebar.radio("Pilih Operasi", ["Turunan", "Integral"], index=0)
    st.sidebar.markdown("---")
    st.sidebar.info("Masukkan fungsi matematika di bawah, contoh: `x**2 + 3*x + 2`")
    fungsi_input = st.text_input("Fungsi matematika", placeholder="Contoh: x**2 + 3*x + 2")
    x = symbols('x')
    if fungsi_input:
        try:
            fungsi = sympify(fungsi_input)
            if menu == "Turunan":
                hasil = diff(fungsi, x)
                st.success(f"📝 Turunan dari `{fungsi_input}` adalah: **{hasil}**")
            else:
                hasil = integrate(fungsi, x)
                st.success(f"📝 Integral dari `{fungsi_input}` adalah: **{hasil} + C**")
        except Exception:
            st.error("Fungsi tidak valid! Pastikan penulisan benar, misal: x**2 + 3*x + 2")

# Main logic
if 'login' not in st.session_state:
    st.session_state['login'] = False

if not st.session_state['login']:
    login_ui()
else:
    menu_ui()
