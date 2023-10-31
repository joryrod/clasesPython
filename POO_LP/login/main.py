# importar mi base de datos
from baseDatos import * # la variable usuarios de mi bd estaria disponible en este archivo

# crear clase para Usuario
# esta clase tendra los siguientes metodos

# actualizar edad del usuario
class Usuario:

    def __init__(self, dni, nombre, f_nacimiento, edad,usuario, password):
        self.dni=dni
        self.nombre=nombre
        self.f_nacimiento=f_nacimiento
        self.edad=edad
        self.usuario=usuario
        self.password=password

    def mostrar_usuario(self, ide):
        resultado=list(filter(lambda par:par['dni']==ide,usuarios))
        return f'''Aqui tienes informacion de la usuario que buscaste:
        .............................................................................................................................................................................. 
        {resultado}'''
    
    def agregar_edad(self, clave, valor):
        for usuario in usuarios:
            if usuario['dni'] == self.dni:
                usuario[clave] = valor
                return 'Se actualizó.'
        return 'Usuario no encontrado.'

# verificar si usuario esta registrado o existe en mis registros
    def verificar_usuario(self, usuario_buscar):
        for usuario in usuarios:
            if usuario['usuario'] == usuario_buscar:
                return 'Usuario registrado.'
        return 'Usuario no encontrado en los registros.'

# validar usuario y password
    def validar_usuario_password(self, usuario_a_validar, password_a_validar):
        for usuario in usuarios:
            if usuario['usuario'] == usuario_a_validar and usuario['password'] == password_a_validar:
                return 'Usuario y contraseña válidos.'
        return 'Usuario o contraseña incorrectos.'

actu=Usuario(71439102,"cristian","11/04/2004",None,"admin","xd")
print(actu.agregar_edad("edad", 17))
print(actu.mostrar_usuario(71439102))

usuario_a_buscar = "asta"
print(actu.verificar_usuario(usuario_a_buscar))
print(actu.mostrar_usuario(71439102))

usuario_a_validar = "asta"
password_a_validar = "xd"
print(actu.validar_usuario_password(usuario_a_validar, password_a_validar))
print(actu.mostrar_usuario(71439102))