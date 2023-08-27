'''La idea de este proyecto es convertir un artículo existente en un archivo de audio reproducible 
en formato mp3. Para ello puedes hacer uso de bibliotecas existenes como nltk (kit de 
herramientas de lenguaje natural), newspaper3k y gtts (puedes seguir las instrucciones de 
instalación de pip).
Puedes crear un programa al que proporcionarle una URL de un artículo a convertir para 
luego manejar la conversión de texto a voz'''

from newspaper import Article
from gtts import gTTS

def obtener_urls(file):
    '''Función para obtener la url del artículo de una hoja de texto'''
    with open(file, 'r') as archivo:
    # Lee todo el contenido del archivo
        urls = archivo.readlines()
    return urls

def convertir_texto_a_voz(texto):
    '''Función para convertir texto a voz utilizando gtts'''
    audio = gTTS(texto, lang="es-us")
    return audio


#Determinamos el archivo de donde se leerá el url para no escribirlo en código
file = "url_articulo.txt"

#obtenemos las urls
urls = obtener_urls(file)

for url in urls:
    articulo = Article(url)
    articulo.download()
    articulo.parse()
    contenido_articulo = articulo.text
    audio = convertir_texto_a_voz(contenido_articulo)
    audio.save("articulo_"+ articulo.title[0:20] +".mp3")

















