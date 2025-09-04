import tkinter as tk
from tkinter import messagebox
import urllib.request

def check_website():
    url = entry.get()
    try:
        response = urllib.request.urlopen(url)
        status_code = response.getcode()
        if status_code == 200:
            messagebox.showinfo("Estado del sitio", f"El sitio {url} está disponible.")
        else:
            messagebox.showwarning("Estado del sitio", f"El sitio {url} no está disponible. Código de estado HTTP: {status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo acceder al sitio {url}. Error: {str(e)}")

def clear_entry():
    entry.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Comprobador de Conectividad de Sitios Web")

# Etiqueta y entrada para la URL
label = tk.Label(root, text="Ingrese la URL del sitio web:")
label.pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Botón para verificar la conectividad
button_check = tk.Button(root, text="Verificar Sitio Web", command=check_website)
button_check.pack(pady=10)

# Botón para limpiar la entrada
button_clear = tk.Button(root, text="Limpiar URL", command=clear_entry)
button_clear.pack(pady=10)

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()
