
#variables globales --> dentro de una funcion 

nombre=20 # variables globales
def variable():
    global nombre 
    nombre='jory' # --> variable local

print(nombre)
#variables locales --> dentro de la aplicacion