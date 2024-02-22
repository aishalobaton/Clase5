import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image

st.title("Interfaces Multimodales.")
image = Image.open('text_to_audio.png')

st.image(image, width=200)


try:
    os.mkdir("temp")
except:
    pass

st.subheader("Texto a audio.")
st.write('En el siguiente recuadro puedes escribir tu texto para cpnvertirlo en audio. Una vez lo tengas, '  
         'oprime convertir y luego play para poder ecucharlo. ' 
         ' Este es un ejemplo de texto que puedes utilizar:  '  
         ' Tres tristes tigres comieron trigo en un trigal. ' )
           

text = st.text_input("Ingrese el texto.")

tld="es"

def text_to_speech(text, tld):
    
    tts = gTTS(text,"es", tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text


#display_output_text = st.checkbox("Verifica el texto")

if st.button("convertir"):
    result, output_text = text_to_speech(text, tld)
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown(f"## Tú audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    #if display_output_text:
    st.markdown(f"## Texto en audio:")
    st.write(f" {output_text}")


def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)
