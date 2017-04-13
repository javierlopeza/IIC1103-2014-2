
import random

cadena_aleatoria=""
ca=cadena_aleatoria

#mientras la cadena aleatoria formada tenga una longitud menor a 10 cocatenarle
#otro numero entre 0 y 9

while len(ca)<10:
    numero_aleatorio=random.randint(0, 9)
    na=str(numero_aleatorio)
    ca=ca+na
    
print(ca)
