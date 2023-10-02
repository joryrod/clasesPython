import tkinter as tk

# Función que muestra un mensaje cuando se presiona el botón
def mostrar_mensaje():
    mensaje_label.config(text=F"""
                     
 ¡HOLA PROFE!
      ☺            
""")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo Tkinter")

# Crear un botón
boton = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)

# Crear una etiqueta para mostrar el mensaje
mensaje_label = tk.Label(ventana, text="")

# Colocar el botón y la etiqueta en la ventana
boton.pack()
mensaje_label.pack()

# Iniciar el bucle principal de la ventana
ventana.geometry("500x500")
ventana.mainloop()


## Este código crea una ventana con un botón que dice "Mostrar Mensaje". Cuando haces clic en el botón, se llama a la función mostrar_mensaje(), que actualiza una etiqueta en la ventana con el mensaje "¡Hola, Tkinter!".