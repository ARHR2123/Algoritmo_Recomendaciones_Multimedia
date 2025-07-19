🎬🎵 Sistema de Recomendaciones Multimedia con Inteligencia Artificial

¡Hola! 👋
Bienvenido a este repositorio que contiene un Sistema de Inteligencia Artificial para Recomendaciones Multimedia, enfocado en películas y música.
Este proyecto ha sido desarrollado en Python aplicando técnicas de Machine Learning, con el objetivo de ofrecer recomendaciones personalizadas según tus elecciones en la plataforma.

🚀 Funcionalidades principales
Recomendación de películas y canciones según ítems seleccionados.

Algoritmo entrenado con similitud de contenido.

Visualización amigable a través de una interfaz construida con Streamlit.

Modelos previamente entrenados cargados para mejorar el rendimiento.

⚙️ Pasos para ejecutar el proyecto
Clona el repositorio

bash
Copiar código
git clone https://github.com/tu_usuario/tu_repositorio.git
Abre el proyecto en tu editor favorito
Por ejemplo: Visual Studio Code.

Instala las dependencias necesarias
Asegúrate de estar usando Python 3.12 para evitar errores con paquetes como pandas.
Instala los requerimientos ejecutando:

bash
Copiar código
pip install -r requirements.txt
Verifica la carpeta modelo/
Debe contener los siguientes archivos:

movie_list.pkl

similarity.pkl

song_list.pkl

song_similarity.pkl

Ejecuta el sistema de recomendaciones por consola (opcional):

bash
Copiar código
python recomendacion_peliculas.py
python recomendacion_music.py
Inicia la aplicación web con Streamlit:

bash
Copiar código
streamlit run Inicio.py
Abre el navegador y disfruta
Se abrirá automáticamente un servidor local donde podrás interactuar con la aplicación de Recomendaciones Multimedia.

💡 Notas adicionales
El sistema detectará tus elecciones y mostrará recomendaciones personalizadas con una visualización intuitiva.

Este proyecto es ideal tanto para aprender sobre sistemas de recomendación como para expandirlo con nuevas funcionalidades o tipos de contenido.

¿Te gustó este proyecto? ¡Dale una ⭐ en GitHub!
¡Gracias por visitar!

