import sys
polinomio=str(sys.stdin.readline()).strip()
num=int(sys.stdin.readline())
 
 #reemplazar sumas y espacios
polinomio=polinomio.replace(' ','')
polinomio=polinomio.split('+')
suma=0
for i in range(len(polinomio)):
    polinomio_1=polinomio[i]
    polinomio_2=polinomio_1.split('*x^')
    constante=int(polinomio_2[0])
    exponente=int(polinomio_2[1])
    suma_parcial=constante*(num**exponente)
    suma+=suma_parcial
 
 
print(suma)
        
