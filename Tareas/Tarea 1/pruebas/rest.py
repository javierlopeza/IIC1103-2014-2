(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)=(1000,999,998,99,98,97,95,578,45,455,67,77,88,99,22,33)

f11=not(a>2 and b>2 and a==b) and not(a<2 and b<2 and a!=b)
f12=not(b>2 and c>2 and b==c) and not(b<2 and c<2 and b!=c)
f13=not(c>2 and d>2 and c==d) and not(c<2 and d<2 and c!=d)
f21=not(e>2 and f>2 and e==f) and not(e<2 and f<2 and e!=f)
f22=not(f>2 and g>2 and f==g) and not(f<2 and g<2 and f!=g)
f23=not(g>2 and h>2 and g==h) and not(g<2 and h<2 and g!=h)
f31=not(i>2 and j>2 and i==j) and not(i<2 and j<2 and i!=j)
f32=not(j>2 and k>2 and j==k) and not(j<2 and k<2 and j!=k)
f33=not(k>2 and l>2 and k==l) and not(k<2 and l<2 and k!=l) 
f41=not(m>2 and n>2 and m==n) and not(m<2 and n<2 and m!=n)
f42=not(n>2 and o>2 and n==o) and not(n<2 and o<2 and n!=o)
f43=not(o>2 and p>2 and o==p) and not(o<2 and p<2 and o!=p)

c11=not(a>2 and e>2 and a==e) and not(a<2 and e<2 and a!=e)
c12=not(e>2 and i>2 and e==i) and not(e<2 and i<2 and e!=i)
c13=not(i>2 and m>2 and i==m) and not(i<2 and m<2 and i!=m)
c21=not(b>2 and f>2 and b==f) and not(b<2 and f<2 and b!=f)
c22=not(f>2 and j>2 and f==j) and not(f<2 and j<2 and f!=j)
c23=not(j>2 and n>2 and j==n) and not(j<2 and n<2 and j!=n)
c31=not(c>2 and g>2 and c==g) and not(c<2 and g<2 and c!=g)
c32=not(g>2 and k>2 and g==k) and not(g<2 and k<2 and g!=k)
c33=not(k>2 and o>2 and k==o) and not(k<2 and o<2 and k!=o)
c41=not(d>2 and h>2 and d==h) and not(d<2 and h<2 and d!=h)
c42=not(h>2 and l>2 and h==l) and not(h<2 and l<2 and h!=l)
c43=not(l>2 and p>2 and l==p) and not(l<2 and p<2 and l!=p)

fT = f11 and f12 and f13 and f21 and f22 and f23 and f31 and f32 and f33 and f41 and f42 and f43
cT = c11 and c12 and c13 and c21 and c22 and c23 and c31 and c32 and c33 and c41 and c42 and c43

fcT = fT and cT

if (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)!=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) and fcT:

    dC = a==0 or b==0 or c==0 or d==0 or e==0 or f==0 or g==0 or h==0 or i==0 or j==0 or k==0 or l==0 or m==0 or n==0 or o==0 or p==0 
