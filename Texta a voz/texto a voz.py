from newspaper import Article
import nltk
import os
from gtts import gTTS
from langdetect import detect, LangDetectException

# Descargar recursos necesarios de nltk
nltk.download('punkt')

def extract_article_text(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article.text

def detect_language(text):
    try:
        return detect(text)
    except LangDetectException:
        return None

def text_to_speech(text, output_file, language='es'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)

def get_user_choice(prompt, choices):
    while True:
        choice = input(prompt).strip().lower()
        if choice in choices:
            return choice
        print(f"Opción no válida. Por favor elige una de las siguientes: {', '.join(choices)}")

def main():
    choice = get_user_choice("¿Quieres leer desde una URL (u) o ingresar el texto manualmente (t)? ", ['u', 't'])

    if choice == 'u':
        url = input("Introduce la URL del artículo: ").strip()
        print("Extrayendo el texto del artículo...")
        text = extract_article_text(url)
    elif choice == 't':
        print("Introduce el texto que quieres convertir a voz. Pulsa Enter dos veces para finalizar:")
        text_lines = []
        while True:
            line = input()
            if line:
                text_lines.append(line)
            else:
                break
        text = '\n'.join(text_lines)

    # Detectar automáticamente el idioma del texto
    detected_language = detect_language(text)
    if detected_language:
        print(f"Idioma detectado: {detected_language}")
    else:
        print("No se pudo detectar el idioma del texto. Usando 'es' por defecto.")
        detected_language = 'es'

    # Permitir al usuario seleccionar el idioma o usar el detectado
    language = input(f"Elige el idioma para la lectura (es, en, fr, etc.) o presiona Enter para usar el detectado ({detected_language}): ").strip().lower()
    if not language:
        language = detected_language

    output_file = input("Introduce el nombre del archivo de salida (con .mp3): ").strip()
    if not output_file.endswith('.mp3'):
        output_file += '.mp3'

    print("Convirtiendo el texto a voz...")
    try:
        text_to_speech(text, output_file, language)
        print(f"Archivo de audio guardado como {output_file}")
    except Exception as e:
        print(f"Error al convertir el texto a voz: {e}")

if __name__ == "__main__":
    main()




