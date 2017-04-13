
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
print(len(cdi))




#LISTA DE NUMEROS
lista_de_numeros=[]
ldn=lista_de_numeros

for r in range(0,256):
    ldn=ldn+[r]

print("LISTA DE NUMEROS ORDENADOS:")
print(ldn)

#Cambio de orden de numeros en lista de numeros    V1:
#cadena de inicio auxiliar
cdi_aux=2*cdi
r=0
while r<257:
    r=0
    nueva_posicion=r+int(cdi_aux[r])
    np=nueva_posicion
    gpos=ldn[r]
    ldn[r]=ldn[np]
    ldn[np]=gpos
    r+=1

print("LISTA DE NUMEROS CAMBIADOS DE ORDEN:")
print(ldn)

#Cambio de orden de numeros en lista de numeros   V2:
#cadena de inicio auxiliar
cdi_aux=2*cdi

for h in range(256):
    nueva_posicion=r+int(cdi_aux[r])
    np=nueva_posicion
    gpos=ldn[r]
    ldn[r]=ldn[np]
    ldn[np]=gpos
    r+=1

print("LISTA DE NUMEROS CAMBIADOS DE ORDEN:")
print(ldn)

















