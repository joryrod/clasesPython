## crear un sistema para gestion control de stock de producos.
# caso de uso
# historia de usuario
# producto ower
# baclog
# MVP
# prototipos de mierda

# entidad entitis
# la base de datos sobre la que voy a trabajar
# averiguar formas normales (normalizacion de base de datos)
productos=[
    {
        "ID":1,
        "nombre":"arroz",
        "descripcion":"costeño costal x 50 kg",
        "stock":5,
        "unidad":"costales",
        "precio":125,
        "moneda":"soles"
    }   
]
## casos de uso

class Producto:
    # atributos de clase
    def __init__(self,nombre,descripcion,stock,unidad,precio,moneda="soles"):
        self.nombre=nombre
        self.descripcion=descripcion
        self.stock=stock
        self.unidad=unidad
        self.precio=precio
        self.moneda=moneda

    # creacion de metodos

    def mostrar_productos(self):
            mensaje=f"""
            tienes {len(productos)} productos
            los productos son:
            {productos}
            """
            return mensaje

    def registrar_producto(self):
            nuevo_ID=len(productos)+1
            producto_nuevo={
                "ID":nuevo_ID,
                "nombre":self.nombre,
                "descripcion":self.descripcion,
                "stock":self.stock,
                "unidad":self.unidad,
                "precio":self.precio,
                "moneda":self.moneda
            }
            registrar_producto=productos.append(producto_nuevo)
            return f" El siguiente producto se registro exitosamente{producto_nuevo}"
        
    def mostrar_producto(self,ID):
            producto_buscar=productos[ID-1]
            return producto_buscar

    def eliminar_producto(self,ID):
            producto_eliminar=productos.pop(ID-1)    
            return f"el siguiente producto fue eliminado {producto_eliminar}"
    def actualizar_producto(self):
            return f"""
            sus productos an sido actualizados
            """
    
    



prod=Producto("aceite","extra virgen",2,"botella x litro",12.50)
print(prod.registrar_producto())
print(prod.mostrar_productos())
print(prod.mostrar_producto(1))
print(prod.eliminar_producto(2))
print(prod.mostrar_productos())
print(prod.actualizar_producto())
print(prod.mostrar_productos())