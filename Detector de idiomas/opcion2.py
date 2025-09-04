import tkinter as tk
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
import langcodes

# Fijar la semilla para obtener resultados consistentes
DetectorFactory.seed = 0

# Diccionario de idiomas de la interfaz (puedes añadir más si lo deseas)
idiomas_interfaz = {
    'es': 'Español',
    'en': 'Inglés',
    'fr': 'Francés',
    'de': 'Alemán'
}

# Diccionario de textos de la interfaz
textos_interfaz = {
    'es': {
        'instrucciones': 'Ingresa el texto para detectar el idioma:',
        'boton': 'Detectar Idioma',
        'selecciona_idioma': 'Selecciona el idioma de la interfaz:'
    },
    'en': {
        'instrucciones': 'Enter text to detect language:',
        'boton': 'Detect Language',
        'selecciona_idioma': 'Select interface language:'
    },
    'fr': {
        'instrucciones': 'Entrez le texte pour détecter la langue:',
        'boton': 'Détecter la Langue',
        'selecciona_idioma': 'Sélectionnez la langue de l\'interface:'
    },
    'de': {
        'instrucciones': 'Text eingeben, um die Sprache zu erkennen:',
        'boton': 'Sprache erkennen',
        'selecciona_idioma': 'Wählen Sie die Schnittstellensprache:'
    }
}

def detectar_idioma():
    texto = entrada_texto.get("1.0", tk.END).strip()
    if texto:
        try:
            codigo_idioma = detect(texto)
            idioma_seleccionado = idioma_var.get()
            nombre_idioma = langcodes.Language.get(codigo_idioma).display_name(idioma_seleccionado)
            etiqueta_resultado.config(text=f"El idioma detectado es: {nombre_idioma}")
        except LangDetectException:
            etiqueta_resultado.config(text="No se pudo detectar el idioma. Por favor, ingresa más texto.")
        except Exception as e:
            etiqueta_resultado.config(text=f"Error: {str(e)}")
    else:
        etiqueta_resultado.config(text="Por favor, ingresa algún texto.")

def actualizar_textos(*args):
    idioma_seleccionado = idioma_var.get()
    label_instrucciones.config(text=textos_interfaz[idioma_seleccionado]['instrucciones'])
    boton_detectar.config(text=textos_interfaz[idioma_seleccionado]['boton'])
    label_idioma_interfaz.config(text=textos_interfaz[idioma_seleccionado]['selecciona_idioma'])

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Detector de Idioma")

# Crear y colocar los widgets usando grid
label_instrucciones = tk.Label(ventana)
label_instrucciones.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

entrada_texto = tk.Text(ventana, height=10, width=50)
entrada_texto.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

boton_detectar = tk.Button(ventana, command=detectar_idioma)
boton_detectar.grid(row=2, column=0, columnspan=2, pady=10)

etiqueta_resultado = tk.Label(ventana, text="", fg="blue")
etiqueta_resultado.grid(row=3, column=0, columnspan=2, pady=10)

# Añadir un selector de idioma para la interfaz
label_idioma_interfaz = tk.Label(ventana)
label_idioma_interfaz.grid(row=4, column=0, pady=10, padx=10)

idioma_var = tk.StringVar(value='es')
idioma_var.trace_add('write', actualizar_textos)
selector_idioma = tk.OptionMenu(ventana, idioma_var, *idiomas_interfaz.keys())
selector_idioma.grid(row=4, column=1, pady=10, padx=10)

# Inicializar la interfaz con los textos en español
actualizar_textos()

# Ejecutar la aplicación
ventana.mainloop()
