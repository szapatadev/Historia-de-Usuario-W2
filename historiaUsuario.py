def agregar_producto():
    try:
        # Se solicita cuántos productos va a ingresar el usuario
        i = int(input("Cuantos productos quieres ingresar: "))
    except:
        # Si el usuario escribe algo que no es número
        print("Ingresa el valor solicitado")
    
    # Mientras el contador sea diferente de cero se siguen registrando productos
    while i != 0:
        try:
            # Solicitar datos del producto
            nombre = input("Ingresa el nombre del producto: ")
            precio = float(input("Ingresa el precio del producto: "))
            cantidad = int(input("Ingresa la cantidad disponible: "))

            # Agregar un diccionario con la información al inventario
            inventario.append({
                "Nombre": nombre,
                "Precio": precio,
                "Cantidad": cantidad
            })
        except:
            # Manejo de errores si el usuario digita datos incorrectos
            print("Ingresa el valor solicitado")

        # Reducimos el contador de productos pendientes por ingresar
        i -= 1
        print("\n")

def mostrar_inventario():
    # Si no hay productos registrados
    if len(inventario) == 0:
        print("No hay productos en el inventario\n")
    else:
        # Empezamos a recorrer desde el último producto hacia atrás
        i = len(inventario)
        while i != 0:
            # Mostrar información del producto usando formato
            print(
                f"Producto: {inventario[i - 1]['Nombre']} | "
                f"Precio: {inventario[i - 1]['Precio']} | "
                f"Cantidad: {inventario[i - 1]['Cantidad']}"
            )
            i -= 1
        print("\n")

def calcular_estadisticas():
    # Cantidad de productos en el inventario
    i = len(inventario)
    sumaInventario = 0

    # Recorrer los productos para calcular el valor total
    while i != 0:
        sumaInventario += inventario[i - 1]["Precio"] * inventario[i - 1]["Cantidad"]
        i -= 1

    # Mostrar resultados
    print(f"El valor total del inventario es: {sumaInventario}")
    print(f"Haz registrado {len(inventario)} en el inventario \n")

# Variable para controlar el menú principal
opcion_entrada = 0

# Lista donde se almacenarán los productos
inventario = []

# Ciclo principal del programa
while opcion_entrada != 4:
    try:
        # Mostrar el menú al usuario
        print(
            "Menu - Escoge una opción\n"
            "1 - Agregar producto\n"
            "2 - Mostrar inventario\n"
            "3 - Calcular estadísticas\n"
            "4 - Salir\n"
        )
        opcion_entrada = int(input("Que quieres? "))
    except:
        # En caso de ingresar algo inválido
        print("Agrega una opción valida\n")

    # Validación de opción fuera de rango
    if opcion_entrada < 1 or opcion_entrada > 4:
        print("Ingresa un valor valido\n")

    # Llamar a la función correspondiente según la opción
    if opcion_entrada == 1:
        agregar_producto()
    elif opcion_entrada == 2:
        mostrar_inventario()
    elif opcion_entrada == 3:
        calcular_estadisticas()