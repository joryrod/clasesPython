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



## 7. Haciendo uso de la POO crear un objeto para emitir una factura.
# class Factura:
#     def __init__(self, numero, fecha, cliente, total):
#         self.numero = numero
#         self.fecha = fecha
#         self.cliente = cliente
#         self.total = total

#     def mostrar_informacion(self):
#         print("Número de factura:", self.numero)
#         print("Fecha:", self.fecha)
#         print("Cliente:", self.cliente)
#         print("Total:", self.total)


# # Crear un objeto para una factura
# mi_factura = Factura("F0001", "01/05/2022", "Cliente A", 150.50)

# # Mostrar la información de la factura
# mi_factura.mostrar_informacion()


## 8.crear un objeto laptop con dos atributos de clase y 5 atributos de instancia devera tener hasta 3 funcionalidades como minimo.

# class Laptop:
#     marca = "Desconocida"
#     sistema_operativo = "Desconocido"
#     def __init__(self, modelo, pantalla, procesador, memoria, almacenamiento):
#         self.modelo = modelo
#         self.pantalla = pantalla
#         self.procesador = procesador
#         self.memoria = memoria
#         self.almacenamiento = almacenamiento
#     def encender(self):
#         return f"{self.modelo} está encendida."
#     def apagar(self):
#         return f"{self.modelo} está apagada."
#     def mostrar_informacion(self):
#         return f"Modelo:{self.modelo},Pantalla:{self.pantalla},Procesador:{self.procesador},Memoria:{self.memoria},Almacenamiento:{self.almacenamiento}"
# miLaptop=Laptop("lenovo","15.6 pulgadas","Intel Core i7","16 GB RAM","512 GB SSD")
# print(miLaptop.encender())
# print(miLaptop.apagar())
# print(miLaptop.mostrar_informacion())



## 9. crear una clase puesto de mercado que tenga un atributo de clase, 5 atributos de instancia y 5 funcionalidades.
# debera crear 4 instancias de la clase mercado ejm puesto mechita, puesto la gringa, puesto ojo de uva.


class puesto:
    nombre_puesto= "Desconocida"
    def __init__(self,verduras,frutas,abarrotes,limpieza,concerbas):
        self.verduras =verduras
        self.frutas=frutas
        self.abarrotes=abarrotes
        self.limpieza=limpieza
        self.concerbas=concerbas
    def llamado_cliente(self):
        return f""" 
compre cacero... :v
"""
    def venta(self):
        return f"""
...
{self.verduras}
{self.abarrotes}
{self.frutas}
{self.limpieza}
{self.concerbas}
...
"""
    def atencion(self):
        return f"""
compre chamo XD
"""
    def delybery(self):
        return f"""
delybery 156794357
"""
    def compra(self):
        return f"""
Esperando a los provedores
"""
puestoLaChina=puesto("verduras","frutas","abarrotes","limpieza","concerbas")
print(puestoLaChina.llamado_cliente())
print(puestoLaChina.venta())
print(puestoLaChina.atencion())
print(puestoLaChina.delybery())
print(puestoLaChina.compra())

puestoJoselito=puesto("verduras","frutas","abarrotes","limpieza","concerbas")
print(puestoJoselito.llamado_cliente())
print(puestoJoselito.venta())
print(puestoJoselito.atencion())
print(puestoJoselito.delybery())
print(puestoJoselito.compra())

puestoGringasho=puesto("verduras","frutas","abarrotes","limpieza","concerbas")
print(puestoGringasho.llamado_cliente())
print(puestoGringasho.venta())
print(puestoGringasho.atencion())
print(puestoGringasho.delybery())
print(puestoGringasho.compra())

puestoMechita=puesto("verduras","frutas","abarrotes","limpieza","concerbas")
print(puestoMechita.llamado_cliente())
print(puestoMechita.venta())
print(puestoMechita.atencion())
print(puestoMechita.delybery())
print(puestoMechita.compra())