import streamlit as st
from sympy import symbols, diff, integrate, sympify

def menu_ui():
    st.markdown(
        """
        <div style="text-align:center;">
            <h2 style="color:#27AE60;">🧮 Kalkulator Integral & Turunan</h2>
            <p style="color:#555;">Pilih operasi yang ingin kamu lakukan, lalu masukkan fungsi matematikanya!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.sidebar.markdown("## Menu Utama")
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

# Contoh pemanggilan fungsi menu setelah login berhasil
if 'login' not in st.session_state:
    st.session_state['login'] = False

if st.session_state['login']:
    menu_ui()
