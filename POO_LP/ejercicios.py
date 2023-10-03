# 1. Haciendo uso de la POO crear un objeto para la entidad celular.

# class Celular:
#     marca="Samsung"
#     color="negro"
#     modelo="Galaxy S20"
#     numero= 75634534
#     def llamar(self, numero):
#         print(f"Llamando al número {numero} desde un celular {Celular.marca} {Celular.modelo} de color {Celular.color}.")

#     def enviar_mensaje(self, numero, mensaje):
#         print(f"Enviando mensaje a {numero} desde un celular {Celular.marca} {Celular.modelo} de color {self.color}: {mensaje}.")

#     # Crear una instancia de Celular
# mi_celular = Celular("Samsung", "Galaxy S20", "Negro")

# # Utilizar los métodos del objeto
# mi_celular.llamar("123456789")
# mi_celular.enviar_mensaje("987654321", "¡Hola! ¿Cómo estás?") 
# #=================================================

# # 2. Haciendo uso de la POO crear un objeto para la entidad vehiculo.
# class Vehiculo:
#     def __init__(self, marca, modelo, color):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color

#     def acelerar(self):
#         print(f"El vehículo {self.marca} {self.modelo} está acelerando")

#     def frenar(self):
#         print(f"El vehículo {self.marca} {self.modelo} está frenando")
# mi_vehiculo = Vehiculo("Toyota", "Corolla", "Rojo")

# # Acceder a los atributos del objeto
# print(f"Marca: {mi_vehiculo.marca}")
# print(f"Modelo: {mi_vehiculo.modelo}")
# print(f"Color: {mi_vehiculo.color}")
# mi_vehiculo.acelerar()
# mi_vehiculo.frenar()

# # 3. Haciendo uso de la POO crear un objeto para la entidad avion.
# class avion():

#     ruedas=2

#     def desplazamiento(self):
#         print("El coche se esta desplazando sobre 2 ruedas")
    
# miAvion=avion()

# print("Mi avion tiene ", miAvion.ruedas, " ruedas")

# miAvion.desplazamiento()



# 4. Haciendo uso de la POO crear un objeto para un heroe de Dota2.
# class HeroeDota2:
#     def __init__(self,nombre,atributo,rol):
#         self.nombre="antimage"
#         self.atributo="agilidad"
#         self.rol="carry"

#     def atacar(self):
#         print(f"El heroe {self.nombre} de {self.atributo} está atacando")

#     def defender(self):
#         print(f"El heroe {self.nombre} de {self.atributo} está defendiendo")
# heroe=HeroeDota2 ("antimage","agilidad","carry")

# # Acceder a los atributos del objeto
# print(f"nombre: {heroe.nombre}")
# print(f"atributo: {heroe.atributo}")
# print(f"rol: {heroe.rol}")
# heroe.atacar()
# heroe.defender()




## 5. haciendo uso de la poo crear un obgeto para una pc
# class pc:
#     def __init__(self,monitor,procesador,teclado,mouse):
#         self.monitor="sansung"
#         self.procesador="gigabyte"
#         self.teclado="genius"
#         self.mouse="genius"

#     def prender(self):
#         print(f"La pc {self.monitor} de procesador {self.procesador} se esta encendiendo")

#     def apagar(self):
#         print(f"La pc {self.monitor} de procesador {self.procesador} se esta apagando")
# compu=pc ("sansung","gigabyte","genius","genius")

# # Acceder a los atributos del objeto
# print(f"monitor: {compu.monitor}")
# print(f"procesador: {compu.procesador}")
# print(f"teclado: {compu.teclado}")
# print(f"mouse: {compu.mouse}")
# compu.prender()
# compu.apagar()



## 6. haciendo uso de la poo crear un obgeto para una impresora
# class epson:
#     def __init__(self,marca,modelo,serie):
#         self.marca="Eppson"
#         self.modelo="multifuncional"
#         self.serie="L3110"

#     def imprimir(self):
#         print(f"La impresora {self.marca} {self.serie} esta imprimiendo")
#     def copiar(self):
#         print(f"La impresora {self.marca} {self.serie} esta fotocopiando")
#     def escanear(self):
#         print(f"La impresora {self.marca} {self.serie} esta Escaneando")
# impresora=epson("Eppson","multifuncional","L3110")

# print(f"marca: {impresora.marca}")
# print(f"procesador: {impresora.modelo}")
# print(f"teclado: {impresora.serie}")
# impresora.imprimir()
# impresora.copiar()
# impresora.escanear()



## 7. haciendo uso de la poo crear un obgeto para emitir una factura
class epson:
    def __init__(self,monto,cantidad,precio_unitario,total):
        self.monto=input("ingrese el monto comprado: ")
        self.cantidad=input("ingrese la cantidada comprar: ")
        self.precio_unitario=input("ingrese el precio unitario: ")
        self.total=total_a_pagar
    def imprimir(self):
        print(f"La impresora {self.marca} {self.serie} esta imprimiendo")
    def copiar(self):
        print(f"La impresora {self.marca} {self.serie} esta fotocopiando")
    def escanear(self):
        print(f"La impresora {self.marca} {self.serie} esta Escaneando")
impresora=epson("Eppson","multifuncional","L3110")

print(f"marca: {impresora.marca}")
print(f"procesador: {impresora.modelo}")
print(f"teclado: {impresora.serie}")
impresora.imprimir()
impresora.copiar()
impresora.escanear()