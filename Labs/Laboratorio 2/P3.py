import sys
a = float(sys.stdin.readline())
b = float(sys.stdin.readline())
c = float(sys.stdin.readline())
if a==0:
    print('no es ecuacion cuadratica')
elif ((b**2)-(4*a*c))>0:
    print('ecuacion cuadratica con raices reales distintas')
elif ((b**2)-(4*a*c))==0:
    print('ecuacion cuadratica con raices reales iguales')
elif ((b**2)-(4*a*c))<0:
    print('ecuacion cuadratica con raices complejas')
