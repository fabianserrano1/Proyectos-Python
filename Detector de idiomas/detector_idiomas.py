import tkinter as tk
from tkinter import messagebox
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Fijar la semilla para obtener resultados consistentes
DetectorFactory.seed = 0

def detectar_idioma():
    texto = entrada_texto.get("1.0", tk.END).strip()
    if texto:
        try:
            idioma = detect(texto)
            messagebox.showinfo("Idioma Detectado", f"El idioma detectado es: {idioma}")
        except LangDetectException:
            messagebox.showerror("Error", "No se pudo detectar el idioma. Por favor, ingresa más texto.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa algún texto.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Detector de Idioma")

# Crear y colocar los widgets
label_instrucciones = tk.Label(ventana, text="Ingresa el texto para detectar el idioma:")
label_instrucciones.pack(pady=10)

entrada_texto = tk.Text(ventana, height=10, width=50)
entrada_texto.pack(pady=10)

boton_detectar = tk.Button(ventana, text="Detectar Idioma", command=detectar_idioma)
boton_detectar.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
