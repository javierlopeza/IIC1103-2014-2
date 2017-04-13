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
    while True:      
        while True:
            tecla=esperar_presionar_tecla()
            val=True
            al=False
            while val==True:
                (A,B,C,D)=(a,b,c,d)
                (E,F,G,H)=(e,f,g,h)
                (I,J,K,L)=(i,j,k,l)
                (M,N,O,P)=(m,n,o,p)
                (A,E,I,M)=(a,e,i,m)
                (B,F,J,N)=(b,f,j,n)
                (C,G,K,O)=(c,g,k,o)
                (D,H,L,P)=(d,h,l,p)
                
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
                            if (eleccionizq == "d"):
                                d=aleatorio()
                            elif (eleccionizq == "h"):
                                h=aleatorio()
                            elif (eleccionizq == "l"):
                                l=aleatorio()
                            elif (eleccionizq == "p"):
                                p=aleatorio()
                            R=False
                            
                    
                    f11=(a>2 and b>2 and a==b) or (a<3 and b<3 and a!=b)
                    f12=(b>2 and c>2 and b==c) or (b<3 and c<3 and b!=c)
                    f13=(c>2 and d>2 and c==d) or (c<3 and d<3 and c!=d)
                    f21=(e>2 and f>2 and e==f) or (e<3 and f<3 and e!=f)
                    f22=(f>2 and g>2 and f==g) or (f<3 and g<3 and f!=g)
                    f23=(g>2 and h>2 and g==h) or (g<3 and h<3 and g!=h)
                    f31=(i>2 and j>2 and i==j) or (i<3 and j<3 and i!=j)
                    f32=(j>2 and k>2 and j==k) or (j<3 and k<3 and j!=k)
                    f33=(k>2 and l>2 and k==l) or (k<3 and l<3 and k!=l) 
                    f41=(m>2 and n>2 and m==n) or (m<3 and n<3 and m!=n)
                    f42=(n>2 and o>2 and n==o) or (n<3 and o<3 and n!=o)
                    f43=(o>2 and p>2 and o==p) or (o<3 and p<3 and o!=p)

                    c11=(a>2 and e>2 and a==e) or (a<3 and e<3 and a!=e)
                    c12=(e>2 and i>2 and e==i) or (e<3 and i<3 and e!=i)
                    c13=(i>2 and m>2 and i==m) or (i<3 and m<3 and i!=m)
                    c21=(b>2 and f>2 and b==f) or (b<3 and f<3 and b!=f)
                    c22=(f>2 and j>2 and f==j) or (f<3 and j<3 and f!=j)
                    c23=(j>2 and n>2 and j==n) or (j<3 and n<3 and j!=n)
                    c31=(c>2 and g>2 and c==g) or (c<3 and g<3 and c!=g)
                    c32=(g>2 and k>2 and g==k) or (g<3 and k<3 and g!=k)
                    c33=(k>2 and o>2 and k==o) or (k<3 and o<3 and k!=o)
                    c41=(d>2 and h>2 and d==h) or (d<3 and h<3 and d!=h)
                    c42=(h>2 and l>2 and h==l) or (h<3 and l<3 and h!=l)
                    c43=(l>2 and p>2 and l==p) or (l<3 and p<3 and l!=p)

                    if (a==0 or b==0 or c==0 or d==0 or e==0 or f==0 or g==0 or h==0 or i==0 or j==0 or k==0 or l==0 or m==0 or n==0 or o==0 or p==0)==False or f11==False or f12==False or f13==False or f21==False or f22==False or f23==False or f31==False or f32==False or f33==False or f41==False or f42==False or f43==False or c11==False or c12==False or c13==False or c21==False or c22==False or c23==False or c31==False or c32==False or c33==False or c41==False or c42==False or c43==False:
                        a="C"
                        b="A"
                        actualizar_tablero()
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
                            
                    
                    f11=(a>2 and b>2 and a==b) or (a<3 and b<3 and a!=b)
                    f12=(b>2 and c>2 and b==c) or (b<3 and c<3 and b!=c)
                    f13=(c>2 and d>2 and c==d) or (c<3 and d<3 and c!=d)
                    f21=(e>2 and f>2 and e==f) or (e<3 and f<3 and e!=f)
                    f22=(f>2 and g>2 and f==g) or (f<3 and g<3 and f!=g)
                    f23=(g>2 and h>2 and g==h) or (g<3 and h<3 and g!=h)
                    f31=(i>2 and j>2 and i==j) or (i<3 and j<3 and i!=j)
                    f32=(j>2 and k>2 and j==k) or (j<3 and k<3 and j!=k)
                    f33=(k>2 and l>2 and k==l) or (k<3 and l<3 and k!=l) 
                    f41=(m>2 and n>2 and m==n) or (m<3 and n<3 and m!=n)
                    f42=(n>2 and o>2 and n==o) or (n<3 and o<3 and n!=o)
                    f43=(o>2 and p>2 and o==p) or (o<3 and p<3 and o!=p)

                    c11=(a>2 and e>2 and a==e) or (a<3 and e<3 and a!=e)
                    c12=(e>2 and i>2 and e==i) or (e<3 and i<3 and e!=i)
                    c13=(i>2 and m>2 and i==m) or (i<3 and m<3 and i!=m)
                    c21=(b>2 and f>2 and b==f) or (b<3 and f<3 and b!=f)
                    c22=(f>2 and j>2 and f==j) or (f<3 and j<3 and f!=j)
                    c23=(j>2 and n>2 and j==n) or (j<3 and n<3 and j!=n)
                    c31=(c>2 and g>2 and c==g) or (c<3 and g<3 and c!=g)
                    c32=(g>2 and k>2 and g==k) or (g<3 and k<3 and g!=k)
                    c33=(k>2 and o>2 and k==o) or (k<3 and o<3 and k!=o)
                    c41=(d>2 and h>2 and d==h) or (d<3 and h<3 and d!=h)
                    c42=(h>2 and l>2 and h==l) or (h<3 and l<3 and h!=l)
                    c43=(l>2 and p>2 and l==p) or (l<3 and p<3 and l!=p)

                    if (a==0 or b==0 or c==0 or d==0 or e==0 or f==0 or g==0 or h==0 or i==0 or j==0 or k==0 or l==0 or m==0 or n==0 or o==0 or p==0)==False or f11==False or f12==False or f13==False or f21==False or f22==False or f23==False or f31==False or f32==False or f33==False or f41==False or f42==False or f43==False or c11==False or c12==False or c13==False or c21==False or c22==False or c23==False or c31==False or c32==False or c33==False or c41==False or c42==False or c43==False:
                        a="C"
                        b="A"
                        actualizar_tablero()
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
                            
                    
                    f11=(a>2 and b>2 and a==b) or (a<3 and b<3 and a!=b)
                    f12=(b>2 and c>2 and b==c) or (b<3 and c<3 and b!=c)
                    f13=(c>2 and d>2 and c==d) or (c<3 and d<3 and c!=d)
                    f21=(e>2 and f>2 and e==f) or (e<3 and f<3 and e!=f)
                    f22=(f>2 and g>2 and f==g) or (f<3 and g<3 and f!=g)
                    f23=(g>2 and h>2 and g==h) or (g<3 and h<3 and g!=h)
                    f31=(i>2 and j>2 and i==j) or (i<3 and j<3 and i!=j)
                    f32=(j>2 and k>2 and j==k) or (j<3 and k<3 and j!=k)
                    f33=(k>2 and l>2 and k==l) or (k<3 and l<3 and k!=l) 
                    f41=(m>2 and n>2 and m==n) or (m<3 and n<3 and m!=n)
                    f42=(n>2 and o>2 and n==o) or (n<3 and o<3 and n!=o)
                    f43=(o>2 and p>2 and o==p) or (o<3 and p<3 and o!=p)

                    c11=(a>2 and e>2 and a==e) or (a<3 and e<3 and a!=e)
                    c12=(e>2 and i>2 and e==i) or (e<3 and i<3 and e!=i)
                    c13=(i>2 and m>2 and i==m) or (i<3 and m<3 and i!=m)
                    c21=(b>2 and f>2 and b==f) or (b<3 and f<3 and b!=f)
                    c22=(f>2 and j>2 and f==j) or (f<3 and j<3 and f!=j)
                    c23=(j>2 and n>2 and j==n) or (j<3 and n<3 and j!=n)
                    c31=(c>2 and g>2 and c==g) or (c<3 and g<3 and c!=g)
                    c32=(g>2 and k>2 and g==k) or (g<3 and k<3 and g!=k)
                    c33=(k>2 and o>2 and k==o) or (k<3 and o<3 and k!=o)
                    c41=(d>2 and h>2 and d==h) or (d<3 and h<3 and d!=h)
                    c42=(h>2 and l>2 and h==l) or (h<3 and l<3 and h!=l)
                    c43=(l>2 and p>2 and l==p) or (l<3 and p<3 and l!=p)

                    if (a==0 or b==0 or c==0 or d==0 or e==0 or f==0 or g==0 or h==0 or i==0 or j==0 or k==0 or l==0 or m==0 or n==0 or o==0 or p==0)==False or f11==False or f12==False or f13==False or f21==False or f22==False or f23==False or f31==False or f32==False or f33==False or f41==False or f42==False or f43==False or c11==False or c12==False or c13==False or c21==False or c22==False or c23==False or c31==False or c32==False or c33==False or c41==False or c42==False or c43==False:
                        a="C"
                        b="A"
                        actualizar_tablero()
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


                    f11=(a>2 and b>2 and a==b) or (a<3 and b<3 and a!=b)
                    f12=(b>2 and c>2 and b==c) or (b<3 and c<3 and b!=c)
                    f13=(c>2 and d>2 and c==d) or (c<3 and d<3 and c!=d)
                    f21=(e>2 and f>2 and e==f) or (e<3 and f<3 and e!=f)
                    f22=(f>2 and g>2 and f==g) or (f<3 and g<3 and f!=g)
                    f23=(g>2 and h>2 and g==h) or (g<3 and h<3 and g!=h)
                    f31=(i>2 and j>2 and i==j) or (i<3 and j<3 and i!=j)
                    f32=(j>2 and k>2 and j==k) or (j<3 and k<3 and j!=k)
                    f33=(k>2 and l>2 and k==l) or (k<3 and l<3 and k!=l) 
                    f41=(m>2 and n>2 and m==n) or (m<3 and n<3 and m!=n)
                    f42=(n>2 and o>2 and n==o) or (n<3 and o<3 and n!=o)
                    f43=(o>2 and p>2 and o==p) or (o<3 and p<3 and o!=p)

                    c11=(a>2 and e>2 and a==e) or (a<3 and e<3 and a!=e)
                    c12=(e>2 and i>2 and e==i) or (e<3 and i<3 and e!=i)
                    c13=(i>2 and m>2 and i==m) or (i<3 and m<3 and i!=m)
                    c21=(b>2 and f>2 and b==f) or (b<3 and f<3 and b!=f)
                    c22=(f>2 and j>2 and f==j) or (f<3 and j<3 and f!=j)
                    c23=(j>2 and n>2 and j==n) or (j<3 and n<3 and j!=n)
                    c31=(c>2 and g>2 and c==g) or (c<3 and g<3 and c!=g)
                    c32=(g>2 and k>2 and g==k) or (g<3 and k<3 and g!=k)
                    c33=(k>2 and o>2 and k==o) or (k<3 and o<3 and k!=o)
                    c41=(d>2 and h>2 and d==h) or (d<3 and h<3 and d!=h)
                    c42=(h>2 and l>2 and h==l) or (h<3 and l<3 and h!=l)
                    c43=(l>2 and p>2 and l==p) or (l<3 and p<3 and l!=p)

                    if (a==0 or b==0 or c==0 or d==0 or e==0 or f==0 or g==0 or h==0 or i==0 or j==0 or k==0 or l==0 or m==0 or n==0 or o==0 or p==0)==False or f11==False or f12==False or f13==False or f21==False or f22==False or f23==False or f31==False or f32==False or f33==False or f41==False or f42==False or f43==False or c11==False or c12==False or c13==False or c21==False or c22==False or c23==False or c31==False or c32==False or c33==False or c41==False or c42==False or c43==False:
                        a="C"
                        b="A"
                        actualizar_tablero()
                    al=False    
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
