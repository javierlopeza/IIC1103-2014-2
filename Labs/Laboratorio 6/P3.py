import sys

NH=str(sys.stdin.readline())
NH=NH.split(" ")
N=int(NH[0])
H=int(NH[1])

pi=sys.stdin.readline()
px=pi.split(" ")
pni=(px[len(px)-1]).split("\n")
px[len(px)-1]=pni[0]    

pend_t=""
for v in range(0, H):
    p=sys.stdin.readline()
    py=p.split(" ")
    pn=(py[len(px)-1]).split("\n")
    py[len(px)-1]=pn[0]  
    #px1=px[0], px2=px[1], ... , pxN=px[N-1]
    #py1=py[0], py2=py[1], ... , pyN=py[N-1]
    pend=""
    for v in range(0, N-1):
        pxNn=float(px[v])
        pyNn=float(py[v])
        pxNn1=float(px[v+1])
        pyNn1=float(py[v+1])
        m=float(((pyNn1-pyNn))/((pxNn1-pxNn)))
        pend=pend+str(m)+" "
    pend_t=pend_t+"\n"+pend
print(pend_t[1:(len(pend_t)-1)])
        
        
        
    
    




    

