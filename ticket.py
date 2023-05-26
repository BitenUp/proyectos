def entra_productos():
    """Se guardan los productos en un diccionario """
    datosCompra = {}
    entrada = False

    while not entrada:
        opcion = input("Para opcion un producto 'A' y para salir 'S': ")
        if opcion.lower() == "a":
            producto = input("Introduce el nombre del producto: ")
            cantidad = input("Introduce la cantidad: ")
            # Excepción para el valor numérico
            try:
                cantidad = int(cantidad)
                # Convertimos la cadena para la key de datosProducto
                producto = producto.title()
                # Actualizamos el diccionario con sus nuevos elementos
                datosCompra.update({producto: cantidad})
            except ValueError:
                print("La cantidad introducida debe ser numérica")

        elif opcion.lower() == "s":
            if not datosCompra:
                print("No se han ingresado productos.")
                return
            entrada = True

        else:
            print("Opción no válida")

    return datosCompra


def obtener_precio(producto, cantidad):
    """Cálculo del total por producto"""
    datosProducto = {
        "Bacalao": 3,
        "Mermelada": 3.4,
        "Queso": 5
    }

    # En caso de que el producto añadido no se encuentre en datosProducto
    try:
        subtotal = round(datosProducto[producto] * cantidad, 2)
        print(
            f"{producto}: {str(datosProducto[producto])} x {str(cantidad)} = {str(subtotal)}€")
        return subtotal
    except KeyError:
        print(f"El producto '{producto}' no se encuentra en 'stock'.")
        # Devolvemos un subtotal de 0, para que el programa continue con el cálculo de la factura
        return 0


def obtener_descuento(factura, membresia):
    """Descuento según la membresía"""
    # Dos variables para iniciar el valor del descuento y total devuelto.
    descuento = 0
    totalfactura = 0
    if membresia.lower() == "s":
        return factura

    if factura >= 25:
        if membresia.title() == "Gold":
            totalfactura = factura * 0.80
            descuento = 20

        elif membresia.title() == "Silver":
            totalfactura = factura * 0.90
            descuento = 10

        elif membresia.title() == "Bronze":
            totalfactura = factura * 0.95
            descuento = 5

        else:
            print(f"'{membresia}' no es una membresía")

        print(f"La cantidad de {str(round(factura))}€ tiene un descuento del {str(descuento)}% por la membresía {str(membresia.title())}: {round((factura * descuento)/100, 2)}€\
            \nTotal: {round(totalfactura, 2)}€")
    else:
        print("La cantidad de", factura, "€", "no tiene descuento")
        return factura

    return totalfactura


def factura_productos(datosCompra, membresia):
    """Función de llamada a las demás funciones"""
    total = 0
    factura = 0
    membresia_valida = False
    # Si la membresía no es válida, se vuelve a preguntar por ella
    while not membresia_valida:
        if membresia.lower() == "gold":
            membresia_valida = True

        elif membresia.lower() == "silver":
            membresia_valida = True

        elif membresia.lower() == "bronze":
            membresia_valida = True

        elif membresia.lower() == "s":
            membresia_valida = True

        else:
            print(f"'{membresia}' no es una membresía válida")
            membresia = input("Introduce tu membresía o 'S' para salir: ")

    # Recorremos los elementos del diccionario
    for producto, unidad in datosCompra.items():
        # almaceno el total en la variable 'factura'
        factura += obtener_precio(producto, unidad)

    # total con el descuento aplicado
    total = obtener_descuento(factura, membresia)
    print(f"El total es de {str(round(total, 2))}€")


datosCompra = entra_productos()
membresia = input("Cuál es tu membresía: ")

factura_productos(datosCompra, membresia)
