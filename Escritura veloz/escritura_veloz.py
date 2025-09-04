import tkinter as tk
import timeit
import random

# creamos un texto de referencia para que el usuario lo copie
frases = [    
    "En un lugar de la Mancha, de cuyo nombre no quiero acordarme.",
    "Tenia en su casa una ama que pasaba de los cuarenta y una sobrina que no llegaba a los veinte.",
    "Frisaba la edad de nuestro hidalgo con los cincuenta años.",
    "Los altos cielos que de vuestra divinidad divinamente con las estrellas os fortifican y os hacen merecedora.",
    "Pero, con todo, alababa en su autor aquel acabar su libro con la promesa de aquella inacabable aventura."
]

class PruebaEscritura:
    def __init__(self, root):
        self.root = root
        self.root.title("Prueba de Escritura Veloz")
        
        self.frase_actual = random.choice(frases)
        
        self.label_frase = tk.Label(root, text=self.frase_actual, wraplength=300)
        self.label_frase.pack(pady=20)
        
        self.entry_texto = tk.Entry(root, width=50)
        self.entry_texto.pack(pady=20)
        self.entry_texto.bind("<KeyPress>", self.iniciar_temporizador)
        self.entry_texto.bind("<Return>", self.terminar_prueba)
        
        self.boton_comenzar = tk.Button(root, text="Comenzar", command=self.comenzar_prueba)
        self.boton_comenzar.pack(pady=10)
        
        self.label_resultado = tk.Label(root, text="")
        self.label_resultado.pack(pady=20)
        
        self.tiempo_inicio = None
    
    def comenzar_prueba(self):
        self.frase_actual = random.choice(frases)
        self.label_frase.config(text=self.frase_actual)
        self.entry_texto.delete(0, tk.END)
        self.label_resultado.config(text="")
        self.tiempo_inicio = None
    
    def iniciar_temporizador(self, event):
        if self.tiempo_inicio is None:
            self.tiempo_inicio = timeit.default_timer()
    
    def terminar_prueba(self, event):
        tiempo_fin = timeit.default_timer()
        tiempo_total = tiempo_fin - self.tiempo_inicio
        texto_usuario = self.entry_texto.get()
        
        if texto_usuario == self.frase_actual:
            velocidad = len(texto_usuario) / tiempo_total
            self.label_resultado.config(text=f"¡Correcto! Tiempo: {tiempo_total:.2f} segundos. Velocidad: {velocidad:.2f} caracteres/segundo.") # El tiempo se cualcula cuando el texto escrito por el usuario es identido al original.
        else:
            self.label_resultado.config(text="El texto ingresado no coincide con la frase.")  # El texto tiene que ser identico, o sea acentos, mayusculas, comas y puntos.

if __name__ == "__main__":
    root = tk.Tk()
    app = PruebaEscritura(root)
    root.mainloop()
