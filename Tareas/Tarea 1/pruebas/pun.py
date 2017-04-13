import math
def ptje_ficha(x):
    if x>2:
        i=int(math.log((x/3), 2))
        pX=(3**(i+1))
        return (pX)
    elif x<3:
        pX=0
        return (pX)
a=2
b=6
c=1
d=12
pA=ptje_ficha(a)
pB=ptje_ficha(b)
pC=ptje_ficha(c)
pD=ptje_ficha(d)



puntaje=(pA + pB + pC + pD)

print(puntaje)
