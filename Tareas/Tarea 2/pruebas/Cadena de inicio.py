
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
print("CADENA DE INICIO")
print(cdi)
print(len(cdi))


