import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Leer el archivo CSV
canciones = pd.read_csv('data/Spotify2.csv')

# Mostrar información básica
print("Cantidad de canciones:", canciones.shape)

# Función para limpiar texto
def limpiar_texto(texto):
    return str(texto).lower().replace(",", " ").replace("-", " ").replace("  ", " ").strip()

# Crear columna 'tags' combinando texto relevante
canciones['tags'] = (
    canciones['Artist'].apply(limpiar_texto) + " " +
    canciones['Track'].apply(limpiar_texto) + " " +
    canciones['Album'].apply(limpiar_texto) + " " +
    canciones['Title'].apply(limpiar_texto)
)

# Vectorización de los textos
cv = CountVectorizer(max_features=5000, stop_words='english')
vector = cv.fit_transform(canciones['tags']).toarray()

# Calcular similitud coseno
similarity = cosine_similarity(vector)

# Función de recomendación
def recommend(titulo_cancion):
    if titulo_cancion not in canciones['Track'].values:
        return ["Canción no encontrada."]
    
    index = canciones[canciones['Track'] == titulo_cancion].index[0]
    distancias = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recomendadas = []
    for i in distancias[1:6]:  # Excluye la misma canción
        recomendadas.append(canciones.iloc[i[0]].Track)
    
    return recomendadas

# Ejemplo de uso
print("\nRecomendaciones para 'In Da Club':")
print(recommend("In Da Club"))

# Guardar el modelo y la matriz
pickle.dump(canciones, open('modelo/song_list.pkl', 'wb'))
pickle.dump(similarity, open('modelo/song_similarity.pkl', 'wb'))
print()
