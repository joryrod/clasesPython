## 1. crear un programa que me pida la edad de una persona si la edad es mayor o igual a 18 que me muestre un mensaje "eres mayo de edad" caso contrario que me muestre un mensaje "eres menor de edad"
edad=int(input("ingrese su edad: "))
if edad>=18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")


## 2. una tienda comercial desea hacer un descuento del 20%, crear un programa que me determine si el cliente se hace acreedor del descuento teniendo encuenta lo siguiente, si el cliente realiza una compra de igual o mayor a 1000 soles mostrar un mensaje que diga "ganaste el descuento del 20% ahora pagaras <mostrar el totalde la compra menos el descuento>" en caso la compra no supere los 1000 soles entonces mostrar un mensaje que diga "no aplicas al descuento <mostrar el monto de la compra>"
compra=float(input("ingrese el monto de la compra: "))
if compra>=1000:
    descuento=0.20*compra
    total_pagar=compra-descuento
    print(f"""
-----------------------------------------------
  GANASTE EL DESCUENTO DEL 20% AHORA PAGARAS:       
total de la compra  : {compra}
descuento           : {descuento}
total a pagar       : {total_pagar}
-----------------------------------------------
""")
else:
    print(f"""
------------------------------------------
        NO APLICAS AL DESCUENTO
monto de la compra  : {compra}
------------------------------------------
""")

## 3. crear un programa que me pida 5 veces un nombre y cada ves que lo pida muestre la cantidad de veces que ingreso el nombre
nombres=[]
for i in range(1,6):
    nombre=input("ingrese un nobre: ")
    if nombre in nombres:
        nombres[nombre] += 1
    print(f"""
.................................
{nombre} se ingreso {i} de veces.        
.................................     
""")


## 4. crear un programa que pida un numero y lo evalue con el numero premiado si el numero ingresado es el premiado el programa finalizara si el numero ingresado es incorrecto el programa seguira pidiendo el numero premiado.
numero_premiado = 9
while True:  
    numero_ingresado = int(input("Ingresa un número: "))
    if numero_ingresado == numero_premiado:
        print(f"""
        
                      ¡Felicidades! 
              Has adivinado el número premiado.
              
""")
        break  
    else:
        print("Número incorrecto. Inténtalo de nuevo.")


## 5. crear una funcion por cada operador aritmetico que reciba 2 parametros y retorne el resultadode la operacion creando una funcion qeu imprima en consola el resultado
def suma(a,b):
    resultado=a+b
    return resultado

def resta(a,b):
    resultado=a-b
    return resultado

def multiplicacion(a,b):
    resultado=a*b
    return resultado

def division(a,b):
    resultado=a/b
    return resultado
num1=float(input("ingrese un numero: "))
num2=float(input("ingrese otro numero numero: "))
operacion=input("que tipo de operacion desea realizar: ")
if operacion== "sumar":
    resultado=suma(num1,num2)
elif operacion=="restar":
    resultado=resta(num1,num2)
elif operacion=="multiplicar":
    resultado=multiplicacion(num1,num2)
elif operacion=="dividir":
    resultado=division(num1,num2)
else:
    print("operacion no valida")
    resultado=None
if resultado is not None:
    print("El resultado es: ",resultado)

## 6. escribe una funcion que reciba un numero entero positivo y devuelva su factorial que si el resultado sea negativo muestre un error
def factorial(numero):
    if numero < 0:
        print("Error: El factorial no está definido para números negativos.")
        return None
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado
num1 = int(input("Ingrese un número entero positivo: "))
if num1 >= 0:
    resultado_factorial = factorial(num1)
    
    if resultado_factorial is not None:
        print("El factorial de", num1, "es", resultado_factorial)
else:
    print("Error: Ingrese un número entero positivo.")

## 7.escribir una funcion que reciba como parametros una lista de numeros y retorne una nueva lista con cada numero elevado al cuadrado.
def elevar_al_cuadrado(lista_numeros):
    return[numero **2 for numero in lista_numeros]
numeros = [1,2,3,4,5,6,7,8,9,10]
numeros_al_cuadrado = elevar_al_cuadrado(numeros)
print(numeros_al_cuadrado)

## 8. escribir un programa que reciba una cadena de caracteres y devuelva un objeto con cada palabra que contiene y su frecuencia.
from collections import Counter
def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia_palabras = Counter(palabras)
    return frecuencia_palabras
entrada = input("Ingrese una cadena de caracteres: ")
resultado = contar_palabras(entrada)
for palabra, frecuencia in resultado.items():
    print(f'Palabra: "{palabra}" - Frecuencia: {frecuencia}')
