import copy
def mostrar_menu_principal():
    print("")
    print("(1) Crear una nueva ficha")
    print("(2) Crear un nuevo tablero")
    print("(3) Cargar un tablero con fichas")
    print("(0) Salir")
def mostrar_menu_cargar():
    print("")
    print("(1) Imprimir el tablero con las fichas")
    print("(2) Preguntar por los movimientos de una pieza")
    print("(3) Verificar si se pueden mover las piezas sobre el tablero sin repetir posiciones")
    print("(0) Volver al menu principal")
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
    print("-------- Ficha <<"+nombre_nueva_ficha+">> creada correctamente --------")
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
    print("-------- Tablero <<"+nombre_nuevo_tablero+">> creado correctamente --------")
    print("")
def cargar_tablero_con_fichas():
    print("")
    nombre_tablero=str(input("Ingrese el nombre del archivo correspondiente al tablero: "))
    tablero_cargado=Tablero(str(nombre_tablero))
    filasT=(tablero_cargado.dimensiones_tablero()[0])
    columnasT=(tablero_cargado.dimensiones_tablero()[1])
    proxima_ficha_o_terminar=None
    numero_ficha=0
    while proxima_ficha_o_terminar!="0":
        proxima_ficha_o_terminar=str(input("Ingrese el nombre del archivo de la próxima ficha o un 0 para terminar: "))
        if proxima_ficha_o_terminar!="0":
            nombre_archivo=str(proxima_ficha_o_terminar)
            contador=0
            for i in tablero_cargado.fichas_posicionadas:
                if i.count(nombre_archivo)!=0:
                    contador+=1
            if contador==0:
                numero_ficha+=1
                ficha_cargada=Ficha(str(nombre_archivo))
                tablero_cargado.fichas_posicionadas.append((numero_ficha,nombre_archivo,ficha_cargada.lista_movimientos()))
                posicion_inicial=str(input(str("Ingrese la posición inicial para "+str(ficha_cargada.nombre_ficha)+": ")))
                if posicion_valida(filasT, columnasT, posicion_inicial)==True:
                    posiciones=posicion_inicial.split(",")
                    posicionF=int(posiciones[0])
                    posicionC=int(posiciones[1])
                    if ficha_cargada.posicionar_en(posicion_inicial, filasT, columnasT)==True and tablero_cargado.casillas_tablero[posicionF][posicionC]=="O":
                        tablero_cargado.agregar_ficha(ficha_cargada.nombre_ficha, posicionF, posicionC)
                        print("")
                        print("-------- La ficha <<"+ficha_cargada.nombre_ficha+">> ha sido posicionada correctamente en "+str(ficha_cargada.posicion)+" --------")
                        print("")
                    else:
                        print("Posición inválida, intente otra vez...")
                else:
                    print("Posición inválida, intente otra vez...")
            else:
                print("Ficha ya posicionada, intente otra vez...")
        else:
            break
    return(tablero_cargado)
def imprimir_tablero_con_fichas(tablero_con_fichas):
    print("")
    tablero_con_fichas.mostrar_tablero()
def mostrar_posibles_movimientos_ficha(tablero):
    print("")
    for i in range(len(tablero.fichas_posicionadas)):
        print("("+str(i+1)+") "+str(tablero.fichas_posicionadas[i][1]))
    numero_ficha=-1
    numero_ficha=int(input("Seleccione una ficha: "))
    while numero_ficha>len(tablero.fichas_posicionadas) or numero_ficha<0:
        print("Selección inválida, por favor escoja una de las fichas de la lista...")
        numero_ficha=int(input("Seleccione una ficha: "))
    movimientos=tablero.fichas_posicionadas[int(numero_ficha)][2]
    
        
        
    
#-------------------------
    
class Ficha():
    def __init__(self,nombre_archivo):
        self.nombre_ficha=str(nombre_archivo)
        self.posicion=None
    def posicionar_en(self, ubicacion, filasT, columnasT): #Recibe donde quiero posicionarla (un par ordenado en string) y las dimensiones del tablero en cuestion
        es_valido=posicion_valida(filasT, columnasT, ubicacion)
        if es_valido==True:
            self.posicion=ubicacion
            return True
        else:
            return False
    def lista_movimientos(self): #Me entrega una lista con los movimientos posibles.
        self.movimientos=open(str(self.nombre_ficha),"r")
        lista_movimientos=self.movimientos.readlines()
        self.movimientos.close()
        return (lista_movimientos)

class Tablero():
    casillas_tablero=[]
    fichas_posicionadas=[]
    str_simbologia="O: Posición libre | X: Posición prohibida | " #Fichas con sus simbolos respectivos
    def __init__(self,nombre_archivo):
        self.nombre_tablero=str(nombre_archivo)
        tablero_txt=open(str(nombre_archivo),"r+")
        self.lista_tablero_txt=tablero_txt.readlines()
        tablero_txt.close()
        dims=self.lista_tablero_txt[0].split(",")
        self.F=int(dims[0])
        self.C=int(dims[1])
        for i in range(self.F):
            fila=[]
            for j in range(self.C):
                fila.append("O")
            self.casillas_tablero.append(fila)
        if len(self.lista_tablero_txt)>1: #Si la lista del texto tablero incluye restricciones, crear la lista con las restricciones, si no, no.
            self.posiciones_prohibidas=self.lista_tablero_txt[1:]
            for i in range(0,len(self.posiciones_prohibidas)):
                posicionP=self.posiciones_prohibidas[i].split(",")
                posPF=int(posicionP[0])
                posPC=int(posicionP[1])
                self.casillas_tablero[posPF][posPC]="X"
        self.simbolo_ficha=0         
    def dimensiones_tablero(self):
        dims=self.lista_tablero_txt[0].split(",")
        F=int(dims[0])
        C=int(dims[1])
        return (F,C)
    def mostrar_tablero(self):
        for i in range(len(self.casillas_tablero)):
            for j in range(len(self.casillas_tablero[i])):
                print(self.casillas_tablero[i][j], end=' ')
            print('')
        print("")
        print(self.str_simbologia)
        print("")
    def agregar_ficha(self, nombre_ficha, posicionF, posicionC):
        self.simbolo_ficha+=1
        agregar=str(str(self.simbolo_ficha)+": "+str(nombre_ficha)+" | ")
        self.str_simbologia+=agregar
        self.casillas_tablero[int(posicionF)][int(posicionC)]=self.simbolo_ficha

#-------------------------


while True:
    mostrar_menu_principal()
    opcion=(input("Seleccione una opción: "))
    if verificar_numero_0a3(opcion)==True:
        opcion=int(opcion)
        if opcion==3:
            tablero_cargado=cargar_tablero_con_fichas()
            while opcion==3:
                mostrar_menu_cargar()
                opcionC=int(input("Seleccione una opción: "))
                if opcionC==1:
                    imprimir_tablero_con_fichas(tablero_cargado)
                if opcionC==2:
                    mostrar_posibles_movimientos_ficha(tablero_cargado)
                if opcionC==3:
                    pass
                if opcionC==0:
                    opcion=4
                    break
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
