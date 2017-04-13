import copy
def mostrar_menu_principal():
    print("(1) Crear una nueva ficha")
    print("(2) Crear un nuevo tablero")
    print("(3) Cargar un tablero con fichas")
    print("(0) Salir")
def verificar_par_ordenado(par_verificar):
        existe_coma=par_verificar.find(",")
        if existe_coma!=-1:
            lista_numeros_par_ordenados=par_verificar.split(",")
        else:
            return("ERROR")
        if len(lista_numeros_par_ordenados)==2:
            for i in range(0,2):
                ver=0
                for c in lista_numeros_par_ordenados[i]:
                    if ord(str(c))>47 and ord(str(c))<58:
                        ver+=1
                if ver!=len(lista_numeros_par_ordenados[i]):
                    return("ERROR")
        else:
            return("ERROR")
        n1=int(lista_numeros_par_ordenados[0])
        n2=int(lista_numeros_par_ordenados[1])
        return(n1,n2)
def crear_txt_ficha():
    nombre_nueva_ficha=str(input("Ingrese el nombre del archivo de la nueva ficha: "))
    nuevo_txt_ficha=open(str(nombre_nueva_ficha),"a")
    movimiento_ficha=None
    while movimiento_ficha!=0:
        movimiento_ficha=str(input("Ingrese el siguiente movimiento de la ficha o un 0 para terminar: "))
        #---
        #Verificar que el movimiento ingresado sea un par ordenado del tipo: n1,n2
        verificador=copy.deepcopy(movimiento_ficha)
        if verificar_par_ordenado(verificador)!="ERROR":
            n1=verificar_par_ordenado(verificador)[0]
            n2=verificar_par_ordenado(verificador)[1]
            
        #---
        if str(movimiento_ficha)!="0":
            nuevo_txt_ficha.write(movimiento_ficha)
while True:
    mostrar_menu_principal()
    opcion=int(input("Seleccione una opción: "))
    if opcion==1:
        crear_ficha()
    if opcion==0:
        print("PROGRAMA FINALIZADO")
