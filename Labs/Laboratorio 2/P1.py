import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
if a==b and b==c:
    print('3')
elif a==b and b!=c:
    print('2')
elif b==c and a!=b:
    print('2')
elif a==c and a!=b:
    print('2')
else:
    print('0')

