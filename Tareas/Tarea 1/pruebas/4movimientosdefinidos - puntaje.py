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
    actualizar_tablero()
    while True:
        tecla=esperar_presionar_tecla()
        val=True
        while val==True:
            if tecla=='izquierda':
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
                val=False

            if tecla=='derecha':
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
                    n+=im
                    m=0
                elif n==0:
                    (m,n)=(0,m)
                val=False
                
            if tecla=='abajo':
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
                val=False

            if tecla=='arriba':
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
                val=False


            import math
            (pA,pB,pC,pD,pE,pF,pG,pH,pI,pJ,pK,pL,pM,pN,pO,pP)=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
            if a>2:
                ia=((math.log10(a/3))/math.log10(2))
                pA=3**(ia+1)
            if b>2:
                ib=((math.log10(b/3))/math.log10(2))
                pB=3**(ib+1)
            if c>2:
                ic=((math.log10(c/3))/math.log10(2))
                pC=3**(ic+1)
            if d>2:
                iD=((math.log10(d/3))/math.log10(2))
                pD=3**(iD+1)
            if e>2:
                ie=((math.log10(e/3))/math.log10(2))
                pE=3**(ie+1)
            if f>2:
                iF=((math.log10(f/3))/math.log10(2))
                pF=3**(iF+1)
            if g>2:
                ig=((math.log10(g/3))/math.log10(2))
                pG=3**(ig+1)
            if h>2:
                ih=((math.log10(h/3))/math.log10(2))
                pH=3**(ih+1)
            if i>2:
                ii=((math.log10(i/3))/math.log10(2))
                pI=3**(ii+1)
            if j>2:
                ij=((math.log10(j/3))/math.log10(2))
                pJ=3**(ij+1)
            if k>2:
                ik=((math.log10(k/3))/math.log10(2))
                pK=3**(ik+1)
            if l>2:
                il=((math.log10(l/3))/math.log10(2))
                pL=3**(il+1)
            if m>2:
                im=((math.log10(m/3))/math.log10(2))
                pM=3**(im+1)
            if n>2:
                iN=((math.log10(n/3))/math.log10(2))
                pN=3**(iN+1)
            if o>2:
                io=((math.log10(o/3))/math.log10(2))
                pO=3**(io+1)
            if p>2:
                ip=((math.log10(p/3))/math.log10(2))
                pP=3**(ip+1)

            puntaje=int(pA+pB+pC+pD+pE+pF+pG+pH+pI+pJ+pK+pL+pM+pN+pO+pP)

            
            actualizar_tablero()
            

    #Aqui termina tu tarea
    
tablero = tableroGUI.Application("tarea")
tablero.title('DCC - Threes')
tablero.loadProgram(tarea)
tablero.start()
