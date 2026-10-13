# Sistema de facturacion
# Tarea 1: Inventario en memoria

nombre_empresa = "Tecnologia Springfield"
iva = 0.15

print("================================")
print(nombre_empresa)
print("Sistema de facturacion")
print("================================")
print(f"IVA configurado: {iva * 100}%")

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

print(productos[0]["nombre"])

print("\n--- INVENTARIO ---")

for producto in productos:
    print(f"ID: {producto['id']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: ${producto['precio']:.2f}")
    print(f"Stock: {producto['stock']}")
    print("-------------------")