from tkinter import *
from funciones import *

root = Tk()
root.title("calculadora")
root.geometry("296x350")
root.resizable(0,0)
#pantalla que muestre los numeros ingresados y el resultado
fuente_general=("arial",10, "bold") 
pantalla=Entry(root, 
               width=22,
               bg="#DEFFF0", #asigna color fondo 
               fg="#8F4CEF", #asigna el color de letra
               borderwidth=5, #tamaño del borde de cuadro de texto
               font=("arial", 12, "bold")) #asigna el tipo y tamaño de letra 
pantalla.grid(row=0,columnspan=4,padx=4,pady=4)
#añadir botones a la calculadora
#cursor sirve para cambiar el estilo del mause al hacer click el boton
#bg= --> color de fondo
#fg= --> color del texto
#width= --> ancho
#height= --> altura
#boton numeros
boton_1=Button(root,text="1",width=9,height=3,bg="white", fg="#402FEF",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(1,pantalla)).grid(row=1, column=0, padx=1, pady=1)
boton_2=Button(root,text="2",width=9,height=3,bg="white", fg="#402FEF",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(2,pantalla)).grid(row=1, column=1, padx=1, pady=1)
boton_3=Button(root,text="3",width=9,height=3,bg="white", fg="#402FEF",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(3,pantalla)).grid(row=1, column=2, padx=1, pady=1)
boton_4=Button(root,text="4",width=9,height=3,bg="white", fg="#402FEF",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(4,pantalla)).grid(row=2, column=0, padx=1, pady=1)
boton_5=Button(root,text="5",width=9,height=3,bg="white", fg="#402FEF",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(5,pantalla)).grid(row=2, column=1, padx=1, pady=1)
boton_6=Button(root,text="6",width=9,height=3,bg="white", fg="#402FEF",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(6,pantalla)).grid(row=2, column=2, padx=1, pady=1)
boton_7=Button(root,text="7",width=9,height=3,bg="white", fg="#402FEF",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(7,pantalla)).grid(row=3, column=0, padx=1, pady=1)
boton_8=Button(root,text="8",width=9,height=3,bg="white", fg="#402FEF",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(8,pantalla)).grid(row=3, column=1, padx=1, pady=1)
boton_9=Button(root,text="9",width=9,height=3,bg="white", fg="#402FEF",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(9,pantalla)).grid(row=3, column=2, padx=1, pady=1)
boton_0=Button(root,text="0",width=9,height=3,bg="#E8D7F0", fg="#1A4CEF",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(0,pantalla)).grid(row=4, column=1, padx=1, pady=1)

#boton igual &punto
boton_igual=Button(root,text="=",width=9,height=3,bg="#DED7F0", fg="#402FEF",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:igual(pantalla)).grid(row=4, column=0, padx=1, pady=1)
boton_punto=Button(root,text=".",width=9,height=3,bg="#E8D7F0", fg="#1A4CEF",borderwidth=0,cursor="hand2",font=fuente_general,command=lambda:enviar_boton(".",pantalla)).grid(row=4, column=2, padx=1, pady=1)

#boton de operaciones
boton_suma=Button(root,text="+",width=6,height=3,bg="#94FFF0", fg="#1A4CEF",borderwidth=1,cursor="hand2",font=fuente_general,command=lambda:operacion("+",pantalla)).grid(row=1, column=3, padx=1, pady=1)
boton_resta=Button(root,text="-",width=6,height=3,bg="#94FFF0", fg="#1A4CEF",borderwidth=1,cursor="hand2",font=fuente_general,command=lambda:operacion("-",pantalla)).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion=Button(root,text="*",width=6,height=3,bg="#94FFF0", fg="#1A4CEF",borderwidth=1,cursor="hand2",font=fuente_general,command=lambda:operacion("*",pantalla)).grid(row=3, column=3, padx=1, pady=1)
boton_division=Button(root,text="/",width=6,height=3,bg="#94FFF0", fg="#1A4CEF",borderwidth=1,cursor="hand2",font=fuente_general,command=lambda:operacion("/",pantalla)).grid(row=4, column=3, padx=1, pady=1)

#boton para eliminar toda la informacion ingresada a la pantalla
boton_borrar=Button(root, text = "CLEAR", width= 22, height = 3,bg="#EBC8F2",fg="#1A4CEF",borderwidth=4,cursor="hand2",font=fuente_general, command = lambda: borrar(pantalla)).grid(row=5, column =0, columnspan=4,padx=1, pady=1)

root.mainloop()