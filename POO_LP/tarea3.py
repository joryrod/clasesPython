productos=[
    {
        'id':1,
        'nombre':'arroz',
        'codigo':'2023-A',
        'descripcion':'costeño costal x 100 kg',
        'stock':5,
        'unidad':'costales',
        'precio':125,
        'moneda':'soles'
    }
]

## casos de uso
class Producto:
    ## atributos de clase
    ## moneda = 'soles'


    ## atribustos de instancia
    def __init__(self, codigo, nombre, descripcion, stock, unidad, precio, moneda='soles',):
        self.codigo=codigo
        self.nombre=nombre
        self.descripcion=descripcion
        self.stock=stock
        self.unidad=unidad
        self.precio=precio
        self.moneda=moneda


    ## creacion de metodos
    def mostrar_productos(self):
        mensaje=f"""
        tienes {len(productos)} productos
        los productos son:
        {productos}
        """
        return mensaje
    def mostrar_producto(self, id):
        producto_buscar=productos[id-1] ## en mis prodcutos empeiza de 0 y el id es 1, por eso id - 1 para que me jueste mi primer producto
        pass

    def registrar_producto(self):
        nuevo_id=len(productos)+1
        producto_nuevo={
            "id":nuevo_id,
            'codigo':self.codigo,
            "nombre":self.nombre,
            'descripcion':self.descripcion,
            'stock':self.stock,
            'unidad':self.unidad,
            'precio':self.precio,
            'moneda':self.moneda
        }
        registro_producto=productos.append(producto_nuevo)
        return 'producto registrado exitosamente'

    def eliminar_producto(self, id):
        producto_eliminar=productos.pop(id-1)
        return f"el siguiente producto fue eliminado {producto_eliminar}"

    def actualizar_producto(self, id, clave, valor):
        ol=valor
        producto_actualizar=list(filter(lambda obj:obj[clave]==id,productos))[0].update({clave:valor})
        return 'se actualizo'



prod=Producto('2023-b','aceite', 'extra virgen',2, 'botella x litro', 12.5)
print(prod.registrar_producto())
print(prod.mostrar_productos())
print(prod.actualizar_producto(125,'precio','130'))
print(prod.mostrar_productos())