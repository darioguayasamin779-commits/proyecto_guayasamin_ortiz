# Sistema de facturacion
# Tareas 1, 2 y 3

nombre_empresa = "Tecnologia Springfield"
iva = 0.15

print("=================================")
print("Sistema de facturacion")
print("=================================")
print(nombre_empresa)
print(f"IVA configurado: {iva * 100}%")
print("=================================")

# ---------------------------------------------------------
# TAREA 1: Inventario
# ---------------------------------------------------------
productos = [
    {
        "id": 1,
        "nombre": "Teclado",
        "precio": 15.00,
        "stock": 10
    },
    {
        "id": 2,
        "nombre": "Mouse",
        "precio": 8.50,
        "stock": 20
    },
    {
        "id": 3,
        "nombre": "Monitor",
        "precio": 180.00,
        "stock": 5
    }
]

print("\n--- INVENTARIO ---")
for producto in productos:
    print(f"ID: {producto['id']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: ${producto['precio']:.2f}")
    print(f"Stock: {producto['stock']}")
    print("-------------------")


# ---------------------------------------------------------
# TAREA 2: Función para buscar productos por ID
# ---------------------------------------------------------
def buscar_producto(id_producto):
    for producto in productos:
        if producto["id"] == id_producto:
            return producto
    return None


# ---------------------------------------------------------
# TAREA 3: Agregar productos
# ---------------------------------------------------------
print("\n--- CREAR FACTURA ---")
factura_items = []

id_ingresado = int(input("Ingrese el ID del producto que desea agregar: "))
cantidad_ingresada = int(input("Ingrese la cantidad: "))

producto_encontrado = buscar_producto(id_ingresado)

if producto_encontrado:
    if cantidad_ingresada <= producto_encontrado["stock"]:
        item_factura = {
            "nombre": producto_encontrado["nombre"],
            "precio": producto_encontrado["precio"],
            "cantidad": cantidad_ingresada,
            "subtotal": producto_encontrado["precio"] * cantidad_ingresada
        }
        factura_items.append(item_factura)
        print(f"\n ¡Producto agregado con éxito!")
        print(f"Agregado: {cantidad_ingresada}x {producto_encontrado['nombre']} - Subtotal: ${item_factura['subtotal']:.2f}")
    else:
        print("\n Error: No hay suficiente stock disponible para esa cantidad.")
else:
    print("\n Error: El producto con ese ID no existe.")

print("\n--- DETALLE DE LA FACTURA ---")
for item in factura_items:
    print(f"- {item['cantidad']}x {item['nombre']} (${item['precio']:.2f} c/u) = ${item['subtotal']:.2f}")