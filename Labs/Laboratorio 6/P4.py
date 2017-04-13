import sys

LK=str(sys.stdin.readline())
LK=LK.split(" ")
L=int(LK[0])
K=int(LK[1])

if L>2 and L<=100:
    lista_frases=[]
    for v in range(0, L):
        frase=str(sys.stdin.readline())
        frase=frase[:(len(frase)-1)]
        lista_frases.append(frase)

    respuesta_f=""
    
    for v in range(0, K):
        respuesta=0
        solicitud=str(sys.stdin.readline())
        solicitud=solicitud.split("-")
        solicitud=str(solicitud[1])
        solicitud=solicitud[:(len(solicitud)-1)]
        contador=0
        for n in range(0, L):
            if (lista_frases[n]).count(solicitud)!=0:
                contador+=1
        respuesta=contador/L
        respuesta=str(respuesta)
        respuesta=respuesta[0:4]
        respuesta_f=respuesta_f + str(respuesta) + "\n"

    RES=respuesta_f[:(len(respuesta_f)-1)]
    RES=RES.split("\n")
    for n in range(0, K):
        RES[n]=float(RES[n])
        print('%.2f' % (RES[n]))
            
            



    

