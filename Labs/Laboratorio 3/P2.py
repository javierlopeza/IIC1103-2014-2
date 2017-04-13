import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

aa=0
bb=0
C=0
while a>0 and b>0:
    aa=a%10
    bb=b%10
    if aa+bb+C>9:
        C=C+1
    a=int(a/10)
    b=int(b/10)
print(C)
    
    
