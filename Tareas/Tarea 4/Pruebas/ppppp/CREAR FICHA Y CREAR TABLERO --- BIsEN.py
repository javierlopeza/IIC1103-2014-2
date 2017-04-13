import copy
def mostrar_menu_principal():
    print("(1) Crear una nueva ficha")
    print("(2) Crear un nuevo tablero")
    print("(3) Cargar un tablero con fichas")
    print("(0) Salir")
def verificar_numero_0a3(n):
    if len(n)!=1:
        return False
    largo=len(str(n))
    for c in str(n):
        if ord(c)>47 and ord(c)<52:
            return True
        else:
            return False
def verificar_par_ordenado(par_verificar):
        existe_coma=par_verificar.find(",")
        if existe_coma!=-1 and existe_coma!=0 and existe_coma!=(len(par_verificar))-1:
            lista_numeros_par_ordenados=par_verificar.split(",")
        else:
            return("ERROR")
        if len(lista_numeros_par_ordenados)==2:
            for i in range(0,2):
                ver=0
                for c in range(len(lista_numeros_par_ordenados[i])):
                    actual=ord(str(lista_numeros_par_ordenados[i][c]))
                    if c!=0:
                        anterior=ord(str(lista_numeros_par_ordenados[i][c-1]))
                    if c!=len(lista_numeros_par_ordenados[i])-1:
                        siguiente=ord(str(lista_numeros_par_ordenados[i][c+1]))
                    if actual>47 and actual<58:
                        ver+=1
                    if actual==45 and len(lista_numeros_par_ordenados[i])==1:
                        return("ERROR") 
                    elif actual==45 and c==0 and (siguiente>47 and siguiente<58):
                        ver+=1
                if ver!=len(lista_numeros_par_ordenados[i]):
                    return("ERROR")
        else:
            return("ERROR")
        n1=(lista_numeros_par_ordenados[0])
        n2=(lista_numeros_par_ordenados[1])
        return(n1,n2)
def verificar_repetido(a_agregar, nombre_archivo):
    archivo_txt=open(str(nombre_archivo),"r")
    lista=archivo_txt.readlines()
    for i in range(len(lista)):
        if str(lista[i][:-1])==(str(a_agregar[:-1])):
            #Ya se ingresó anteriormente el movimiento a la ficha
            archivo_txt.close()
            return False
    archivo_txt.close()
    return True
def verificar_repetido_tablero(a_agregar, nombre_archivo):
    archivo_txt=open(str(nombre_archivo),"r")
    lista=archivo_txt.readlines()
    for i in range(1,len(lista)):
        if str(lista[i][:-1])==(str(a_agregar[:-1])):
            #Ya se ingresó anteriormente el movimiento a la ficha
            archivo_txt.close()
            return False
    archivo_txt.close()
    return True
def crear_txt_ficha():
    print("")
    nombre_nueva_ficha=str(input("Ingrese el nombre del archivo de la nueva ficha: "))
    nuevo_txt_ficha=open(str(nombre_nueva_ficha),"a")
    nuevo_txt_ficha.close()
    movimiento_o_terminar=None
    while str(movimiento_o_terminar)!="0":
        movimiento_o_terminar=str(input("Ingrese el siguiente movimiento de la ficha o un 0 para terminar: "))
        if str(movimiento_o_terminar)=="0":
            break
        #Verificar que el movimiento ingresado sea un par ordenado del tipo: n1,n2
        verificador=copy.deepcopy(movimiento_o_terminar)
        if verificar_par_ordenado(verificador)!="ERROR":
            n1=verificar_par_ordenado(verificador)[0]
            n2=verificar_par_ordenado(verificador)[1]
            agregar_a_txt=str(n1)+","+str(n2)+"\n"
            #Verificar que no sea un movimiento ya ingresado
            no_repetido=verificar_repetido(agregar_a_txt, nombre_nueva_ficha)
            if no_repetido==True:
                nuevo_txt_ficha=open(str(nombre_nueva_ficha),"a")
                nuevo_txt_ficha.write(agregar_a_txt)
                nuevo_txt_ficha.close()
            elif no_repetido==False:
                print("")
                print("El movimiento ya ha sido ingresado previamente...")
                print("")
        else:
            print("")
            print("Por favor, ingrese un par ordenado valido...")
            print("")
    print("")
    print("-------- ficha "+nombre_nueva_ficha+" creada correctamente --------")
    print("")
