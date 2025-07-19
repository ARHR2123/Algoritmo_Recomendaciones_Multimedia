import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

def local_css(file_name):
    with open(file_name, encoding='utf-8') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("assets/estilosP.css")

# ------------------ Encabezado ------------------ #
st.markdown('<div class="main-title">🎬✨ Bienvenido a MediaMatch, donde tus gustos crean la historia.</div>', unsafe_allow_html=True)
st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

# ------------------ Subtítulo ------------------ #

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("assets/img/logoh.png", width=250)

st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

st.markdown("""
<div class="subtitulo">
    Déjate sorprender por una inteligencia que entiende tu mundo y te guía hacia el contenido que realmente conecta contigo.
</div>
""", unsafe_allow_html=True)

# ------------------ Sidebar ------------------ #
with st.sidebar:
    st.markdown("""
        <div style='text-align: center;'>
            <h2 style='color: #1DB954; margin-bottom: 0;'>✨ MediaMatch</h2>
            <h4 style='color: white; font-weight: normal; margin-top: 5px;'>Encuentra la canción perfecta</h4>
        </div>
    """, unsafe_allow_html=True)

    st.image("assets/img/logoh.png", use_container_width=True)

    st.markdown("---")

    st.markdown("""
    <div style='text-align: center; color: gray; font-size: 0.9em; margin-top: 20px;'>
        🎼 Versión 1.0 • Proyecto musical<br>
        👨‍💻 Desarrollado por: Ing. René Herrería
    </div>
    """, unsafe_allow_html=True)
