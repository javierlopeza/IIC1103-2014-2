def crear_tablero():
    n=int(input("Ingrese numero: "))
    if n==5:
        print("CACACACACACACA")
    else:
        crear_tablero()

crear_tablero()
