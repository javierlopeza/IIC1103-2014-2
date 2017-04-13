

#Mensaje recibido codificado
mensaje_recibido_codificado="897689821601100000011010001001101010010100"
mrecod=mensaje_recibido_codificado

#Le quito la cadena aleatoria de los 10 primeros numeros

mrecibido=mrecod[10:]
print(mrecibido)

cadena_aleatoria_entrante=mrecod[:10]
cae=cadena_aleatoria_entrante
print(cae)

clave="8681307185584869"


#Para la cadena de inicio entrante(E) cocateno la clave con la cadena aleatoria
secuencia_a_repetir_entrante=clave+cae
secrepe=secuencia_a_repetir_entrante
print(secrepe)
cadena_de_inicio_entrante=(9*secrepe)+clave
cdie=cadena_de_inicio_entrante
for n in range(0,6):
    cdie=cdie+(cae[n])
print(cdie)




#LISTA DE NUMEROS E
lista_de_numeros_e=[]
ldne=lista_de_numeros_e

for r in range(0,256):
    ldne=ldne+[r]

print(ldne)



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


print(ldne)



#codificacion de lista de numeros desordenados a codigo binario cada numero:

for i in range(0,256):
    ldne[i]=bin(ldne[i])
    ldne[i]=ldne[i].split("b")
    ldne[i]=ldne[i][1]
    while len(ldne[i])<8:
        ldne[i]=("0"+ldne[i])
     
print(ldne)



#cocatenacion de los numeros binarios correspondientes a los de la lista de numeros de 0 a 255 cambiados de orden

cocatenado_ndesordenados_binarios_e=""
ccnbe=cocatenado_ndesordenados_binarios_e
for nb in range(0, 256):
    ccnbe=ccnbe+ldne[nb]

ldnbine=ccnbe
print(ldnbine)



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

mensaje_recibido_binario=""
mrecbin=mensaje_recibido_binario
for i in range(0, len(mrecibido)):
    if mrecibido[i]==0:
        if ldnbine[i]==0:
            mrecbin=mrecbin+"0"
        elif ldnbine[i]==1:
            mrecbin=mrecbin+"1"
    elif mrecibido[i]==1:
        if ldnbine[i]==0:
            mrecbin=mrecbin+"1"
        elif ldnbine[i]==1:
            mrecbin=mrecbin+"0"
print(mrecbin)
    




































