import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
if a<(b+c) and b<(a+c) and c<(a+b) and a>((((b-c)**2))**(1/2)) and b>((((c-a)**2))**(1/2)) and c>((((b-a)**2))**(1/2)):
    print('True')
else:
    print('False')
