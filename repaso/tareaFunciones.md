# 1. averiguar funciones de python mas usadas con sus ejemplos practicos.

# **print():** 
Imprime un mensaje en la consola.

    print("Hola, mundo!")

# **input():**
Lee una línea de entrada del usuario.

    nombre = input("Por favor, ingrese su nombre: ")
    print("Hola, " + nombre)

# **len():**
 Devuelve la longitud (número de elementos) de un objeto iterable.

    lista = [1, 2, 3, 4, 5]
    print(len(lista))  # Output: 5

# **range():**
Genera una secuencia de números.

    for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# **str(), int(), float():**
Convierten a tipo de datos string, entero y flotante respectivamente.

    numero = 10
    numero_str = str(numero)
    print("El número es " + numero_str)

# **list(), tuple(), dict():**
Convierten a listas, tuplas y diccionarios respectivamente.

    lista = list(range(5))
    tupla = tuple(lista)
    diccionario = dict(zip(lista, [x**2 for x in lista]))

# **append():** 
Agrega un elemento al final de una lista.

    lista = [1, 2, 3]
    lista.append(4)
    print(lista)  # Output: [1, 2, 3, 4]

# **split():** 
Divide una cadena en una lista de subcadenas.

    cadena = "Hola, mundo"
    palabras = cadena.split(", ")
    print(palabras)  # Output: ['Hola', 'mundo']

# **join():** 
Une una lista de cadenas en una sola cadena.

    palabras = ['Hola', 'mundo']
    cadena = ', '.join(palabras)
    print(cadena)  # Output: 'Hola, mundo'

# **map():** 
Aplica una función a cada elemento de una lista.

    numeros = [1, 2, 3, 4]
    cuadrados = map(lambda x: x**2, numeros)
    print(list(cuadrados))  # Output: [1, 4, 9, 16]



# 2. averiguar sobre entornos virtuales en python
Los entornos virtuales en Python son herramientas esenciales que permiten aislar y gestionar las dependencias y versiones de los paquetes de Python para proyectos específicos. Esto es crucial para evitar conflictos entre las versiones de los paquetes utilizados en diferentes proyectos. A continuación, te proporciono una guía completa sobre entornos virtuales en Python:

## **2.1. ¿Qué es un entorno virtual?**
Un entorno virtual es un entorno de trabajo aislado que contiene su propia instalación de Python y sus propias bibliotecas. Esto permite que diferentes proyectos tengan sus propias dependencias sin interferir entre sí.

## **2.2. Ventajas de los entornos virtuales:**
# *Aislamiento:*
 Cada entorno virtual es independiente, lo que impide conflictos entre las dependencias de diferentes proyectos.

 # *Reproducibilidad:*
Garantiza que un proyecto se ejecute de la misma manera en diferentes máquinas y entornos.

# *Manejo de dependencias:* 
Permite instalar versiones específicas de paquetes para cada proyecto.

## **2.3. Creación de un entorno virtual:**
Para crear un entorno virtual, se utiliza la herramienta venv (disponible en Python 3.x por defecto):

# Crear un entorno virtual en el directorio actual
    python3 -m venv mi_entorno_virtual

Esto creará un directorio llamado mi_entorno_virtual que contiene la estructura del entorno virtual.

## **2.4. Activación y desactivación del entorno virtual:**
# *Activación (Linux/Mac):*
    source mi_entorno_virtual/bin/activate

# *Activación (Windows - PowerShell):*
    .\mi_entorno_virtual\Scripts\Activate.ps1

# *Desactivación:*
    deactivate

## **2.5. Instalación de paquetes en el entorno virtual:**
Una vez activado el entorno virtual, puedes instalar paquetes utilizando pip, que instalará las dependencias solo en el entorno actual:
    
    pip install nombre_paquete

## **2.6. Listar paquetes instalados:**
Puedes listar los paquetes instalados en el entorno virtual con:
    
    pip list

## **2.7. Exportar e importar dependencias:**
Para exportar las dependencias instaladas en un entorno virtual a un archivo:
    
    pip freeze > requirements.txt

Para instalar dependencias desde un archivo requirements.txt:

    pip install -r requirements.txt

## **2.8. Eliminar un entorno virtual:**
Simplemente elimina el directorio del entorno virtual.

## **2.9. Utilización de entornos virtuales con IDEs:**
La mayoría de los IDEs permiten seleccionar un entorno virtual para cada proyecto, asegurando que se utilicen las dependencias correctas.

## **2.10.  Virtualenv y otros gestores de entornos virtuales:**
Además de venv, existen herramientas como virtualenv y conda que proporcionan funcionalidades adicionales y flexibilidad en la creación y gestión de entornos virtuales.