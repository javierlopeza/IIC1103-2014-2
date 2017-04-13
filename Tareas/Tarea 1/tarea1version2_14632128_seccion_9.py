import tableroGUI
tablero = None 
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = (0,)*16
puntaje = 0
def inicia_juego():
    global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p = tablero.inicia_juego()

def actualizar_tablero():
    global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p
    tablero.update(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p, puntaje)

def esperar_presionar_tecla():
    return tablero.esperarPresionarTecla()  
    
def aleatorio():
    return tablero.aleatorio()

def tarea(tablero):
    global puntaje,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p
    
    #Aqui empieza tu tarea

    inicia_juego()
    import random
    actualizar_tablero()
    while 1+1==2:
        import math
        def ptje_ficha(x):
            if x>2:
                i=int(math.log((x/3), 2))
                pX=(3**(i+1))
                return (pX)
            elif x<3:
                pX=0
                return (pX)
        pA=ptje_ficha(a)
        pB=ptje_ficha(b)
        pC=ptje_ficha(c)
        pD=ptje_ficha(d)
        pE=ptje_ficha(e)
        pF=ptje_ficha(f)
        pG=ptje_ficha(g)
        pH=ptje_ficha(h)
        pI=ptje_ficha(i)
        pJ=ptje_ficha(j)
        pK=ptje_ficha(k)
        pL=ptje_ficha(l)
        pM=ptje_ficha(m)
        pN=ptje_ficha(n)
        pO=ptje_ficha(o)
        pP=ptje_ficha(p)

        puntaje=int(pA+pB+pC+pD+pE+pF+pG+pH+pI+pJ+pK+pL+pM+pN+pO+pP)
        actualizar_tablero()
        tecla=esperar_presionar_tecla()
        val=True
        al=False
        while val==True:
            if tecla=='izquierda':
                (A,B,C,D)=(a,b,c,d)
                (E,F,G,H)=(e,f,g,h)
                (I,J,K,L)=(i,j,k,l)
                (M,N,O,P)=(m,n,o,p)
                if ((a==b and a>2 and b>2) or (a==1 and b==2) or (a==2 and b==1)):
                    a+=b
                    b=c
                    c=d
                    d=0
                elif a==0:
                    a=b
                    b=c
                    c=d
                    d=0
                elif ((b==c and b>2 and c>2) or (b==1 and c==2) or (b==2 and c==1)):
                    b+=c
                    c=d
                    d=0
                elif b==0:
                    b=c
                    c=d
                    d=0
                elif ((c==d and c>2 and d>2) or (c==1 and d==2) or (c==2 and d==1)):
                    c+=d
                    d=0
                elif c==0:
                    c=d
                    d=0
                        
                if ((e==f and e>2 and f>2) or (e==1 and f==2) or (e==2 and f==1)):
                    e+=f
                    f=g
                    g=h
                    h=0
                elif e==0:
                    (e,f,g,h)=(f,g,h,0)
                elif ((f==g and f>2 and g>2) or (f==1 and g==2) or (f==2 and g==1)):
                    f+=g
                    g=h
                    h=0
                elif f==0:
                    (f,g,h)=(g,h,0)
                elif ((g==h and g>2 and h>2) or (g==1 and h==2) or (g==2 and h==1)):
                    g+=h
                    h=0
                elif g==0:
                    (g,h)=(h,0)
                    
                if ((i==j and i>2 and j>2) or (i==1 and j==2) or (i==2 and j==1)):
                    i+=j
                    j=k
                    k=l
                    l=0
                elif i==0:
                    (i,j,k,l)=(j,k,l,0)
                elif ((j==k and j>2 and k>2) or (j==1 and k==2) or (j==2 and k==1)):
                    j+=k
                    k=l
                    l=0
                elif j==0:
                    (j,k,l)=(k,l,0)
                elif ((k==l and k>2 and l>2) or (k==1 and l==2) or (k==2 and l==1)):
                    k+=l
                    l=0
                elif k==0:
                    (k,l)=(l,0)
                   
                if ((m==n and m>2 and n>2) or (m==1 and n==2) or (m==2 and n==1)):
                    m+=n
                    n=o
                    o=p
                    p=0
                elif m==0:
                    (m,n,o,p)=(n,o,p,0)
                elif ((n==o and n>2 and o>2) or (n==1 and o==2) or (n==2 and o==1)):
                    n+=o
                    o=p
                    p=0
                elif n==0:
                    (n,o,p)=(o,p,0)
                elif ((o==p and o>2 and p>2) or (o==1 and p==2) or (o==2 and p==1)):
                    o+=p
                    p=0
                elif o==0:
                    (o,p)=(p,0)


                if ((A,B,C,D)!=(a,b,c,d) or (E,F,G,H)!=(e,f,g,h) or (I,J,K,L)!=(i,j,k,l) or (M,N,O,P)!=(m,n,o,p)):
                    al=True
                if al==True:
                    R=False
                    if (A,B,C,D)!=(a,b,c,d) and (E,F,G,H)!=(e,f,g,h) and (I,J,K,L)!=(i,j,k,l) and (M,N,O,P)!=(m,n,o,p):
                        aleatarriba = ["d","h","l","p"]
                        R=True
                        
                    if (A,B,C,D)==(a,b,c,d) and (E,F,G,H)!=(e,f,g,h) and (I,J,K,L)!=(i,j,k,l) and (M,N,O,P)!=(m,n,o,p):
                        aleatarriba = ["h","l","p"]
                        R=True
                    if (A,B,C,D)!=(a,b,c,d) and (E,F,G,H)==(e,f,g,h) and (I,J,K,L)!=(i,j,k,l) and (M,N,O,P)!=(m,n,o,p):
                        aleatarriba = ["d","l","p"]
                        R=True
                    if (A,B,C,D)!=(a,b,c,d) and (E,F,G,H)!=(e,f,g,h) and (I,J,K,L)==(i,j,k,l) and (M,N,O,P)!=(m,n,o,p):
                        aleatarriba = ["d","h","p"]
                        R=True
                    if (A,B,C,D)!=(a,b,c,d) and (E,F,G,H)!=(e,f,g,h) and (I,J,K,L)!=(i,j,k,l) and (M,N,O,P)==(m,n,o,p):
                        aleatarriba = ["d","h","l"]
                        R=True
                        
                    if (A,B,C,D)==(a,b,c,d) and (E,F,G,H)==(e,f,g,h) and (I,J,K,L)!=(i,j,k,l) and (M,N,O,P)!=(m,n,o,p):
                        aleatarriba = ["l","p"]
                        R=True
                    if (A,B,C,D)!=(a,b,c,d) and (E,F,G,H)!=(e,f,g,h) and (I,J,K,L)==(i,j,k,l) and (M,N,O,P)==(m,n,o,p):
                        aleatarriba = ["h","d"]
                        R=True
                    if (A,B,C,D)==(a,b,c,d) and (E,F,G,H)!=(e,f,g,h) and (I,J,K,L)!=(i,j,k,l) and (M,N,O,P)==(m,n,o,p):
                        aleatarriba = ["l","h"]
                        R=True
                    if (A,B,C,D)!=(a,b,c,d) and (E,F,G,H)==(e,f,g,h) and (I,J,K,L)==(i,j,k,l) and (M,N,O,P)!=(m,n,o,p):
                        aleatarriba = ["d","p"]
                        R=True
                    if (A,B,C,D)==(a,b,c,d) and (E,F,G,H)!=(e,f,g,h) and (I,J,K,L)==(i,j,k,l) and (M,N,O,P)!=(m,n,o,p):
                        aleatarriba = ["h","p"]
                        R=True
                    if (A,B,C,D)!=(a,b,c,d) and (E,F,G,H)==(e,f,g,h) and (I,J,K,L)!=(i,j,k,l) and (M,N,O,P)==(m,n,o,p):
                        aleatarriba = ["l","d"]
                        R=True
                        
                    if (A,B,C,D)==(a,b,c,d) and (E,F,G,H)==(e,f,g,h) and (I,J,K,L)==(i,j,k,l) and (M,N,O,P)!=(m,n,o,p):
                        p=aleatorio()
                    if (A,B,C,D)==(a,b,c,d) and (E,F,G,H)==(e,f,g,h) and (I,J,K,L)!=(i,j,k,l) and (M,N,O,P)==(m,n,o,p):
                        l=aleatorio()
                    if (A,B,C,D)!=(a,b,c,d) and (E,F,G,H)==(e,f,g,h) and (I,J,K,L)==(i,j,k,l) and (M,N,O,P)==(m,n,o,p):
                        d=aleatorio()
                    if (A,B,C,D)==(a,b,c,d) and (E,F,G,H)!=(e,f,g,h) and (I,J,K,L)==(i,j,k,l) and (M,N,O,P)==(m,n,o,p):
                        h=aleatorio()
                        
                    if R==True:
                        eleccionizq = random.choice(aleatarriba)
                        if (eleccionizq == "ad"):
                            d=aleatorio()
                        elif (eleccionizq == "h"):
                            h=aleatorio()
                        elif (eleccionizq == "l"):
                            l=aleatorio()
                        elif (eleccionizq == "p"):
                            p=aleatorio()
                        R=False
                        
                al=False    
                val=False



            if tecla=='derecha':
                (A,B,C,D)=(a,b,c,d)
                (E,F,G,H)=(e,f,g,h)
                (I,J,K,L)=(i,j,k,l)
                (M,N,O,P)=(m,n,o,p)
                if ((c==d and c>2 and d>2) or (c==1 and d==2) or (c==2 and d==1)):
                    d+=c
                    c=b
                    b=a
                    a=0
                elif d==0:
                    d=c
                    c=b
                    b=a
                    a=0
                elif ((b==c and b>2 and c>2) or (b==1 and c==2) or (b==2 and c==1)):
                    c+=b
                    b=a
                    a=0
                elif c==0:
                    c=b
                    b=a
                    a=0
                elif ((a==b and a>2 and b>2) or (a==1 and b==2) or (a==2 and b==1)):
                    b+=a
                    a=0
                elif b==0:
                    b=a
                    a=0
                        
                if ((h==g and h>2 and g>2) or (h==1 and g==2) or (h==2 and g==1)):
                    h+=g
                    g=f
                    f=e
                    e=0
                elif h==0:
                    (e,f,g,h)=(0,e,f,g)
                elif ((f==g and f>2 and g>2) or (f==1 and g==2) or (f==2 and g==1)):
                    g+=f
                    f=e
                    e=0
                elif g==0:
                    (e,f,g,h)=(0,e,f,h)
                elif ((e==f and e>2 and f>2) or (e==1 and f==2) or (e==2 and f==1)):
                    f+=e
                    e=0
                elif f==0:
                    (e,f)=(0,e)
                        
                if ((l==k and l>2 and k>2) or (l==1 and k==2) or (l==2 and k==1)):
                    l+=k
                    k=j
                    j=i
                    i=0
                elif l==0:
                    (i,j,k,l)=(0,i,j,k)
                elif ((j==k and j>2 and k>2) or (j==1 and k==2) or (j==2 and k==1)):
                    k+=j
                    j=i
                    i=0
                elif k==0:
                    (i,j,k)=(0,i,j)
                elif ((i==j and i>2 and j>2) or (i==1 and j==2) or (i==2 and j==1)):
                    j+=i
                    i=0
                elif j==0:
                    (i,j)=(0,i)
                    
                if ((o==p and o>2 and p>2) or (o==1 and p==2) or (o==2 and p==1)):
                    p+=o
                    o=n
                    n=m
                    m=0
                elif p==0:
                    (m,n,o,p)=(0,m,n,o)
                elif ((n==o and n>2 and o>2) or (n==1 and o==2) or (n==2 and o==1)):
                    o+=n
                    n=m
                    m=0
                elif o==0:
                    (m,n,o,p)=(0,m,n,p)
                elif ((m==n and m>2 and n>2) or (m==1 and n==2) or (m==2 and n==1)):
                    n+=m
                    m=0
                elif n==0:
                    (m,n)=(0,m)

                if ((A,B,C,D)!=(a,b,c,d) or (E,F,G,H)!=(e,f,g,h) or (I,J,K,L)!=(i,j,k,l) or (M,N,O,P)!=(m,n,o,p)):
                    al=True
                if al==True:
                    R=False
                    if (A,B,C,D)!=(a,b,c,d) and (E,F,G,H)!=(e,f,g,h) and (I,J,K,L)!=(i,j,k,l) and (M,N,O,P)!=(m,n,o,p):
                        aleatarriba = ["a","e","i","m"]
                        R=True
                        
                    if (A,B,C,D)==(a,b,c,d) and (E,F,G,H)!=(e,f,g,h) and (I,J,K,L)!=(i,j,k,l) and (M,N,O,P)!=(m,n,o,p):
                        aleatarriba = ["e","i","m"]
                        R=True
                    if (A,B,C,D)!=(a,b,c,d) and (E,F,G,H)==(e,f,g,h) and (I,J,K,L)!=(i,j,k,l) and (M,N,O,P)!=(m,n,o,p):
                        aleatarriba = ["a","i","m"]
                        R=True
                    if (A,B,C,D)!=(a,b,c,d) and (E,F,G,H)!=(e,f,g,h) and (I,J,K,L)==(i,j,k,l) and (M,N,O,P)!=(m,n,o,p):
                        aleatarriba = ["a","e","m"]
                        R=True
                    if (A,B,C,D)!=(a,b,c,d) and (E,F,G,H)!=(e,f,g,h) and (I,J,K,L)!=(i,j,k,l) and (M,N,O,P)==(m,n,o,p):
                        aleatarriba = ["a","e","i"]
                        R=True
                        
                    if (A,B,C,D)==(a,b,c,d) and (E,F,G,H)==(e,f,g,h) and (I,J,K,L)!=(i,j,k,l) and (M,N,O,P)!=(m,n,o,p):
                        aleatarriba = ["i","m"]
                        R=True
                    if (A,B,C,D)!=(a,b,c,d) and (E,F,G,H)!=(e,f,g,h) and (I,J,K,L)==(i,j,k,l) and (M,N,O,P)==(m,n,o,p):
                        aleatarriba = ["e","a"]
                        R=True
                    if (A,B,C,D)==(a,b,c,d) and (E,F,G,H)!=(e,f,g,h) and (I,J,K,L)!=(i,j,k,l) and (M,N,O,P)==(m,n,o,p):
                        aleatarriba = ["i","e"]
                        R=True
                    if (A,B,C,D)!=(a,b,c,d) and (E,F,G,H)==(e,f,g,h) and (I,J,K,L)==(i,j,k,l) and (M,N,O,P)!=(m,n,o,p):
                        aleatarriba = ["a","m"]
                        R=True
                    if (A,B,C,D)==(a,b,c,d) and (E,F,G,H)!=(e,f,g,h) and (I,J,K,L)==(i,j,k,l) and (M,N,O,P)!=(m,n,o,p):
                        aleatarriba = ["e","m"]
                        R=True
                    if (A,B,C,D)!=(a,b,c,d) and (E,F,G,H)==(e,f,g,h) and (I,J,K,L)!=(i,j,k,l) and (M,N,O,P)==(m,n,o,p):
                        aleatarriba = ["i","a"]
                        R=True
                        
                    if (A,B,C,D)==(a,b,c,d) and (E,F,G,H)==(e,f,g,h) and (I,J,K,L)==(i,j,k,l) and (M,N,O,P)!=(m,n,o,p):
                        m=aleatorio()
                    if (A,B,C,D)==(a,b,c,d) and (E,F,G,H)==(e,f,g,h) and (I,J,K,L)!=(i,j,k,l) and (M,N,O,P)==(m,n,o,p):
                        i=aleatorio()
                    if (A,B,C,D)!=(a,b,c,d) and (E,F,G,H)==(e,f,g,h) and (I,J,K,L)==(i,j,k,l) and (M,N,O,P)==(m,n,o,p):
                        a=aleatorio()
                    if (A,B,C,D)==(a,b,c,d) and (E,F,G,H)!=(e,f,g,h) and (I,J,K,L)==(i,j,k,l) and (M,N,O,P)==(m,n,o,p):
                        e=aleatorio()
                        
                    if R==True:
                        eleccionderecha = random.choice(aleatarriba)
                        if (eleccionderecha == "a"):
                            a=aleatorio()
                        elif (eleccionderecha == "e"):
                            e=aleatorio()
                        elif (eleccionderecha == "i"):
                            i=aleatorio()
                        elif (eleccionderecha == "m"):
                            m=aleatorio()
                        R=False
                        
                al=False    
                val=False


               
            if tecla=='abajo':
                (A,E,I,M)=(a,e,i,m)
                (B,F,J,N)=(b,f,j,n)
                (C,G,K,O)=(c,g,k,o)
                (D,H,L,P)=(d,h,l,p)
                if ((m==i and m>2 and i>2) or (m==1 and i==2) or (m==2 and i==1)):
                    m+=i
                    i=e
                    e=a
                    a=0
                elif m==0:
                    m=i
                    i=e
                    e=a
                    a=0
                elif ((e==i and e>2 and i>2) or (e==1 and i==2) or (e==2 and i==1)):
                    i+=e
                    e=a
                    a=0
                elif i==0:
                    i=e
                    e=a
                    a=0
                elif ((a==e and a>2 and e>2) or (a==1 and e==2) or (a==2 and e==1)):
                    e+=a
                    a=0
                elif e==0:
                    e=a
                    a=0
                        
                if ((n==j and n>2 and j>2) or (n==1 and j==2) or (n==2 and j==1)):
                    n+=j
                    j=f
                    f=b
                    b=0
                elif n==0:
                    n=j
                    j=f
                    f=b
                    b=0
                elif ((f==j and f>2 and j>2) or (f==1 and j==2) or (f==2 and j==1)):
                    j+=f
                    f=b
                    b=0
                elif j==0:
                    j=f
                    f=b
                    b=0
                elif ((b==f and b>2 and f>2) or (b==1 and f==2) or (b==2 and f==1)):
                    f+=b
                    b=0
                elif f==0:
                    f=b
                    b=0
                        
                if ((o==k and o>2 and k>2) or (o==1 and k==2) or (o==2 and k==1)):
                    o+=k
                    k=g
                    g=c
                    c=0
                elif o==0:
                    o=k
                    k=g
                    g=c
                    c=0
                elif ((g==k and g>2 and k>2) or (g==1 and k==2) or (g==2 and k==1)):
                    k+=g
                    g=c
                    c=0
                elif k==0:
                    k=g
                    g=c
                    c=0
                elif ((c==g and c>2 and g>2) or (c==1 and g==2) or (c==2 and g==1)):
                    g+=c
                    c=0
                elif g==0:
                    g=c
                    c=0
                    
                if ((p==l and p>2 and l>2) or (p==1 and l==2) or (p==2 and l==1)):
                    p+=l
                    l=h
                    h=d
                    d=0
                elif p==0:
                    p=l
                    l=h
                    h=d
                    d=0
                elif ((h==l and h>2 and l>2) or (h==1 and l==2) or (h==2 and l==1)):
                    l+=h
                    h=d
                    d=0
                elif l==0:
                    l=h
                    h=d
                    d=0
                elif ((d==h and d>2 and h>2) or (d==1 and h==2) or (d==2 and h==1)):
                    h+=d
                    d=0
                elif h==0:
                    h=d
                    d=0


                if ((A,E,I,M)!=(a,e,i,m) or (B,F,J,N)!=(b,f,j,n) or (C,G,K,O)!=(c,g,k,o) or (D,H,L,P)!=(d,h,l,p)):
                    al=True
                if al==True:
                    R=False
                    if (A,E,I,M)!=(a,e,i,m) and (B,F,J,N)!=(b,f,j,n) and (C,G,K,O)!=(c,g,k,o) and (D,H,L,P)!=(d,h,l,p):
                        aleatarriba = ["a","b","c","d"]
                        R=True
                        
                    if (A,E,I,M)==(a,e,i,m) and (B,F,J,N)!=(b,f,j,n) and (C,G,K,O)!=(c,g,k,o) and (D,H,L,P)!=(d,h,l,p):
                        aleatarriba = ["b","c","d"]
                        R=True
                    if (A,E,I,M)!=(a,e,i,m) and (B,F,J,N)==(b,f,j,n) and (C,G,K,O)!=(c,g,k,o) and (D,H,L,P)!=(d,h,l,p):
                        aleatarriba = ["a","c","d"]
                        R=True
                    if (A,E,I,M)!=(a,e,i,m) and (B,F,J,N)!=(b,f,j,n) and (C,G,K,O)==(c,g,k,o) and (D,H,L,P)!=(d,h,l,p):
                        aleatarriba = ["a","b","d"]
                        R=True
                    if (A,E,I,M)!=(a,e,i,m) and (B,F,J,N)!=(b,f,j,n) and (C,G,K,O)!=(c,g,k,o) and (D,H,L,P)==(d,h,l,p):
                        aleatarriba = ["a","b","c"]
                        R=True
                        
                    if (A,E,I,M)==(a,e,i,m) and (B,F,J,N)==(b,f,j,n) and (C,G,K,O)!=(c,g,k,o) and (D,H,L,P)!=(d,h,l,p):
                        aleatarriba = ["c","d"]
                        R=True
                    if (A,E,I,M)!=(a,e,i,m) and (B,F,J,N)!=(b,f,j,n) and (C,G,K,O)==(c,g,k,o) and (D,H,L,P)==(d,h,l,p):
                        aleatarriba = ["b","a"]
                        R=True
                    if (A,E,I,M)==(a,e,i,m) and (B,F,J,N)!=(b,f,j,n) and (C,G,K,O)!=(c,g,k,o) and (D,H,L,P)==(d,h,l,p):
                        aleatarriba = ["c","b"]
                        R=True
                    if (A,E,I,M)!=(a,e,i,m) and (B,F,J,N)==(b,f,j,n) and (C,G,K,O)==(c,g,k,o) and (D,H,L,P)!=(d,h,l,p):
                        aleatarriba = ["a","d"]
                        R=True
                    if (A,E,I,M)==(a,e,i,m) and (B,F,J,N)!=(b,f,j,n) and (C,G,K,O)==(c,g,k,o) and (D,H,L,P)!=(d,h,l,p):
                        aleatarriba = ["b","d"]
                        R=True
                    if (A,E,I,M)!=(a,e,i,m) and (B,F,J,N)==(b,f,j,n) and (C,G,K,O)!=(c,g,k,o) and (D,H,L,P)==(d,h,l,p):
                        aleatarriba = ["c","a"]
                        R=True
                        
                    if (A,E,I,M)==(a,e,i,m) and (B,F,J,N)==(b,f,j,n) and (C,G,K,O)==(c,g,k,o) and (D,H,L,P)!=(d,h,l,p):
                        d=aleatorio()
                    if (A,E,I,M)==(a,e,i,m) and (B,F,J,N)==(b,f,j,n) and (C,G,K,O)!=(c,g,k,o) and (D,H,L,P)==(d,h,l,p):
                        c=aleatorio()
                    if (A,E,I,M)!=(a,e,i,m) and (B,F,J,N)==(b,f,j,n) and (C,G,K,O)==(c,g,k,o) and (D,H,L,P)==(d,h,l,p):
                        a=aleatorio()
                    if (A,E,I,M)==(a,e,i,m) and (B,F,J,N)!=(b,f,j,n) and (C,G,K,O)==(c,g,k,o) and (D,H,L,P)==(d,h,l,p):
                        b=aleatorio()
                        
                    if R==True:
                        eleccionabajo = random.choice(aleatarriba)
                        if (eleccionabajo == "a"):
                            a=aleatorio()
                        elif (eleccionabajo == "b"):
                            b=aleatorio()
                        elif (eleccionabajo == "c"):
                            c=aleatorio()
                        elif (eleccionabajo == "d"):
                            d=aleatorio()
                        R=False
                        
                al=False    
                val=False


            if tecla=='arriba':
                (A,E,I,M)=(a,e,i,m)
                (B,F,J,N)=(b,f,j,n)
                (C,G,K,O)=(c,g,k,o)
                (D,H,L,P)=(d,h,l,p)
                if ((a==e and a>2 and e>2) or (a==1 and e==2) or (a==2 and e==1)):
                    a+=e
                    e=i
                    i=m
                    m=0
                elif a==0:
                    a=e
                    e=i
                    i=m
                    m=0
                elif ((e==i and e>2 and i>2) or (e==1 and i==2) or (e==2 and i==1)):
                    e+=i
                    i=m
                    m=0
                elif e==0:
                    e=i
                    i=m
                    m=0
                elif ((i==m and i>2 and m>2) or (i==1 and m==2) or (i==2 and m==1)):
                    i+=m
                    m=0
                elif i==0:
                    i=m
                    m=0
                        
                if ((b==f and b>2 and f>2) or (b==1 and f==2) or (b==2 and f==1)):
                    b+=f
                    f=j
                    j=n
                    n=0
                elif b==0:
                    b=f
                    f=j
                    j=n
                    n=0
                elif ((f==j and f>2 and j>2) or (f==1 and j==2) or (f==2 and j==1)):
                    f+=j
                    j=n
                    n=0
                elif f==0:
                    f=j
                    j=n
                    n=0
                elif ((j==n and j>2 and n>2) or (j==1 and n==2) or (j==2 and n==1)):
                    j+=n
                    n=0
                elif j==0:
                    j=n
                    n=0

                if ((c==g and c>2 and g>2) or (c==1 and g==2) or (c==2 and g==1)):
                    c+=g
                    g=k
                    k=o
                    o=0
                elif c==0:
                    c=g
                    g=k
                    k=o
                    o=0
                elif ((g==k and g>2 and k>2) or (g==1 and k==2) or (g==2 and k==1)):
                    g+=k
                    k=o
                    o=0
                elif g==0:
                    g=k
                    k=o
                    o=0
                elif ((k==o and k>2 and o>2) or (k==1 and o==2) or (k==2 and o==1)):
                    k+=o
                    o=0
                elif k==0:
                    k=o
                    o=0

                if ((d==h and d>2 and h>2) or (d==1 and h==2) or (d==2 and h==1)):
                    d+=h
                    h=l
                    l=p
                    p=0
                elif d==0:
                    d=h
                    h=l
                    l=p
                    p=0
                elif ((h==l and h>2 and l>2) or (h==1 and l==2) or (h==2 and l==1)):
                    h+=l
                    k=p
                    p=0
                elif h==0:
                    h=l
                    l=p
                    p=0
                elif ((l==p and l>2 and p>2) or (l==1 and p==2) or (l==2 and p==1)):
                    l+=p
                    p=0
                elif l==0:
                    l=p
                    p=0

                
                if ((A,E,I,M)!=(a,e,i,m) or (B,F,J,N)!=(b,f,j,n) or (C,G,K,O)!=(c,g,k,o) or (D,H,L,P)!=(d,h,l,p)):
                    al=True
                if al==True:
                    R=False
                    if (A,E,I,M)!=(a,e,i,m) and (B,F,J,N)!=(b,f,j,n) and (C,G,K,O)!=(c,g,k,o) and (D,H,L,P)!=(d,h,l,p):
                        aleatarriba = ["m","n","o","p"]
                        R=True
                        
                    if (A,E,I,M)==(a,e,i,m) and (B,F,J,N)!=(b,f,j,n) and (C,G,K,O)!=(c,g,k,o) and (D,H,L,P)!=(d,h,l,p):
                        aleatarriba = ["n","o","p"]
                        R=True
                    if (A,E,I,M)!=(a,e,i,m) and (B,F,J,N)==(b,f,j,n) and (C,G,K,O)!=(c,g,k,o) and (D,H,L,P)!=(d,h,l,p):
                        aleatarriba = ["m","o","p"]
                        R=True
                    if (A,E,I,M)!=(a,e,i,m) and (B,F,J,N)!=(b,f,j,n) and (C,G,K,O)==(c,g,k,o) and (D,H,L,P)!=(d,h,l,p):
                        aleatarriba = ["m","n","p"]
                        R=True
                    if (A,E,I,M)!=(a,e,i,m) and (B,F,J,N)!=(b,f,j,n) and (C,G,K,O)!=(c,g,k,o) and (D,H,L,P)==(d,h,l,p):
                        aleatarriba = ["m","n","o"]
                        R=True
                        
                    if (A,E,I,M)==(a,e,i,m) and (B,F,J,N)==(b,f,j,n) and (C,G,K,O)!=(c,g,k,o) and (D,H,L,P)!=(d,h,l,p):
                        aleatarriba = ["o","p"]
                        R=True
                    if (A,E,I,M)!=(a,e,i,m) and (B,F,J,N)!=(b,f,j,n) and (C,G,K,O)==(c,g,k,o) and (D,H,L,P)==(d,h,l,p):
                        aleatarriba = ["n","m"]
                        R=True
                    if (A,E,I,M)==(a,e,i,m) and (B,F,J,N)!=(b,f,j,n) and (C,G,K,O)!=(c,g,k,o) and (D,H,L,P)==(d,h,l,p):
                        aleatarriba = ["o","n"]
                        R=True
                    if (A,E,I,M)!=(a,e,i,m) and (B,F,J,N)==(b,f,j,n) and (C,G,K,O)==(c,g,k,o) and (D,H,L,P)!=(d,h,l,p):
                        aleatarriba = ["m","p"]
                        R=True
                    if (A,E,I,M)==(a,e,i,m) and (B,F,J,N)!=(b,f,j,n) and (C,G,K,O)==(c,g,k,o) and (D,H,L,P)!=(d,h,l,p):
                        aleatarriba = ["n","p"]
                        R=True
                    if (A,E,I,M)!=(a,e,i,m) and (B,F,J,N)==(b,f,j,n) and (C,G,K,O)!=(c,g,k,o) and (D,H,L,P)==(d,h,l,p):
                        aleatarriba = ["o","m"]
                        R=True
                        
                    if (A,E,I,M)==(a,e,i,m) and (B,F,J,N)==(b,f,j,n) and (C,G,K,O)==(c,g,k,o) and (D,H,L,P)!=(d,h,l,p):
                        p=aleatorio()
                    if (A,E,I,M)==(a,e,i,m) and (B,F,J,N)==(b,f,j,n) and (C,G,K,O)!=(c,g,k,o) and (D,H,L,P)==(d,h,l,p):
                        o=aleatorio()
                    if (A,E,I,M)!=(a,e,i,m) and (B,F,J,N)==(b,f,j,n) and (C,G,K,O)==(c,g,k,o) and (D,H,L,P)==(d,h,l,p):
                        m=aleatorio()
                    if (A,E,I,M)==(a,e,i,m) and (B,F,J,N)!=(b,f,j,n) and (C,G,K,O)==(c,g,k,o) and (D,H,L,P)==(d,h,l,p):
                        n=aleatorio()
                        
                    if R==True:
                        eleccionarriba = random.choice(aleatarriba)
                        if (eleccionarriba == "m"):
                            m=aleatorio()
                        elif (eleccionarriba == "n"):
                            n=aleatorio()
                        elif (eleccionarriba == "o"):
                            o=aleatorio()
                        elif (eleccionarriba == "p"):
                            p=aleatorio()
                        R=False
                        
                al=False    
                val=False

                       
            actualizar_tablero()
            

    #Aqui termina tu tarea
    
tablero = tableroGUI.Application("tarea")
tablero.title('DCC - Threes')
tablero.loadProgram(tarea)
tablero.start()
