import whatsintro_gui
import whatsintro_msg
import random

def tarea(tablero):
    #Aqui empieza tu tarea
    usuario = "@jilopez8"
    clave = "8681307185584869"
    conectar = whatsintro_msg.conectar(usuario, clave)
    conectar
    a="javier lopez achondo"
    b="36434628211001110010011010100001010110110101100100100000100010110101101100011111110111111001101010011010010010001101110100011101110111000001100100011110010111001001111101"
    validar_encriptacion=whatsintro_msg.validar_encriptacion(a, b)
    while conectar==True:
        s = "Usuario conectado: " + usuario
        emisor = whatsintro_gui.emisor(s)
        VF=1
        click = whatsintro_gui.esperar_click()
        while VF==1:
            if click=='enviar':
                print("click en boton enviar")
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
                mensaje_encriptado=str(mensaje_a_enviar)
                
                whatsintro_msg.enviar_mensaje(mensaje_encriptado)

                print(whatsintro_msg.enviar_mensaje(mensaje_encriptado))

                if whatsintro_msg.enviar_mensaje(mensaje_encriptado)==(True, 'mensaje enviado'):
                    whatsintro_gui.borrar_mensaje_redactado()
                               
                VF=0
                
            if click=='enviados':
                whatsintro_gui.borrar_lista_mensajes()
                
                cantidad_enviados=int(whatsintro_msg.cantidad_enviados())
                print("Cantidad de enviados es:", cantidad_enviados)

                for k in range(0, cantidad_enviados):
                    texto_enviado=(whatsintro_msg.mensaje_enviado(k))

                    texto_enviado_lista=texto_enviado.split()
                    
                    de=texto_enviado_lista[0]
                    para=texto_enviado_lista[1]
                    msg_sin_decodificar=texto_enviado_lista[2]

                    print(de)
                    print(para)
                    print(msg_sin_decodificar)

                    #Mensaje recibido codificado
                    mensaje_recibido_codificado=msg_sin_decodificar
                    mrecod=mensaje_recibido_codificado
                    #Le quito la cadena aleatoria de los 10 primeros numeros
                    mrecibido=mrecod[10:]
                    cadena_aleatoria_entrante=mrecod[:10]
                    cae=cadena_aleatoria_entrante
                    clave="8681307185584869"
                    #Para la cadena de inicio entrante(E) cocateno la clave con la cadena aleatoria
                    secuencia_a_repetir_entrante=clave+cae
                    secrepe=secuencia_a_repetir_entrante
                    cadena_de_inicio_entrante=(9*secrepe)+clave
                    cdie=cadena_de_inicio_entrante
                    for n in range(0,6):
                        cdie=cdie+(cae[n])
                    #LISTA DE NUMEROS E
                    lista_de_numeros_e=[]
                    ldne=lista_de_numeros_e
                    for r in range(0,256):
                        ldne=ldne+[r]
                    #Cambio de orden de numeros en lista de numeros   V2:
                    for i in range(0, 256):
                        nueva_posicion=int(i+int(cdie[i]))
                        np=nueva_posicion
                        if np<256:
                            gi=ldne[np]
                            ldne[np]=ldne[i]
                            ldne[i]=gi
                        elif np>=256:
                            np=int(np-256)
                            gi=ldne[np]
                            ldne[np]=ldne[i]
                            ldne[i]=gi
                    #codificacion de lista de numeros desordenados a codigo binario cada numero:
                    for i in range(0,256):
                        ldne[i]=bin(ldne[i])
                        ldne[i]=ldne[i].split("b")
                        ldne[i]=ldne[i][1]
                        while len(ldne[i])<8:
                            ldne[i]=("0"+ldne[i])
                    #cocatenacion de los numeros binarios correspondientes a los de la lista de numeros de 0 a 255 cambiados de orden
                    cocatenado_ndesordenados_binarios_e=""
                    ccnbe=cocatenado_ndesordenados_binarios_e
                    for nb in range(0, 256):
                        ccnbe=ccnbe+ldne[nb]
                    ldnbine=ccnbe
                    ### MENSAJE RECIBIDO CODIFICADO (sin sec aleatoria): mrecibido
                    ### CADENA ALEATORIA ENTRANTE: cae
                    ### CLAVE: clave
                    ### CADENA DE INICIO ENTRANTE: cdie
                    ### LISTA DE NUMEROS EN BINARIO ENTRANTE: ldnbine
                    #Ahora debo comparar la lista de numeros en binario entrante con el mensaje
                    #recibido codificado:
                    #Si el mensaje codificado posee un 1 en la posicion i y la lista de n posee
                    #un 0 o un 1 entonces el mensaje recibido decodificado tendra un 1 o un 0
                    #respectivamente.
                    #Si el mensaje codificado posee un 0 en la posicion i y la lista de n posee
                    #un 0 o un 1 entonces el mensaje recibido decodificado tendra un 0 o un 1
                    #respectivamente.
                    #DECODIFICACION MENSAJE RECIBIDO A BINARIO:
                    mrecbin=""
                    for i in range(0, len(mrecibido)):
                        if mrecibido[i]=="0":
                            if ldnbine[i]=="0":
                                mrecbin=mrecbin+("0")
                            if ldnbine[i]=="1":
                                mrecbin=mrecbin+("1")
                        if mrecibido[i]=="1":
                            if ldnbine[i]=="0":
                                mrecbin=mrecbin+("1")
                            if ldnbine[i]=="1":
                                mrecbin=mrecbin+("0")
                    mensaje_recibido_decodificado=""
                    mrecdec=mensaje_recibido_decodificado
                    codigo_binario_letra=""
                    codbinl=codigo_binario_letra
                    for n in range(0, len(mrecbin)):
                        codbinl=codbinl+mrecbin[n]
                        if len(codbinl)==8:
                            ASCIId=int(codbinl, 2)
                            letra_dec=chr(ASCIId)
                            mrecdec=mrecdec+letra_dec
                            codbinl=""
                    msg=mrecdec
                    print(msg)
                    
                    whatsintro_gui.agregar_mensaje_al_final(de, para, msg)
                    
                VF=0

            if click=='recibidos':
                t1=(whatsintro_msg.mensaje_enviado(0))
                t2=(whatsintro_msg.mensaje_enviado(1))
                t3=(whatsintro_msg.mensaje_enviado(2))
                print(t1)
                print(t2)
                print(t3)
                VF=0
        
        
            
        
    
    
app = whatsintro_gui.Application("tarea")
app.title('WhatsIntro')
app.loadProgram(tarea)
app.start()
