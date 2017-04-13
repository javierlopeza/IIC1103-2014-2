import string
import random

#Cadena aleatoria


counter=0
cadenaaleatoria=""
for i in range (0,10):
    number=random.randint(0,9)
    cadenaaleatoria+=str(number)
    counter=1+counter
print(cadenaaleatoria)


    

#Cadena de inicio

clave="705954849672"
cadenainicio=clave+cadenaaleatoria

while len(cadenainicio)<=256:
    cadenainicio+=clave+cadenaaleatoria

cadenainicio=cadenainicio[0:256]


#Lista

lista=[]

for i in range(0,256):
    lista.append(i)


#Cambio

for i in range(0,256):
    if i+int(cadenainicio[i])<256:
        j=i+int(cadenainicio[i])
    elif i+int(cadenainicio[i])>=256:
        j=i+int(cadenainicio[i])-256
    cadenainicio[i],cadenainicio[j]=cadenainicio[j],cadenainicio[i]
    
    
#Transformacion ASCII BINARIO

msj=mensaje_redactado()
binario=""
for i in msj:
    i=ord(i)
    i=bin(i)
    i=str(i)
    i=i.replace("b","")
    binario+=i

#Desde Aquí vas a estar hasta el pico con tu Tarea

    


