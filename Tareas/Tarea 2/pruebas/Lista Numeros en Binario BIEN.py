
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

#CADENA ALEATORIA
print("CADENA ALEATORIA:")
print(ca)


#CLAVE
print("CLAVE:")
clave = "8681307185584869"
print(clave)


#Formacion de secuencia de clave+cadena_aleatoria:
secuencia_a_repetir=clave+ca
secrep=secuencia_a_repetir
print("SECUENCIA A REPETIR:")
print(secrep)


#FORMACION CADENA DE INICIO
cadena_de_inicio=(9*secrep)+clave
cdi=cadena_de_inicio
for n in range(0,6):
    cdi=cdi+(ca[n])
print("CADENA DE INICIO:")
print(cdi)



#LISTA DE NUMEROS
lista_de_numeros=[]
ldn=lista_de_numeros

for r in range(0,256):
    ldn=ldn+[r]

print("LISTA DE NUMEROS ORDENADOS:")
print(ldn)



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

    
print("LISTA DE NUMEROS CAMBIADOS DE ORDEN:")
print(ldn)



#codificacion de lista de numeros desordenados a codigo binario cada numero:

for i in range(0,256):
    ldn[i]=bin(ldn[i])
    ldn[i]=ldn[i].split("b")
    ldn[i]=ldn[i][1]
    while len(ldn[i])<8:
        ldn[i]=("0"+ldn[i])
print("LISTA DE NUMEROS CAMBIADOS DE ORDEN EN CODIGO BINARIO:")        
print(ldn)



#cocatenacion de los numeros binarios correspondientes a los de la lista de numeros de 0 a 255 cambiados de orden

cocatenado_ndesordenados_binarios=""
ccnb=cocatenado_ndesordenados_binarios
for nb in range(0, 256):
    ccnb=ccnb+ldn[nb]
print("COCATENADO DE NUMEROS CAMBIADOS DE ORDEN EN CODIGO BINARIO:")
ldnbin=ccnb
print(ldnbin)





































