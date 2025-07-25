productos = []
while True:
    print("\n---MENÚ DE OPCIONES---")
    print("1.- Agregar un producto a la lista\n"
          "2.- Modificar un producto existente\n"
          "3.- Eliminar producto\n"
          "4.- Ver todos los productos\n"
          "5.- Salir del programa")
    opciones = input("Escriba el número de la opción que desea seleccionar: ")
    match opciones:
        case "1":
            prod = input("Ingrese el nombre del producto: ")
            productos.append(prod)
        case "2":
            for i, elemento in enumerate(productos):
                print(f"{i}: {elemento}")
            indice = int(input("Ingrese el índice del elemento que desea modificar: "))
            elemento_nuevo = input("Ingrese el nuevo producto: ")
            productos[indice] = elemento_nuevo}
            print("Elemento modificado")
