class Tienda:
    def _init_(self, nombre, categorias, horario_atencion, gerente):
        self.nombre = nombre
        self.categorias = categorias
        self.horario_atencion = horario_atencion
        self.gerente = gerente

    def _str_(self):
        return f"Nombre: {self.nombre}, Gerente: {self.gerente}"

# Lista de tiendas
tiendas = [
    Tienda("El chino", ["Bodega"], {"dia": "7am-12m", "tarde": "2pm-8pm"}, "Nadine"),
    Tienda("La esquina", ["Farmacia"], {"dia": "8am-5pm", "tarde": "No atiende"}, "Cristian"),
    Tienda("bodega lili", ["Abarrotes", "Bodega"], {"dia": "6am-10pm", "tarde": "No atiende"}, "Edwin"),
    Tienda("carniceria perron", ["Restaurante"], {"dia": "8am-10pm", "tarde": "No atiende"}, "China"),
    Tienda("bolognesi", ["Farmacia"], {"dia": "9am-6pm", "tarde": "No atiende"}, "Cristian"),
    Tienda("Mini Market la economica", ["Bodega", "Abarrotes"], {"dia": "7am-11pm", "tarde": "3pm-9pm"}, "Nadine"),
    Tienda("Restaurante la cabaña", ["Restaurante"], {"dia": "10am-11pm", "tarde": "No atiende"}, "China"),
    Tienda("La quinta", ["Bodega"], {"dia": "6am-8pm", "tarde": "No atiende"}, "Edwin"),
    Tienda("Farmacia lobo", ["Farmacia"], {"dia": "7am-7pm", "tarde": "No atiende"}, "Cristian"),
    Tienda("Bodega parurri", ["Bodega"], {"dia": "8am-10pm", "tarde": "3pm-9pm"}, "Edwin")
]

# Método para filtrar tiendas por gerente
def tiendas_por_gerente(gerente):
    return [tienda for tienda in tiendas if tienda.gerente == gerente]

# Método para mostrar tiendas con más de dos gerentes
def tiendas_con_mas_de_dos_gerentes():
    gerente_count = {}
    for tienda in tiendas:
        gerente_count[tienda.nombre] = gerente_count.get(tienda.nombre, 0) + 1
    return [nombre for nombre, count in gerente_count.items() if count > 2]

# Método para mostrar el nombre y la RUC de las tiendas (simulación)
def nombre_y_ruc_de_tiendas():
    tiendas_info = {
        "El Pichilón": "RUC-123456789",
        "La Botica": "RUC-987654321",
        "Supermercado XYZ": "RUC-456789123",
        "Cafetería del Sol": "RUC-789123456",
        "La Farmacéutica": "RUC-654321987",
        "Mini Market A1": "RUC-321987654",
        "Restaurante Sabores": "RUC-234567890",
        "La Esquina": "RUC-890123456",
        "Farmacia Rápida": "RUC-567890123",
        "Bodega Económica": "RUC-987654321"
    }
    return tiendas_info

# Ejemplos de uso
print("1. Tiendas de Cristian:")
cristian_tiendas = tiendas_por_gerente("Cristian")
for tienda in cristian_tiendas:
    print(tienda)

print("\n2. Tiendas con más de dos gerentes:")
mas_de_dos_gerentes = tiendas_con_mas_de_dos_gerentes()
for tienda_nombre in mas_de_dos_gerentes:
    print(f"Tienda: {tienda_nombre}")

print("\n3. Nombre y RUC de las tiendas:")
tiendas_info = nombre_y_ruc_de_tiendas()
for nombre, ruc in tiendas_info.items():
    print(f"Nombre: {nombre}, RUC: {ruc}")