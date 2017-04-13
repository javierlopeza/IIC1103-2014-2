import whatsintro_gui
from whatsintro_gui import *
import whatsintro_msg
from whatsintro_msg import *
import random

#codificar mensaje
import random
from whatsintro_msg import*
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
    aleatoria=cadenaaleatoria()
    print(aleatoria)
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
##        (listanum[i],listanum[j])=(listanum[j],listanum[i])
        listanum[j]=mp
    listabuena=[242,9,10,250,238,13,4,2,5,16,11,17,1,7,0,15,25,14,19,21,23,8,27,29,31,33,35,30,36,37,20,18,40,24,39,32,43,38,44,28,34,22,42,52,41,46,48,50,26,54,56,58,60,62,57,63,64,47,45,67,51,66,59,70,65,71,55,61,49,69,79,68,73,75,77,53,81,83,85,87,89,84,90,91,74,72,94,78,93,86,97,92,98,82,88,76,96,106,95,100,102,104,80,108,110,112,114,116,111,117,118,101,99,121,105,120,113,124,119,125,109,115,103,123,133,122,127,129,131,107,135,137,139,141,143,138,144,145,128,126,148,132,147,140,151,146,152,136,142,130,150,160,149,154,156,158,134,162,164,166,168,170,165,171,172,155,153,175,159,174,167,178,173,179,163,169,157,177,187,176,181,183,185,161,189,191,193,195,197,192,198,199,182,180,202,186,201,194,205,200,206,190,196,184,204,214,203,208,210,212,188,216,218,220,222,224,219,225,226,209,207,229,213,228,221,232,227,233,217,223,211,231,241,230,235,237,239,215,243,245,247,249,251,246,252,253,236,234,3,240,255,248,2,254,6,244]
    listamena=[251,9,10,250,243,13,4,12,5,16,11,17,1,7,0,15,25,18,19,14,21,20,23,24,8,22,26,30,36,37,29,33,40,31,39,32,43,38,44,28,34,27,42,52,45,46,41,48,47,50,51,35,49,53,57,63,64,56,60,67,58,66,59,70,65,71,55,61,54,69,79,72,73,68,75,74,77,78,62,76,80,84,90,91,83,87,94,85,93,86,97,92,98,82,88,81,96,106,99,100,95,102,101,104,105,89,103,107,111,117,118,110,114,121,112,120,113,124,119,125,109,115,108,123,133,126,127,122,129,128,131,132,116,130,134,138,144,145,137,141,148,139,147,140,151,146,152,136,142,135,150,160,153,154,149,156,155,158,159,143,157,161,165,171,172,164,168,175,166,174,167,178,173,179,163,169,162,177,187,180,181,176,183,182,185,186,170,184,188,192,198,199,191,195,202,193,201,194,205,200,206,190,196,189,204,214,207,208,203,210,209,212,213,197,211,215,219,225,226,218,222,229,220,228,221,232,227,233,217,223,216,231,241,234,235,230,237,236,239,240,224,238,242,246,252,253,245,249,0,247,255,248,0,254,4,244]
   
    return listanum

def pasar_a_binario(texto):
    final=[]
    for i in texto:
        i=str(i)
        i=ord(i)
        i=bin(i)
        i=str(i)
        i=i.replace("b","")
        final.append(i)
    return final

def encriptar_mensaje(mensaje1):
    listanumfinal=""
    listanum=ordenar_lista()
    mensaje=pasar_a_binario(mensaje1)
    for i in listanum:
        i=int(i)
        i=bin(i)
        i=str(i)
        i=i.replace("b","")
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


def tarea(tablero):
    #Aqui empieza tu tarea
    clave = '38872805571643309'
    usuario = '@cicontreras2'
    print(conectar("@cicontreras2","38872805571643309"))
    emisor('@cicontreras2')
    while True:
        click=esperar_click()
        if click=="enviar":
            mensaje1=mensaje_redactado()
            if len(mensaje1)<=246:
                mensajecodif=encriptar_mensaje(mensaje1)
                print(enviar_mensaje(mensajecodif))
                print(validar_encriptacion(mensaje1,mensajecodif))
                print(mensajecodif)
                borrar_mensaje_redactado()
##        if click=="recibidos":
##            for i in range(1,cantidad_recibidos()):
##                agregar_mensaje_al_final(
##            
##        if click=="enviados":
##            for i in range(1,int(cantidad_enviados())):
                
        
    	
	#Aqui termina tu tarea
app = whatsintro_gui.Application("tarea")
app.title('WhatsIntro')
app.loadProgram(tarea)
app.start()
