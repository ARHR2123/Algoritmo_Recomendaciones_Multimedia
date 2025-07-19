# 🎬🎵 Sistema de Recomendaciones Multimedia con IA

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Made with ❤️ by René Herrería](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)](https://github.com/tu_usuario)

---

## 📌 Descripción

Este es un **Sistema de Inteligencia Artificial para Recomendaciones Multimedia** que utiliza algoritmos de **Machine Learning** para sugerirte **películas** y **canciones** basadas en tus preferencias.

Desarrollado en **Python**, este proyecto aprovecha técnicas de similitud para ofrecer recomendaciones personalizadas, todo presentado mediante una interfaz web interactiva construida con **Streamlit**.

---

## 🧠 Tecnologías utilizadas

- 🐍 Python 3.12  
- 📦 Pandas, NumPy, Scikit-learn  
- 🧠 Machine Learning (Content-Based Filtering)  
- 💾 Pickle  
- 🌐 Streamlit (Interfaz web)

---

## 🚀 ¿Cómo ejecutar el proyecto?

### 1. Clona este repositorio

```bash
git clone https://github.com/ARHR2123/Algoritmo_Recomendaciones_Multimedia.git

```
### 2. Abre el proyecto en tu editor favorito
📁 Recomendado: Visual Studio Code
### 3. Instala las dependencias
Asegúrate de tener Python 3.12 instalado. Luego de aquello instala todos los paquetes que se va a utilizar en el sistema como es pandas, numpy, ast, entre otros
### 4. Ejecuta por consola

```bash
python recomendacion_peliculas.py
python recomendacion_music.py
```
### 5. Verifica la carpeta /modelo
Debe contener los siguientes archivos entrenados:

<ul>movie_list.pkl</ul>
<ul>similarity.pkl</ul>
<ul>song_list.pkl</ul>
<ul>song_similarity.pkl</ul>

### 6. Crear una cuenta en Kaggle
Kaggle: https://www.kaggle.com, y crear un API Person.

### 6. En el archivo ".env.example"
En ese archivo pegar la clave API que generó la plataforma Kaggle, esto con el fin de consumir sus datos.
Luego quitamos la extención ".example".

### 6. Inicia la aplicación web

```bash
streamlit run Inicio.py
```
### 7. ¡Listo!
Se abrirá un servidor local en tu navegador donde podrás disfrutar del sistema de recomendaciones.

### 📬 Contacto
Desarrollado por René Alejandro Herrería
<br>
📧 [alejandrorene19@gmail.com]
<br>
🔗 www.linkedin.com/in/rené-herrería-84b669307
<br>
🐙 https://github.com/ARHR2123

