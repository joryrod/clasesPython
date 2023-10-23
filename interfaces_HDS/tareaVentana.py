from tkinter import *

## VENTANA PRINCIPAL ##

ventana=Tk()
ventana.title("calculadorNotas")
ventana.geometry("400x500+700+100")
ventana.minsize(width=400,height=500)
ventana.configure(bg="lightblue")

## FUNCIONES ##

def convertir():
    numeros=entrada_notas.get().split()
    if len(numeros)==4:
        try:
            num1,num2,num3,num4=map(float,numeros)
            promedio=int((num1+num2+num3+num4)/4)
            rotulo_resultado.config(text=promedio)
        except ValueError:
            if entrada_notas==" ":
                rotulo_resultado.config(text="¿Dato?")
            else:
                rotulo_resultado.config(text="Error")
        finally:
            entrada_notas.config(state="disabled")
            boton_calcular.config(state="disabled")
    else:
        rotulo_resultado.config(text="sin datos")
        
def borrar():
    entrada_notas.config(state="normal")
    boton_calcular.config(state="normal")
    entrada_notas.delete(0,END),
    rotulo_resultado.config(text="")


## ROTULO DE TITULO ##

rotulo_titulo=Label(ventana,
    text="CALCULADOR DE NOTAS",
    bg="lightblue",fg="black",
    font="consolas 20 bold",
    relief=GROOVE,bd=2,
    padx=10,pady=10)
rotulo_titulo.pack(padx=20,pady=20)

## CUADROS PRIMERO ##

cuadro1=Frame(ventana,
    bg="lightblue")

rotulo_notas=Label(cuadro1,
    text="Notas:    ",
    bg="lightblue",
    font="consolas 18 bold")
rotulo_notas.pack(side=LEFT,padx=20,pady=20)

entrada_notas=Entry(cuadro1,
    bg="white",fg="black",
    font="consolas 18 bold",
    relief=SUNKEN,bd=3,
    width=10,
    justify=RIGHT,
    state="normal")
entrada_notas.pack(side=LEFT,padx=10,pady=10)
    
cuadro1.pack(pady=10)

## CUADRO SEGUNDO ##

cuadro2=Frame(ventana,
    bg="lightblue")

rotulo_calcular=Label(cuadro2,
    text="Promedio: ",
    bg="lightblue",
    font="consolas 18 bold")
rotulo_calcular.pack(side=LEFT,padx=20,pady=20)

rotulo_resultado=Label(cuadro2,
    text="",
    bg="lightgreen",
    font="consolas 18 bold",
    width=10,
    relief=GROOVE,
    anchor=E)
rotulo_resultado.pack(side=LEFT,padx=20,pady=20)

cuadro2.pack()

## CUADRO TERCERO ##

cuadro3=Frame(ventana,
    bg="lightblue")

boton_borrar=Button(cuadro3,
    text="Borrar",
    bg="grey",
    font="consolas 18 bold",
    width=10,
    command=borrar)
boton_borrar.pack(side=LEFT,padx=20,pady=20)

boton_calcular=Button(cuadro3,
    text="Calcular",
    bg="orange",
    font="consolas 18 bold",
    width=10,
    state="normal",
    command=convertir)
boton_calcular.pack(side=LEFT,padx=20,pady=20)
cuadro3.pack()


ventana.mainloop()