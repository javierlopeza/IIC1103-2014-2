import random
cadena_aleatoria=""
ca=cadena_aleatoria
#Formacion Cadena Aleatoria
#mientras la cadena aleatoria formada tenga una longitud menor a 10 cocatenarle
#otro numero entre 0 y 9
while len(ca)<10:
    numero_aleatorio=random.randint(0, 9)
    na=str(numero_aleatorio)
    ca=ca+na
#CLAVE
clave = "8681307185584869"
#Formacion de secuencia de clave+cadena_aleatoria:
secuencia_a_repetir=clave+ca
secrep=secuencia_a_repetir
#FORMACION CADENA DE INICIO
cadena_de_inicio=(9*secrep)+clave
cdi=cadena_de_inicio
for n in range(0,6):
    cdi=cdi+(ca[n])
#LISTA DE NUMEROS
lista_de_numeros=[]
ldn=lista_de_numeros
for r in range(0,256):
    ldn=ldn+[r]
#Cambio de orden de numeros en lista de numeros   V2:
for i in range(0, 256):
    nueva_posicion=int(i+int(cdi[i]))
    np=nueva_posicion
    if np<256:
        gi=ldn[np]
        ldn[np]=ldn[i]
        ldn[i]=gi
    elif np>=256:
        np=int(np-256)
        gi=ldn[np]
        ldn[np]=ldn[i]
        ldn[i]=gi
#codificacion de lista de numeros desordenados a codigo binario cada numero:
for i in range(0,256):
    ldn[i]=bin(ldn[i])
    ldn[i]=ldn[i].split("b")
    ldn[i]=ldn[i][1]
    while len(ldn[i])<8:
        ldn[i]=("0"+ldn[i])
#cocatenacion de los numeros binarios correspondientes a los de la lista de numeros de 0 a 255 cambiados de orden
cocatenado_ndesordenados_binarios=""
ccnb=cocatenado_ndesordenados_binarios
for nb in range(0, 256):
    ccnb=ccnb+ldn[nb]
ldnbin=ccnb
#------------------------------------------------------------
#MENSAJE
msje=str(whatsintro_gui.mensaje_redactado())
cocatenado_de_binarios=""
cdb=cocatenado_de_binarios
for l in range(len(msje)):
    #Codificacion ASCII:
    ASCII=ord(msje[l])
    #Codificacion Binaria:
    BIN=str(bin(ASCII))
    #Eliminacion letra "b":
    BIN=BIN.split("b")
    #Uso unicamente de la parte larga del numero binario:
    BIN=BIN[1]
    #Agregar ceros a la izquierda hasta que tenga 8 digitos:
    while len(BIN)<8:
        BIN=("0"+BIN)
    #Cocatenado de numeros binarios correspondientes a cada palabra:
    cdb=cdb+BIN
mbin=cdb
#----------------------------------------------------
#Lista de numeros en binario: ldnbin
#Mensaje en binario: mbin
#MENSAJE CODIFICADO:
mensaje_codificado=""
mcod=mensaje_codificado
rangomcod=int(len(mbin))
for i in range(0, rangomcod):
    if ldnbin[i]==mbin[i]:
        mcod=mcod+"0"
    elif ldnbin[i]!=mbin[i]:
        mcod=mcod+"1"
#---------------------------------------------------------
#MENSAJE A ENVIAR
mensaje_a_enviar=ca+mcod
mensaje_encriptado=mensaje_a_enviar
























































