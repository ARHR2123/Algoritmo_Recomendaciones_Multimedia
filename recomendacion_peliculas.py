import pandas as pd # Sirve para leer y manipular datos
import numpy as np # Sirve para realizar operaciones matemáticas
pd.set_option('display.max_columns', None) # Muestra todas las columnas de un DataFrame
import ast #Convertir cadenas de texto a listas
# Importamos la clase 'CountVectorizer' del modulo 'feature_extraction.text' de la biblioteca 'sklearn'.
from sklearn.feature_extraction.text import CountVectorizer 
# Importamos la clase 'cosine_similarity' del módulo 'metrics.pairwise' de la biblioteca 'sklearn', para calcular la similitud entre vectores.
from sklearn.metrics.pairwise import cosine_similarity
import pickle # Sirve para serializar y deserializar objetos en un archivo binario


# Insertar los archivos planos que contiene las películas

peliculas = pd.read_csv('data/peliculas.csv')
creditos = pd.read_csv('data/creditos.csv', encoding='utf-8')

# Ver cuantas columnas y cuantas filas tiene cada archivo plano
print()
print('Cantidad de Películas: \n')
print(peliculas.shape)
peliculas.head(1)
print()
print('Cantidad de Créditos: \n')
print(creditos.shape)
creditos.head(1)

print()

# Unir las bases de datos por el título de la película
peliculas = peliculas.merge(creditos, on='title')

# Borrar valores nulos
peliculas.dropna(inplace=True)

# Verificación de las dos bases de datos unidas
peliculas.head(2)

