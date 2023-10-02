# averiguar sobre tkinter
# que es?
# modo de uso
# ejemplo practico -> main.py
*Tkinter* es una biblioteca de Python que se utiliza para crear interfaces gráficas de usuario (GUI, por sus siglas en inglés). Es una de las bibliotecas más comunes y ampliamente utilizadas para desarrollar aplicaciones con interfaces de usuario en Python. Tkinter proporciona una serie de herramientas y widgets (elementos de la interfaz de usuario como botones, etiquetas, cuadros de texto, etc.) que permiten crear ventanas y diálogos interactivos en aplicaciones Python de manera relativamente sencilla.

# Para usar Tkinter, generalmente sigues estos pasos:

**Importa la biblioteca:** Debes importar el módulo tkinter en tu script de Python.

> import tkinter as tk

**Crea una ventana principal:** Creas una ventana principal utilizando la clase Tk(). Esto crea la ventana principal de la aplicación.

> ventana = tk.Tk()

**Agrega widgets:** Puedes agregar diferentes widgets (botones, etiquetas, cuadros de texto, etc.) a la ventana principal utilizando métodos como **Label, Button, Entry,** etc.

> etiqueta = tk.Label(ventana, text="¡Hola, Tkinter!")

>boton = tk.Button(ventana, text="Haz clic aquí")

**Organiza los widgets:** Utiliza gestores de geometría como pack, grid o place para organizar los widgets en la ventana principal.

> etiqueta.pack()

> boton.pack()

**Ejecuta el bucle principal:** Finalmente, inicia el bucle principal de la aplicación para que la interfaz gráfica sea interactiva.

> ventana.mainloop()

**Estos son los pasos básicos para crear una aplicación simple con Tkinter. Por supuesto, puedes personalizar y ampliar tu aplicación según tus necesidades, agregando más widgets y funcionalidades.**