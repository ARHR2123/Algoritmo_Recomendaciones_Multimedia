import os
import streamlit as st
import pickle
import requests
import pandas as pd
from dotenv import load_dotenv

# Para llamar a mi carpeta de modelos
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/estilos.css")
load_dotenv()

api_key = os.getenv("TMDB_API_KEY")

#Definimos una funcion llamada 'fetch_poster' que toma un ID de película como entrada y devuelve la URL del póster de la película.
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    # Realizamos una solicitud a la API de TMDB para obtener información sobre la película
    data = requests.get(url)
    data = data.json()  # Convertimos la respuesta a formato JSON
    poster_path = data['poster_path']  # Extraemos la ruta del póster
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path  # Construimos la URL completa del póster
    return full_path  # Devolvemos la URL del póster

# Definimos una función llamada 'recommend' que toma un título de película como entrada y devuelve una lista de títulos recomendados.
def recommend(movie_title):
    # Obtenemos el índice de la película con el título proporcionado.
    index = peliculas[peliculas['title'] == movie_title].index[0]
    
    # Obtenemos una lista de tuplas que contienen los índices y las similitudes de las películas con respecto a la película dada.
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    # Creamos una lista para almacenar los títulos recomendados.
    recommended_movie_names = []
    recommended_movie_posters = []
    
    # Iteramos sobre las distancias para obtener los títulos de las películas recomendadas.
    for i in distances[1:6]:  # Excluimos la primera película (la misma)
        movie_id = peliculas.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(peliculas.iloc[i[0]].title)
    
    return recommended_movie_names, recommended_movie_posters

st.markdown('<div class="main-title">🎬 MovieMind - Recomendador de Películas </div>', unsafe_allow_html=True)
st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
st.markdown("""
<div class="subtitulo">
    Descubre películas recomendadas al instante, según tus gustos.<br>
    Una experiencia cinematográfica personalizada al alcance de un clic.
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("assets/img/logo.png", width=350)

peliculas = pd.read_pickle('modelo/movie_list.pkl')
similarity = pd.read_pickle('modelo/similarity.pkl')

movie_list = peliculas['title'].values

# Preparar lista con opción inicial
movie_list = ['-- Seleccione la Película --'] + peliculas['title'].tolist()

selected_movie = st.selectbox("Seleccione una película que se encuentre en la lista", movie_list)

if selected_movie == '-- Seleccione la Película --':
    st.write("> Por favor, seleccione una película para continuar.")
else:
    st.write(f"> Película seleccionada: {selected_movie}")


st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)


boton_presionado = st.button('🎬 **RECOMENDAR**')

if boton_presionado:
    if selected_movie == '-- Seleccione la Película --':
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        st.warning("⚠️ Por favor, seleccione una película válida antes de solicitar recomendaciones.")
    else:
        try:
            recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

            if not recommended_movie_names:
                st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
                st.warning("⚠️ No se encontraron recomendaciones para la película seleccionada. Intenta con otra.")
            else:
                st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
                st.markdown("""
                <div class="alert-box">
                    🎯 <strong>Recomendaciones personalizadas:</strong><br>
                    Las siguientes películas han sido seleccionadas especialmente según tu elección anterior. ¡Disfrútalas! 🍿🎬
                </div>
                """, unsafe_allow_html=True)
                st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

                cols = st.columns(5)
                for i, col in enumerate(cols):
                    col.markdown(f"""
                        <div class="recommendation-card">
                            <img src="{recommended_movie_posters[i]}" width="100%">
                            <p style='text-align: center; font-weight: bold; color: white;'>{recommended_movie_names[i]}</p>
                        </div>
                    """, unsafe_allow_html=True)
        except Exception as e:
            st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
            st.error("❌ Ocurrió un error al procesar la recomendación. Verifica que la película seleccionada sea válida.")


        
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




    


