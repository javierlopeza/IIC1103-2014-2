import sys

n=int(sys.stdin.readline())
 
def es_primo(p):
    if(n==1):
        return False
    i=2
    while i<p:
        if (p%i)==0:
            return False
        i+=1
    return True
 
def es_mala_onda(md):
    j=1
    while j<=md:
        if (md%j)==0:
            if es_primo(j)==True:
                if j>6:
                    return False
        j+=1
    return True
k=0
i=0
while k<n:
    i+=1
    if es_mala_onda(i)==True:
        k+=1
print(i)
