from tkinter import *

ventana=Tk()
ventana.title("conversor")
ventana.geometry("400x500+700+100")
ventana.minsize(width=400,height=500)
ventana.configure(bg="skyblue")

cuadro1=Frame(ventana,
    bg="lightblue")

rotulo_notas=Label(cuadro1,
    text="Notas:    ",
    bg="lightblue",
    font="consolas 18 bold")
rotulo_notas.pack(side=LEFT,padx=20,pady=20)
cuadro1.pack(pady=10)

entrada_notas=Entry(cuadro1,
    bg="white",fg="black",
    font="consolas 18 bold",
    relief=SUNKEN,bd=3,
    width=10,
    justify=RIGHT,
    state="normal")
entrada_notas.pack(side=LEFT,padx=10,pady=10)
cuadro1.pack(pady=10)
ventana.mainloop()