import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

def local_css(file_name):
    with open(file_name, encoding='utf-8') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("assets/estilos2.css")


canciones = pd.read_pickle("modelo/song_list.pkl")
similarity = pd.read_pickle("modelo/song_similarity.pkl")

def recommend(song_title):
    if song_title not in canciones['Title'].values:
        return []
    index = canciones[canciones['Title'] == song_title].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recomendadas = [canciones.iloc[i[0]].Title for i in distances[1:6]]
    return recomendadas

# ------------------ Encabezado ------------------ #
st.markdown('<div class="main-title">🎧 MusicMatch - Recomendador de Canciones</div>', unsafe_allow_html=True)
st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

# ------------------ Subtítulo ------------------ #
st.markdown("""
<div class="subtitulo">
    Descubre canciones similares a tus favoritas.<br>
    Nuevos artistas, sonidos y emociones... ¡como si Spotify te leyera la mente!
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("assets/img/logoM.png", width=350)
    
st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)


# ------------------ Selectbox ------------------ #
song_list = ['-- Seleccione una Canción --'] + canciones['Title'].tolist()
selected_song = st.selectbox("🎵 Elige una canción", song_list)

if selected_song == '-- Seleccione una Canción --':
    st.write("> Por favor, selecciona una canción para comenzar.")
else:
    st.write(f"> Canción seleccionada: 🎶 **{selected_song}**")

# ------------------ Botón ------------------ #
st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

if st.button("🎶 **RECOMENDAR**"):
    recomendaciones = recommend(selected_song)
    if not recomendaciones:
        st.warning("⚠️ No se encontraron recomendaciones para la canción seleccionada.")
    else:
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        st.markdown("""
        <div class="alert-box">
            🔊 <strong>Recomendaciones basadas en tu elección:</strong><br>
            ¡Explora y disfruta!
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

        for i in range(len(recomendaciones)):
            st.markdown(f"""
                <div class="recommendation-card column">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Spotify_icon.svg" width="50">
                    <p style='margin-left: 5%;'>{recomendaciones[i]}</p>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)


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
