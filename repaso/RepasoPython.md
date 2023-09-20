#                **DATOS**
- "a"string cadena de texto
- "hola" esto tambien es un string
-"hola soy un string y te saludo" cadena larga
*OBSERVACION: todo lo que este entre comillas es un string
"100"
"falce"
"hola"
**un string puede estar entre comillas dobles o simples** 
- 100 este es un tipo de dato numerico entero integer
- 2.1 estees un tipo de dato numerico de tipo flotante float
- falce este es un tipo de dato boleano falso
- true tipo de dato boleano verdadero

#                **VARIABLES**
es donde almacenamos nuestros tipos de datos
esos datos pueden mutar cambiar o modificarce
- como creamos una variable para almacenar nuestros datos?
1. darle un nombre significativo o relacionado al dato que estamos almacenando
2. asignarle a que dato esta asociado(proceso de asignacion) con el simbolo "="
3. indicar el tipo de dato que se va almacenar -> darle el dato a guardar

#                 **OPERADORES**
1. operadores aritmeticos:
- suma "+"
- resta "-"
- multiplicacion "*"
- divicion "/"
op=15+12+14+13/4 precedencia de operadores
suma=45+42 operador suma resultado 87
suma="45"+12 operador de concatenacion resultado 4512
saludo="hola"+"mundo" concatenacion holamundo
saludo2="hola"+" "+"mundo" concatenacion hola mundo
saludos="hola"*2 holahola

#                **DATOS ESTRUCTURADOS**
1. listas: puede almacenar distintos tipos de datos en una lista separados por comas
lista=["nombres",10,falce]
2. objetos: al igual que las listas almacenan distintos tipos de datos pero con un orden. 
para almacenar datos en un objeto necesitamos especificar un indice y un valor clave-> valor  
alumno={"nombre":"jory","edad:":"18","sexo":"todos los dias"}
- combinar ambas estructuras de datos
alumno={"nombre":"jory","edad":30,"amigos":["anthony","edwin","china"],"direcion":{"departamento":"ayacucho","provincia":"lucanas","distrito":"puquio"}}

#                **CONTROLES DE FLUJO**
- decisiones: solo se ejecutara el codigo si la condicion es verdadera, podemos hacer que si la condicion sea falsa se ejecute otro codigo.
primero espesificar el codigo que se ejecutara si cumple una condicion
if "condicion":
    el codigo que deseamos ejecutar si la condicion es verdad
    print("ejecuta esto")
aqui estamos fuera del if o del si este codigo siempre se ejecutara no depende del if
print("esto siempre se ejecutara")
si queremos que se ejecute un codigo en caso sea falso
if "condicion falsa":
    print ("solo imprime si es verdad")
else:
    print("solo imprime si es falso")
- ciclos: existen 2 tipos
1. for.- cuando sabes la cantidad de veces qye vamos a repetir.
para este caso existe el "for"
sintaxis despues de la palabra reservada "for" 
deberemos crear una variable que almacene el 
numero que iremos iterando.
luego tendremos que indicar el rango a iterar a los elementos a iterar.

ejemplo:

* vocales=[45,12,78,1,2]
* for i in vocales:
*   print(i)

cuando no sabemos la cantidad de veces a repetir

2. while.- El bucle while es otra estructura de control de flujo, concretamente lo que hace es repetir un código mientras dure una determinada condición. Se puede decir que el bucle while se utiliza para hacer algo repetidamente, bajo unas condiciones específicas, sin saber cuantas veces se repetirá.

condicion=true

while condicion

    print("hola")

    texto=input("ingresa tu nombre o salir para teminar el programa: ")

    if texto=="salir

    condicion=False

# funciones
existen 2 tipos de funciones

1. propias del lenguaje que ya vienen creadas o insertaddas en el lenguaje de python y estan listas para ser usadas.

estructura de uso de una funcion(tiene el nombre seguido de parentecis) dentro del parentecis podremos pasarle datos que necesita la funcion para ejecutarce

- **print("datos")** esta es una funcion que nos sirve para mostrar en consola datos.

- **len("dato")** esta funcion nos permite saber la longitud de una lista o un string
- **input("dato")** esta funcion se detiene a esperar que el usuario introdusca informacion.
entre parentecis podremos escribir un mensaje que indique que accion realizara el usuario.

- **max([una lista])** nos muestra el numero mayor de una lista.

- **min([lista])** nos muestra el numero menor de una lista.

- **type("numero")** funcion para convertir de un string a un numero entero.

- **str("string")** funcion para convertir de un numero entero a un string.

- **lista.append(elemento)** append es una funcion que nos permite agregar elementos al final de una lista.

- **lista.pop()** pop es una funcion de python que nos permite eliminar los elementos que se encuentran al final de la lista.

- **dato.insert("possicion", "dato a agregar")** insert es una funcion de python que nos permite agregar elementos en cualquier posicion de mi lista para eso se le tiene que pasar dos parametros, primero indicarle el indice y segundo el dato que se va agregar.

- **lista.remove(elemento a aliminar)** remove es un a funcion de python que nos permite eliminar elementos de cualquier posicion de una lista, esta funcion resibe solo el elemento que deseamos eliminar.

- **lista=cadena.split("separador de datos")** split es una funcion que nos permite dividir en una cadena.

2. **funciones propias o funciones creadas**.- 

una funcion son mini programas tambien se les conoce como modulos o fragmentos de codigo  de uso exclusivo.

pasos:

- hacer uso de pa palabra reservada "def" 
- definir un nombre de funcion que describa la tarea que va a realizar.
- establecer los parametros que resivira la funcion entre parentesis().
establecer que valor o dato va retornar mi funcion con la palabra reservada return
> **observacion**: tambien podemos hacer uso de la funcion print() para retornar un mensaje en nuestra funcion.

    def saludo():
    print("hola este es un saludo")
> como hacemos uso de la funcion?? nombre de la funcion y parentesis
    
    saludo()

> ejemplo:

    def suma(a,b):
        total=a+b
        return total
    mi_print(suma(45,12))

te imprimira en consola el resultado que es 57.

