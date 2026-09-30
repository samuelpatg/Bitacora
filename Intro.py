import streamlit as st
from PIL import Image
st.title("Bitacora de las actividades en clase.")

with st.sidebar:
  st.subheader("Actividades elaboradas a lo largo del curso")
  parrafo = (
    "Diferentes actividades realizadas en clase"
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Primer trabajo")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En el siguiente enlace usaremos una de las aplicaciones que convierte texto en audio") 
 url = "https://miprimertrabajitojiijiji.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Reconocimiento de Objetos")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos una app que nos permite detectar objetos en Imágenes.") 
 url = "https://l37bxo8txruhjusy2ug4sz.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Entrenando Modelos")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Conversión de Texto a Código Morse (Audio)")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En el siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://textoaaudio-e8atvrosvirkgucq7yfhqu.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("OCR")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En el siguiente enlace veremos una app que reconoce texto de imagenes y lo convierte a texto en tu pantalla.") 
 url = "https://8a3mzxo4ahszf7kz2u9jwk.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("WordCloud")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace podremos realizar una nube de palabras.") 
 url = "https://wordcloud-hbdsnmemycyswji6j2cavb.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Traductor")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En el siguiente link podras traudcir tu voz o un audio a otro idioma.") 
 url = "https://traductor1-cud5mwbxqpnw9mfi4bmj2t.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("OCR a morse")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos una aplicación que reconoce  el texto en imagenes y convertir ese texto en codigo morse.") 
 url = "https://ocr-audio-fw4c98qxulwsqkkzzdsnau.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Detector de sentimientos")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente pagina podremos ingresar algun sentimiento y nos dira si es negativo, positivo o neutro, y nos mostrara una representacion.") 
 url = "https://sentiment-6fgn5um9ucappfxvluu3c3f.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")