# Seleccionar las columnas relevantes para visualizar
peliculas = peliculas[['movie_id','title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

# Visualización de la matriz que ya estén unidas las dos bases de datos
peliculas.head(1)

# Convertimos las columnas de texto a listas, ya que se encuentra en formato json
def convertir_a_lista(texto):
    listaName=[] # Creamos una lista vacía para almacenar los valores extraidos en formato json.
    for i in ast.literal_eval(texto): # Iteramos sobre el texto convertido a lista
        listaName.append(i['name']) # Agregamos el nombre de cada elemento a la lista
    return listaName # Devolvemos la lista

# La funcion ast.literal_eval() convierte una cadena de texto que representa una lista en una lista real de Python.

# Al revisar la documentación vemos que el archivo 'películas' es un DataFrame de Pandas, por lo que podemos aplicar la función a las columnas correspondientes.
# La intención es convertir las columnas 'genres', 'keywords', 'cast' y 'crew' de cadenas de texto json a listas.

# Se aplica la funcion 'convertir_a_lista' a cada elemento de la columna 'genres/keywords' utilixando el método 'apply'.
peliculas['genres'] = peliculas['genres'].apply(convertir_a_lista)
peliculas['keywords'] = peliculas['keywords'].apply(convertir_a_lista)

# Despues de aplicar la función convertir_a_lista, las columnas 'cast' y 'crew' contienen listas de diccionarios, de la cual tambien debemos transformarlo.
# Se espera que la columna 'genres' contenga una lista de nombres extraidos de los diccionarios en la columna 'cast' y 'crew', para compararlos y sacar referente a los generos los directores.

# Visualizamos que se haya aplicado los cambios
peliculas.head(2)

# Un breve ejemplo de como se ve la columna 'genres' después de aplicar la función convertir_a_lista

ast.literal_eval('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]')

# Se define una función llamada 'convertName' que toma un texto como entrada y devuelve una lista de nombres extraídos de los diccionarios en la columna 'cast' o 'crew'.
def convertName(texto):
    listaName = []  # Creamos una lista vacía para almacenar los valores extraídos en formato json.
    counter = 0  # Inicializamos el contador
    for i in ast.literal_eval(texto):  # Iteramos sobre el texto convertido a lista
        if counter < 3:
            listaName.append(i['name'])  # Agregamos el nombre de cada elemento a la lista
        counter += 1  # Incrementamos el contador
    return listaName  # Devolvemos la lista

# Esta función 'convertName' está diseñada para extraer los nombres de los primeros tres elementos en una lista de diccionarios.
# Si el contador excede 3, los elementos restantes no se agregaran a la lista 'listaName'

# Aquí ya se aplicarán los cambios donde se visualizaran los nombres de los primeros tres elementos en la lista de diccionarios de las columnas 'cast'
peliculas['cast'] = peliculas['cast'].apply(convertName)
peliculas.head(2)

peliculas['cast']= peliculas['cast'].apply(lambda x: x[0:3])  # Limitar a los primeros 3 actores
peliculas.head(2)

# Definimos una funcion llamada 'fetch_director' que toma un texto como entrada y devuelve el nombre del director.

def fetch_director(texto):
    listaName = []  # Creamos una lista vacía para almacenar los valores extraídos en formato json.
    for i in ast.literal_eval(texto):  # Iteramos sobre el texto convertido a lista
        if i['job'] == 'Director':  # Verificamos si el trabajo es 'Director'
            listaName.append(i['name'])  # Agregamos el nombre del director a la lista
    return listaName  # Devolvemos la lista

# Aplicamos la funcion 'fetch_director' a la columna 'crew' para extraer el nombre del director de cada película.

peliculas['crew'] = peliculas['crew'].apply(fetch_director)
peliculas.sample(2)

# Aplicamos una operación a la columna 'overview' de la tabla 'peliculas' utilizando el método 'apply' para convertir cada elemento en una cadena de texto.
peliculas['overview'] = peliculas['overview'].apply(lambda x:x.split())
peliculas.sample(2)

# Definimos una función llamada 'collapse' que toma una lista como entrada y devuelve una cadena de texto unida por espacios.
# En este paso como los generos y las otras columnas cada palabra esta separada por ',', de la cual ahora la vamos a unir en un solo texto.
def collapse(listaName):
    listaDescripcion = []  # Creamos una lista vacía para almacenar los valores extraídos en formato json.
    for i in listaName:
        listaDescripcion.append(i.replace(" ", ""))  # Eliminamos los espacios en blanco de cada elemento
    return listaDescripcion # Devolvemos la lista listaDescripcion

# Devolvemos una nueva lista con los elementos transformados

peliculas['cast'] = peliculas['cast'].apply(collapse)
peliculas['crew'] = peliculas['crew'].apply(collapse)
peliculas['genres'] = peliculas['genres'].apply(collapse)
peliculas['keywords'] = peliculas['keywords'].apply(collapse)
peliculas.head(2)

# Creamos una columna tags para pasar toda la informacion

peliculas['tags'] = peliculas['overview'] + peliculas['genres'] + peliculas['keywords'] + peliculas['cast'] + peliculas['crew']
peliculas.head(2)

# Eliminamos las columnas que ya no son necesarias
new = peliculas.drop(columns=['overview', 'genres', 'keywords', 'cast', 'crew'])
new.head(2)

# Unir los elementos con espacios y que sea una sola frase

new['tags'] = new['tags'].apply(lambda x: " ".join(x))
new.head(2)

# CREACION DEL MODELO ML

# Creamos una instancia de 'CountVectorizer' con el parámetro 'stop_words' establecido en 'english'.
cv = CountVectorizer(max_features=5000, stop_words='english')


# Transformamos todas las palabras en números ya que el Maching Learning trabaja con números.

# Utilizamos el objeto 'cv' para transformar la columna 'tags' del DataFrame 'new' en una matriz de características.
vector = cv.fit_transform(new['tags']).toarray()

vector.shape

#La funcion 'cosine_similarity' calcula la similitud del coseno entre los vectores de características.
similarity = cosine_similarity(vector)

# va a comparar que tan similares son las películas entre sí, dependiendo la película de selección

similarity

# Para comprobar si está funcionando correctamente y ver que indice me manda, ya transformado en números
new[new['title'] == 'The Lego Movie'].index[0]

# Supongamos que 'new' es una tabla de datos que contiene información sobre películas, y queremos encontrar las películas más similares a una película específica, en este caso, "The Lego Movie".
# Definimos una función llamada 'recommend' que toma un título de película como entrada y devuelve una lista de títulos recomendados.
def recommend(peliculas):
    
    # Obtenemos el índice de la película con el título proporcionado.
    index = new[new['title'] == peliculas].index[0]
    
    # Obtenemos una lista de tuplas que contienen los índices y las similitudes de las películas con respecto a la película dada.
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    # Creamos una lista para almacenar los títulos recomendados.
    recommended_movies = []
    
    # Iteramos sobre las distancias para obtener los títulos de las películas recomendadas.
    for i in distances[1:6]:  # Excluimos la primera película (la misma), para que no me cuente la primera.
        recommended_movies.append(new.iloc[i[0]].title)
    
    return recommended_movies  # Devolvemos la lista de títulos recomendados.

# Probamos la función 'recommend' con el título de una película específica. En este ejemplo vamos ha usar esta.

print('> Recomendación de la Película "Avatar" son: \n ',recommend('Avatar'))
print()

# Guardamos el modelo de similitud en un archivo utilizando pickle.
pickle.dump(new, open('modelo/movie_list.pkl', 'wb'))

# Guardamos la matriz de similitud en un archivo utilizando pickle.
# El modo 'wb' indica que el archivo se abrirá en modo escritura binaria.
pickle.dump(similarity, open('modelo/similarity.pkl', 'wb'))

# Estos pasos guardan el DataFrame 'new' y la matriz de similitud 'similarity' en archivos llamados 'movie_list.pkl' y 'similarity.pkl', respectivamente.
# Estos archivos se pueden cargar más tarde para realizar recomendaciones sin necesidad de volver a procesar los datos.

peliculas=pickle.load(open('modelo/movie_list.pkl', 'rb'))