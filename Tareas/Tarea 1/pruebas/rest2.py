(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)=(1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16)
v=True
if v==True:
    f11=(a>2 and b>2 and a==b) or (a<2 and b<2 and a!=b)
    f12=(b>2 and c>2 and b==c) or (b<2 and c<2 and b!=c)
    f13=(c>2 and d>2 and c==d) or (c<2 and d<2 and c!=d)
    f21=(e>2 and f>2 and e==f) or (e<2 and f<2 and e!=f)
    f22=(f>2 and g>2 and f==g) or (f<2 and g<2 and f!=g)
    f23=(g>2 and h>2 and g==h) or (g<2 and h<2 and g!=h)
    f31=(i>2 and j>2 and i==j) or (i<2 and j<2 and i!=j)
    f32=(j>2 and k>2 and j==k) or (j<2 and k<2 and j!=k)
    f33=(k>2 and l>2 and k==l) or (k<2 and l<2 and k!=l) 
    f41=(m>2 and n>2 and m==n) or (m<2 and n<2 and m!=n)
    f42=(n>2 and o>2 and n==o) or (n<2 and o<2 and n!=o)
    f43=(o>2 and p>2 and o==p) or (o<2 and p<2 and o!=p)

    c11=(a>2 and e>2 and a==e) or (a<2 and e<2 and a!=e)
    c12=(e>2 and i>2 and e==i) or (e<2 and i<2 and e!=i)
    c13=(i>2 and m>2 and i==m) or (i<2 and m<2 and i!=m)
    c21=(b>2 and f>2 and b==f) or (b<2 and f<2 and b!=f)
    c22=(f>2 and j>2 and f==j) or (f<2 and j<2 and f!=j)
    c23=(j>2 and n>2 and j==n) or (j<2 and n<2 and j!=n)
    c31=(c>2 and g>2 and c==g) or (c<2 and g<2 and c!=g)
    c32=(g>2 and k>2 and g==k) or (g<2 and k<2 and g!=k)
    c33=(k>2 and o>2 and k==o) or (k<2 and o<2 and k!=o)
    c41=(d>2 and h>2 and d==h) or (d<2 and h<2 and d!=h)
    c42=(h>2 and l>2 and h==l) or (h<2 and l<2 and h!=l)
    c43=(l>2 and p>2 and l==p) or (l<2 and p<2 and l!=p)

    fT = f11 or f12 or f13 or f21 or f22 or f23 or f31 or f32 or f33 or f41 or f42 or f43
    cT = c11 or c12 or c13 or c21 or c22 or c23 or c31 or c32 or c33 or c41 or c42 and c43
    dC = a==0 or b==0 or c==0 or d==0 or e==0 or f==0 or g==0 or h==0 or i==0 or j==0 or k==0 or l==0 or m==0 or n==0 or o==0 or p==0 

    fcT = fT or cT
    
    if (fcT) and dC==True:
        print("TODO BIEN BIEN")
    else:
        print("TODO MAL :(")
        
