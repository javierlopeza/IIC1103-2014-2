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
def crear_txt_ficha():
    print("")
    nombre_nueva_ficha=str(input("Ingrese el nombre del archivo de la nueva ficha: "))
    nuevo_txt_ficha=open(str(nombre_nueva_ficha),"a")
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
            print(n1,n2)
            agregar_a_txt=str(n1)+","+str(n2)+"\n"
            nuevo_txt_ficha.write(agregar_a_txt)
        else:
            print("")
            print("Por favor, ingrese un par ordenado valido...")
            print("")
    nuevo_txt_ficha.close()
    print("")
    print("-------- ficha "+nombre_nueva_ficha+" creada correctamente --------")
    print("")
    

        
while True:
    mostrar_menu_principal()
    opcion=(input("Seleccione una opción: "))
    if verificar_numero_0a3(opcion)==True:
        opcion=int(opcion)
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
