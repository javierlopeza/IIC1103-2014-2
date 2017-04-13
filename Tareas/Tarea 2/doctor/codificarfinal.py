#codificar mensaje
import random
from whatsintro_msg import*
from whatsintro_gui import *


def cadenaaleatoria():
    global cadenaal
    cadenaal=""
    contador=0
    while contador<10:
        numero=random.randint(0,9)
        cadenaal += str(numero)
        contador+=1
    return(cadenaal)


def cadena_de_inicio():
    aleatoria=cadenaal
    cadenainicio=""
    clave="38872805571643309"
    listainicio=[]
    while len(cadenainicio)<=500:
        cadenainicio+=clave
        cadenainicio+=aleatoria
    if len(cadenainicio)>256:
        cadenainicio=cadenainicio[0:256]
    cadenainicio=2*cadenainicio
    return cadenainicio



def lista_numeros():
    listanum=[]
    for i in range(0,256):
        listanum.append(i)
    return listanum


def ordenar_lista():
    listanum=lista_numeros()
    listainicio=cadena_de_inicio()
    for i in range(0,len(listanum)):
        if (i+int(listainicio[i]))<=255:
            j=i+int(listainicio[i])
        else:
            j=(i+int(listainicio[i]))-256
        mp=listanum[i]
        listanum[i]=listanum[j]
        listanum[j]=mp
    return listanum



def pasar_a_binario(texto):
    final=""
    for i in texto:
        i=str(i)
        i=ord(i)
        i=bin(i)
        i=str(i)
        i=i.replace("b","")
        i=i.zfill(8)
        final+=i
    return final


def encriptar_mensaje(mensaje1):
    txt=mensaje1
    listanumfinal=""
    listanum=ordenar_lista()
    mensaje=pasar_a_binario(txt)
    for i in listanum:
        i=int(i)
        i=bin(i)
        i=str(i)
        i=i.replace("0b","")
        i=i.zfill(8)
        i=str(i)
        listanumfinal+=i
    cadena1=""
    for i in mensaje:
        i=str(i)
        cadena1+=i
    cadenacodificada=""
    for i in range(0,len(cadena1)):
        if cadena1[int(i)]==listanumfinal[int(i)]:
            cadenacodificada+="0"
        else:
            cadenacodificada+="1"
    mensajefinal=str(cadenaal)+str(cadenacodificada)
    return mensajefinal



def cadena_de_inicio_decodificar(aleator):
    aleatoria=aleator
    cadenainicio=""
    clave="38872805571643309"
    listainicio=[]
    while len(cadenainicio)<=256:
        cadenainicio+=clave
        cadenainicio+=aleatoria
    if len(cadenainicio)>256:
        cadenainicio=cadenainicio[0:256]
    for i in cadenainicio:
        listainicio.append(i)
    return listainicio

def ordenar_lista_decodificar(aleator):
    listanum=lista_numeros()
    listainicio=cadena_de_inicio_decodificar(aleator)
    listaprincipal=listanum
    for i in range(0,len(listanum)):
        if (i+int(listainicio[i]))<=255:
            j=i+int(listainicio[i])
        else:
            j=(i+int(listainicio[i]))-256
        pos_i=listaprincipal[i]
        pos_j=listaprincipal[j]
        listanum[i]=pos_j
        listanum[j]=pos_i
        return listanum

def decodificar(cadena):
    aleatorio=cadena[0:10]
    cadena=cadena[10:len(cadena)]
    listacadena=[]
    listadesorden=ordenar_lista_decodificar(aleatorio)
    mensaje=[]
    for i in cadena:
        listacadena.append(i)
    for j in range(0,len(listacadena)):
        if listacadena[j]==0:
            mensaje.append(listadesorden[j])
        elif listacadena[j]==1:
            if listadesorden[j]==0:
                mensaje.append(1)
            elif listadesorden[j]==1:
                mensaje.append(0)
        print(mensaje)
        cadenita=""

        for j in range(0,len(cadena)):
        
            if j%8==0:
                lista=listacadena[j:j+8]
                for k in lista:
                    cadenita+=str(k)
                cadenita=int(cadenita,2)
                cadenita=chr(cadenita)
                print(cadenita)
                return cadenita


########
########
usuario="@cicontreras2"
clave="38872805571643309"
print("conectado:", conectar(usuario, clave))
#######
#######
cadenaaleatoria()
cadena_de_inicio()
lista_numeros()
ordenar_lista()
######
a="hola"
b=encriptar_mensaje(a)
#####
print(validar_encriptacion(a,b))
######
