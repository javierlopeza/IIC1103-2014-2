import sys

b1=int(sys.stdin.readline())
b2=int(sys.stdin.readline())
b3=int(sys.stdin.readline())
b4=int(sys.stdin.readline())
b5=int(sys.stdin.readline())
m1=int(sys.stdin.readline())
m2=int(sys.stdin.readline())
m3=int(sys.stdin.readline())
m4=int(sys.stdin.readline())
m5=int(sys.stdin.readline())

pagar=int(sys.stdin.readline())
pagado=int(sys.stdin.readline())

vuelto=pagado-pagar

if vuelto>=20000 and b1>0:
    if (vuelto/20000)<=b1:
        b1=vuelto//20000
        vuelto=vuelto-(20000*b1)

    elif (vuelto/20000)>b1:
        b1=b1
        vuelto=vuelto-(20000*b1)

    print(b1)
    print(20000)

if vuelto>=10000 and b2>0:
    if (vuelto/10000)<=b2:
        b2=vuelto//10000
        vuelto=vuelto-(10000*b2)

    elif (vuelto/10000)>b2:
        b2=b2
        vuelto=vuelto-(10000*b2)

    print(b2)
    print(10000)

if vuelto>=5000 and b3>0:
    if (vuelto/5000)<=b3:
        b3=vuelto//5000
        vuelto=vuelto-(5000*b3)

    elif (vuelto/5000)>b3:
        b3=b3
        vuelto=vuelto-(5000*b3)

    print(b3)
    print(5000)

if vuelto>=2000 and b4>0:
    if (vuelto/2000)<=b4:
        b4=vuelto//2000
        vuelto=vuelto-(2000*b4)

    elif (vuelto/2000)>b4:
        b4=b4
        vuelto=vuelto-(2000*b4)

    print(b4)
    print(2000)

if vuelto>=1000 and b5>0:
    if (vuelto/1000)<=b5:
        b5=vuelto//1000
        vuelto=vuelto-(1000*b5)

    elif (vuelto/1000)>b5:
        b5=b5
        vuelto=vuelto-(1000*b5)

    print(b5)
    print(1000)

if vuelto>=500 and m1>0:
    if (vuelto/500)<=m1:
        m1=vuelto//500
        vuelto=vuelto-(500*m1)

    elif (vuelto/500)>m1:
        m1=m1
        vuelto=vuelto-(500*m1)

    print(m1)
    print(500)

if vuelto>=100 and m2>0:
    if (vuelto/100)<=m2:
        m2=vuelto//100
        vuelto=vuelto-(100*m2)

    elif (vuelto/100)>m2:
        m2=m2
        vuelto=vuelto-(100*m2)

    print(m2)
    print(100)

if vuelto>=50 and m3>0:
    if (vuelto/50)<=m3:
        m3=vuelto//50
        vuelto=vuelto-(50*m3)

    elif (vuelto/50)>m3:
        m3=m3
        vuelto=vuelto-(50*m3)

    print(m3)
    print(50)

if vuelto>=10 and m4>0:
    if (vuelto/10)<=m4:
        m4=vuelto//10
        vuelto=vuelto-(10*m4)

    elif (vuelto/10)>m4:
        m4=m4
        vuelto=vuelto-(10*m4)

    print(m4)
    print(10)

if vuelto>=1 and m5>0:
    if (vuelto/1)<=m5:
        m5=vuelto//1
        vuelto=vuelto-(1*m5)

    elif (vuelto/1)>m5:
        m5=m5
        vuelto=vuelto-(1*m5)

    print(m5)
    print(1)

else:




