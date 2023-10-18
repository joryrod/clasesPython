#crear sistema para gestion de stock de productos

#entidades-> entitis--> la base de datos sobre la que voy a trabajar:
#Averiguar Formas Normales(Nprmalizacion de base de datos).

productos=[
    {
        "ID":1,
        "CODIGO":"2023-A",
        "NOMBRE":"ARROZ",
        "DESCRIPCIÓN":"COSTEÑO COSTAL X 100 K",
        "STOCK":5,
        "UNIDAD":"COSTALES",
        "PRECIO":125,
        "MONEDA":"SOLES"

    }
]

#casos de uso
class Producto:

    #atributos de instancia:
    def __init__(self,nombre,descripcion,stock,unidad,precio,moneda="soles"):
        self.nombre=nombre
        self.descripcion=descripcion
        self.stock=stock
        self.unidad=unidad
        self.precio=precio
        self.moneda=moneda

    #creacion de metodos:
    def mostrar_productos(self):
        mensaje=f"""
    Tienes {len(productos)} productos
    Los productos son: 
    {productos}
"""
        return mensaje
        
    def registrar_producto(self):
        nuevo_id=len(productos)+1
        producto_nuevo={
            "ID": nuevo_id,
            "CODIGO":"2023-B",
            "NOMBRE": self.nombre,
            "DESCRIPCION": self.descripcion,
            "STOCK": self.stock,
            "UNIDAD":self.unidad,
            "PRECIO": self.precio,
            "MONEDA":self.moneda

        }
        registro_producto=productos.append(producto_nuevo)
        return f"el siguiente producto se registro exitosamente {producto_nuevo}"
    
    def mostrar_un_producto(self,id):
        producto_buscar=productos[id-1]
        return producto_buscar
    
    def eliminar_producto(self,id):
        producto_eliminado=productos.pop(id-1)
        return f"el siguiente producto fue eliminado {producto_eliminado}"

    def actualizar_producto(self,id,clave,valor):
        ol=valor
        actualizacion= list(filter(lambda obj: obj[clave]==id, productos))[0].update({clave:valor}) 
        #LIST--funcion para crear una lista {'h','o','l','a'} 
        #METODO FUNCIONAL FILTER --> Retorna una lista nueva con el elemento que sea True en una listak
        #funciones anonimas o autoejecutados en python se les conoce como funciones
        #lambda --> funcion anonima: lambda a,b: return a+b---esta funcion no se llama, se autoejecuta
        return "se actualizo"
    
#PROGRAMACION FUNCIONAL DE PYTHON


prod=Producto('aceite','sol 1L',2,'BOTELLA',10)
print(prod.registrar_producto())
print(prod.mostrar_productos())
# print(prod.mostrar_un_producto(1))
# print(prod.eliminar_producto(2))
# print(prod.mostrar_productos())
print(prod.actualizar_producto("2023-B","CODIGO","CUALQUIER COSA"))
print(prod.mostrar_productos())