# 1. Haciendo uso de la POO crear un objeto para la entidad celular.

class Celular:
    marca="Samsung"
    color="negro"
    modelo="Galaxy S20"
    numero= 75634534
    def llamar(self, numero):
        print(f"Llamando al número {numero} desde un celular {Celular.marca} {Celular.modelo} de color {Celular.color}.")

    def enviar_mensaje(self, numero, mensaje):
        print(f"Enviando mensaje a {numero} desde un celular {Celular.marca} {Celular.modelo} de color {self.color}: {mensaje}.")

    # Crear una instancia de Celular
mi_celular = Celular("Samsung", "Galaxy S20", "Negro")

# Utilizar los métodos del objeto
mi_celular.llamar("123456789")
mi_celular.enviar_mensaje("987654321", "¡Hola! ¿Cómo estás?") 
#=================================================

# 2. Haciendo uso de la POO crear un objeto para la entidad vehiculo.
class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        print(f"El vehículo {self.marca} {self.modelo} está acelerando")

    def frenar(self):
        print(f"El vehículo {self.marca} {self.modelo} está frenando")
mi_vehiculo = Vehiculo("Toyota", "Corolla", "Rojo")

# Acceder a los atributos del objeto
print(f"Marca: {mi_vehiculo.marca}")
print(f"Modelo: {mi_vehiculo.modelo}")
print(f"Color: {mi_vehiculo.color}")
mi_vehiculo.acelerar()
mi_vehiculo.frenar()

# 3. Haciendo uso de la POO crear un objeto para la entidad avion.
class avion():

    ruedas=2

    def desplazamiento(self):
        print("El coche se esta desplazando sobre 2 ruedas")
    
miAvion=avion()

print("Mi avion tiene ", miAvion.ruedas, " ruedas")

miAvion.desplazamiento()



# 4. Haciendo uso de la POO crear un objeto para un heroe de Dota2.
# class heroe():