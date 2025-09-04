# Importamos la librerias necesarias
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto")
        self.root.geometry("800x600")
        
        self.file_path = None  # Variable para almacenar la ruta del archivo actual
        
        # Creamos el campo de texto
        self.text_area = tk.Text(self.root, wrap="word", undo=True)
        self.text_area.pack(expand=1, fill="both")
        
        # Creamos el menú
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        
        # Añadimos el menú Archivo
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Nuevo", command=self.new_file)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Guardar", command=self.save_file)
        self.file_menu.add_command(label="Guardar como...", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.root.quit)
        
        # Añadimos el menú Editar
        self.edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Editar", menu=self.edit_menu)
        self.edit_menu.add_command(label="Deshacer", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Rehacer", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cortar", command=lambda: self.text_area.event_generate("<<Cut>>"))
        self.edit_menu.add_command(label="Copiar", command=lambda: self.text_area.event_generate("<<Copy>>"))
        self.edit_menu.add_command(label="Pegar", command=lambda: self.text_area.event_generate("<<Paste>>"))
        
        # Añadir el menú Ayuda
        self.help_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Ayuda", menu=self.help_menu)
        self.help_menu.add_command(label="Acerca de", command=self.show_about)
        
    def new_file(self):
        self.file_path = None
        self.text_area.delete(1.0, tk.END)
        self.root.title("Editor de Texto")
    
    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", 
                                               filetypes=[("Archivos de Texto", "*.txt"), 
                                                          ("Todos los archivos", "*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, content)
                    self.file_path = file_path
                    self.root.title(f"Editor de Texto - {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")
    
    def save_file(self):
        if self.file_path:
            try:
                with open(self.file_path, "w") as file:
                    content = self.text_area.get(1.0, tk.END)
                    file.write(content)
                    messagebox.showinfo("Guardar", "Archivo guardado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
        else:
            self.save_file_as()
    
    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                 filetypes=[("Archivos de Texto", "*.txt"), 
                                                            ("Todos los archivos", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    content = self.text_area.get(1.0, tk.END)
                    file.write(content)
                    self.file_path = file_path
                    self.root.title(f"Editor de Texto - {file_path}")
                    messagebox.showinfo("Guardar", "Archivo guardado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
    
    def show_about(self):
        messagebox.showinfo("Acerca de", "Editor de Texto creado con Tkinter en Python.")

# Se crea la ventana principal
root = tk.Tk()
editor = TextEditor(root)
root.mainloop()