def posicion_valida(filas, columnas, posicion_evaluada):
    lista_p=posicion_evaluada.split(",")
    filap=int(lista_p[0])
    colp=int(lista_p[1])
    if filap<int(filas) and colp<int(columnas):
        if filap>=0 and colp>=0:
            return True
    else:
        return False
def dimensiones_validas(par_verificar):
    existe_coma=par_verificar.find(",")
    if existe_coma!=-1 and existe_coma!=0 and existe_coma!=(len(par_verificar))-1:
        lista_numeros_par_ordenados=par_verificar.split(",")
    else:
        return("ERROR")
    if len(lista_numeros_par_ordenados)==2:
        for i in range(0,2):
            ver=0
            for c in range(len(lista_numeros_par_ordenados[i])):
                actual=ord(str(lista_numeros_par_ordenados[i][c]))
                if c!=0:
                    anterior=ord(str(lista_numeros_par_ordenados[i][c-1]))
                if c!=len(lista_numeros_par_ordenados[i])-1:
                    siguiente=ord(str(lista_numeros_par_ordenados[i][c+1]))
                if actual>47 and actual<58:
                    ver+=1
                if actual==45 and len(lista_numeros_par_ordenados[i])==1:
                    return("ERROR") 
                elif actual==45 and c==0 and (siguiente>47 and siguiente<58):
                    return("ERROR")
            if ver!=len(lista_numeros_par_ordenados[i]):
                return("ERROR")
    else:
        return("ERROR")
    n1=(lista_numeros_par_ordenados[0])
    n2=(lista_numeros_par_ordenados[1])
    #Verificar que las dimensiones no sean 0's
    if int(n1)==0 or int(n2)==0:
        return("ERROR")
    return True
def crear_txt_tablero():
    print("")
    nombre_nuevo_tablero=str(input("Ingrese el nombre del archivo del nuevo tablero: "))
    dimensiones=str(input("Ingrese las dimensiones del tablero: "))
    nuevo_txt_tablero=open(str(nombre_nuevo_tablero),"a")
    while dimensiones_validas(dimensiones)=="ERROR":
        print("")
        print("Por favor, ingrese dimensiones válidas...")
        print("")
        dimensiones=str(input("Ingrese las dimensiones del tablero: "))
    listadim=dimensiones.split(",")
    filas=listadim[0]
    columnas=listadim[1]
    dimensiones=dimensiones+"\n"
    nuevo_txt_tablero.write(str(dimensiones))
    nuevo_txt_tablero.close()
    pprohibida_o_terminar=None
    while str(pprohibida_o_terminar)!="0":
        pprohibida_o_terminar=str(input("Ingrese la siguiente posición prohibida o un 0 para terminar: "))
        if str(pprohibida_o_terminar)=="0":
            break
        #Verificar que el movimiento ingresado sea un par ordenado del tipo: n1,n2
        verificador=copy.deepcopy(pprohibida_o_terminar)
        if verificar_par_ordenado(verificador)!="ERROR":
            n1=verificar_par_ordenado(verificador)[0]
            n2=verificar_par_ordenado(verificador)[1]
            #Verificar que sea una posición válida para las dimensiones del tablero creado
            if posicion_valida(filas, columnas, verificador)==True:
                #Verificar que no sea una posición prohibida ya ingresada
                agregar_a_txt=str(n1)+","+str(n2)+"\n"
                no_repetido=verificar_repetido_tablero(agregar_a_txt, nombre_nuevo_tablero)
                if no_repetido==True:
                    nuevo_txt_tablero=open(str(nombre_nuevo_tablero),"a")
                    nuevo_txt_tablero.write(agregar_a_txt)
                    nuevo_txt_tablero.close()
                elif no_repetido==False:
                    print("")
                    print("La posición prohibida ya ha sido ingresado previamente...")
                    print("")
            else:
                print("")
                print("La posición prohibida no es válida para el tablero creado...")
                print("")
        else:
            print("")
            print("Por favor, ingrese un par ordenado valido...")
            print("")
    print("")
    print("-------- tablero "+nombre_nuevo_tablero+" creado correctamente --------")
    print("")
    

        
while True:
    mostrar_menu_principal()
    opcion=(input("Seleccione una opción: "))
    if verificar_numero_0a3(opcion)==True:
        opcion=int(opcion)
        if opcion==2:
            crear_txt_tablero()
        if opcion==1:
            crear_txt_ficha()
        if opcion==0:
            print("---")
            print("PROGRAMA FINALIZADO")
            print("---")
            break
    else:
        print("")
        print("Por favor ingrese una opción válida. Debe ser 1, 2, 3 ó 0.")
        print("")
