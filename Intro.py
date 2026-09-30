import os
import streamlit as st
from PIL import Image
 
st.set_page_config(
    page_title="Bitácora de clase",
    page_icon="📒",
    layout="wide",
)
 
st.markdown(
    """
    <style>
    .hero {
        background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
        padding: 2rem 2rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 6px 18px rgba(0,0,0,0.15);
    }
    .hero h1 { margin: 0; font-size: 2.4rem; }
    .hero p  { margin: .4rem 0 0 0; opacity: .9; font-size: 1.05rem; }
    .seccion {
        font-size: 1.5rem;
        font-weight: 700;
        margin: 1.8rem 0 .8rem 0;
        padding-bottom: .3rem;
        border-bottom: 3px solid #2575fc;
        display: inline-block;
    }
    .card-title { font-size: 1.1rem; font-weight: 700; margin: .4rem 0 .2rem 0; }
    .card-desc  { font-size: .92rem; opacity: .85; min-height: 3.2rem; }
    </style>
    """,
    unsafe_allow_html=True,
)
 
ACTIVIDADES = [
    {
        "titulo": "Primer trabajo",
        "emoji": "🔊",
        "imagen": "vapoi.jpg",
        "desc": "Aplicación que convierte texto en audio.",
        "url": "https://miprimertrabajitojiijiji.streamlit.app/",
        "boton": "Texto a voz",
    },
    {
        "titulo": "Texto a código Morse (audio)",
        "emoji": "📡",
        "imagen": "morse1.png",
        "desc": "Aplicación que usa la conversión de voz a texto.",
        "url": "https://textoaaudio-e8atvrosvirkgucq7yfhqu.streamlit.app/",
        "boton": "Voz a texto",
    },
    {
        "titulo": "Traductor",
        "emoji": "🌍",
        "imagen": "trad.png",
        "desc": "Traduce tu voz o un audio a otro idioma.",
        "url": "https://traductor1-cud5mwbxqpnw9mfi4bmj2t.streamlit.app/",
        "boton": "Traductor",
    },
   
    {
        "titulo": "OCR",
        "emoji": "🔎",
        "imagen": "ocr.png",
        "desc": "Reconoce texto en imágenes y lo muestra en pantalla.",
        "url": "https://8a3mzxo4ahszf7kz2u9jwk.streamlit.app/",
        "boton": "OCR",
    },
    {
        "titulo": "OCR a Morse",
        "emoji": "📝",
        "imagen": "ocraudio.png",
        "desc": "Reconoce texto en imágenes y lo convierte a código Morse.",
        "url": "https://ocr-audio-fw4c98qxulwsqkkzzdsnau.streamlit.app/",
        "boton": "OCR a Morse",
    },
    {
        "titulo": "Entrenando modelos",
        "emoji": "🧠",
        "imagen": "reco.jpg",
        "desc": "Este modelo reconoce objetos en imagenes",
        "url": "https://l37bxo8txruhjusy2ug4sz.streamlit.app/",
        "boton": "YOLO entrenado",
    },
    {
        "titulo": "WordCloud",
        "emoji": "☁️",
        "imagen": "nube.jpg",
        "desc": "Genera una nube de palabras.",
        "url": "https://wordcloud-hbdsnmemycyswji6j2cavb.streamlit.app/",
        "boton": "WordCloud",
    },
    {
        "titulo": "Detector de sentimientos",
        "emoji": "😊",
        "imagen": "senti.jpg",
        "desc": "Ingresa un texto y te dice si es positivo, negativo o neutro.",
        "url": "https://sentiment-6fgn5um9ucappfxvluu3c3f.streamlit.app/",
        "boton": "Sentimientos",
    },
]
 
ACTIVIDADES += [
    {
        "titulo": "TDF",
        "emoji": "❓",
        "imagen": "pregunta.jpg",
        "desc": "En este enlace podras subir un texto y aparaceren preguntas con base a el",
        "url": "https://52uipfxaqbfkuwqbixdcji.streamlit.app/",
        "boton": "Abrir: TDF",
    },
    {
        "titulo": "Detector de Samuel",
        "emoji": "✨",
        "imagen": "samu.jpg",
        "desc": "En esta pagina puedes tomar una foto y detectara si esta el estudiante que realizo estas actividades en ella.",
        "url": "https://detector-de-paz-cnymgqrevh7u6rwmkrzpih.streamlit.app/",
        "boton": "Abrir: Detector",
    },
]
 
 
def mostrar_tarjeta(act):
    with st.container(border=True):
        if act["imagen"] and os.path.exists(act["imagen"]):
            st.image(Image.open(act["imagen"]), use_container_width=True)
        else:
            st.markdown(
                f"<div style='text-align:center;font-size:4rem;padding:1.2rem 0'>{act['emoji']}</div>",
                unsafe_allow_html=True,
            )
        st.markdown(
            f"<div class='card-title'>{act['emoji']} {act['titulo']}</div>",
            unsafe_allow_html=True,
        )
        st.markdown(f"<div class='card-desc'>{act['desc']}</div>", unsafe_allow_html=True)
        if act["url"]:
            st.link_button(f"Abrir: {act['boton']}", act["url"], use_container_width=True)
        else:
            st.button("Próximamente", disabled=True, use_container_width=True, key=f"d_{act['titulo']}")
 
 
def mostrar_fila(lista, por_fila=3):
    for i in range(0, len(lista), por_fila):
        cols = st.columns(por_fila)
        for col, act in zip(cols, lista[i : i + por_fila]):
            with col:
                mostrar_tarjeta(act)
 
 
with st.sidebar:
    st.header("📒 Bitácora")
    st.subheader("Actividades elaboradas a lo largo del curso")
    st.write("Diferentes actividades realizadas en clase.")
    st.divider()
    st.metric("Actividades registradas", sum(1 for a in ACTIVIDADES if a["url"]))
    st.divider()
    st.link_button(
        "🌐 Páginas y ejercicios prácticos",
        "https://sites.google.com/view/aplicacionesdeia/inicio",
        use_container_width=True,
    )
 
st.markdown(
    """
    <div class="hero">
        <h1>📒 Bitácora de las actividades en clase</h1>
        <p>Aplicaciones de Inteligencia Artificial · Proyectos y ejercicios prácticos</p>
    </div>
    """,
    unsafe_allow_html=True,
)
 
st.info(
    "En el siguiente enlace puedes encontrar páginas y ejercicios prácticos: "
    "[Abrir sitio](https://sites.google.com/view/aplicacionesdeia/inicio)",
    icon="🔗",
)
 
st.markdown("<div class='seccion'>🚀 Actividades del curso</div>", unsafe_allow_html=True)
mostrar_fila(ACTIVIDADES)
 
