import tkinter as tk
from urllib.request import urlopen

def verificar_sitio(url):
  """
  Función que verifica la conectividad de un sitio web.

  Args:
    url (str): La URL del sitio web a verificar.

  Returns:
    str: Mensaje indicando si el sitio web está disponible o no.
  """
  try:
    response = urlopen(url)
    if response.status == 200:
      return f"El sitio web {url} está disponible."
    else:
      return f"Error: El sitio web {url} no está disponible (código de estado {response.status})"
  except Exception as e:
    return f"Error: No se pudo conectar al sitio web {url} ({e})"

def mostrar_resultado(resultado):
  """
  Función que muestra el resultado de la verificación en la interfaz gráfica.

  Args:
    resultado (str): El mensaje que indica el resultado de la verificación.
  """
  text_area.delete(1.0, tk.END)
  text_area.insert(tk.INSERT, resultado)

def verificar():
  """
  Función que se activa cuando el usuario hace clic en el botón "Verificar".
  """
  url = entry_url.get()
  resultado = verificar_sitio(url)
  mostrar_resultado(resultado)

def borrar_url():
  """
  Función que borra la URL del campo de entrada.
  """
  entry_url.delete(0, tk.END)

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("Comprobador de Conectividad de Sitios Web")

# Agregar etiqueta para la URL
label_url = tk.Label(ventana, text="URL del sitio web:")
label_url.pack()

# Agregar campo de entrada para la URL (más grande)
entry_url = tk.Entry(ventana, width=50)
entry_url.pack()

# Agregar botón para verificar la conexión
boton_verificar = tk.Button(ventana, text="Verificar", command=verificar)
boton_verificar.pack()

# Agregar botón para borrar la URL
boton_borrar = tk.Button(ventana, text="Borrar URL", command=borrar_url)
boton_borrar.pack()

# Agregar área de texto para mostrar el resultado
text_area = tk.Text(ventana, height=5)
text_area.pack()

ventana.mainloop()


