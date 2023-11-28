import orm 
from tablas.Productos import Productos
from tablas.Clientes import Clientes

db=orm.SQLiteORM("tiendita")
db.crear_tabla(Productos)
db.crear_tabla(Clientes)

# data={
#         "nombre":"detergente potito",
#         "precio":2.50,
#         "descripcion":"el que limpia todo",
#         "cantidad":10
# }
# db.insertarUno("Productos",data)
# print(db.mostrar("Productos"))

# data=[
#     {
#         "nombre":"Chinita",
#         "dni":70142589,
#         "celular":123654789,
#         "f_nacimineto":"13/06/2004"
#     },
#     {
#         "nombre":"mochucha",
#         "dni":758669213,
#         "celular":789456321,
#         "f_nacimineto":"25/12/2023"
#     }
# ]
# db.insertarVarios("Clientes",data)
# print(db.mostrar("Clientes"))

data=("f_nacimiento":"10/10/2003")

db.actualizar("Clientes",data,nombre="mochucha")
print(db.mostrar("Clientes"))
