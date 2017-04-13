import sys

#Problema 1:
a = float(sys.stdin.readline())
b = float(sys.stdin.readline())
h = (((a*a)+(b*b))**0.5)
print(h)


#Problema 2:
n = int(sys.stdin.readline())
if n%2==0:
    print('True')
else:
    print('False')

    
#Problema 3:
p = float(sys.stdin.readline())
r = ((p**3)+(3*(p**2))+(6*p)-2-(0.5*(p**2))-4)
print(r)


#Problema 4:
u = float(sys.stdin.readline())
t = (((3*u)+2)/(u+1))**(1/3)
print(t)
