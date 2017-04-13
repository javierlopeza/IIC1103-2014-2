import sys


#n: base del numero ingresado
#m: numero ingresado
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())



#verificacion de datos bien ingresados
c=m
v=0
while c>0:
    if v<n:
        continuar=True
    else:
        continuar=False
    v = c%10
    c = int(c/10)


#datos mal ingresados
if continuar==False:
    malo=-1
    print(malo)


#datos bien ingresados
if continuar==True:
#teorema fundamental de la numeracion
    dg=0
    tf = 0
    while m>0:
        tf = tf + ((m%10)*(n**(dg)))
        m=int(m/10)
        dg+=1
    print(tf)
        
