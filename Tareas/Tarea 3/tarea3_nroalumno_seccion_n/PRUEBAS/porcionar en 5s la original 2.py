import copy

def porcionar5(matriz):
    n_filas=len(matriz)
    n_columnas=len(matriz[0])
    nueva=[]
    aux=copy.deepcopy(matriz)
    f5=n_filas/5
    c5=n_columnas/5
    porciones=int(f5*c5)
    for p in range(porciones):
        minimatriz=[]
        for i in range(n_filas):
            minifila=[]
            while len(minifila)<6:
                for j in range(n_columnas):
                    if (p+1)*i<n_filas and (p+1)*j<n_columnas:
                        E=aux[(p+1)*i][(p+1)*j]
                        print(E)
                        minifila.append(E)
            minimatriz.append(minifila)
        nueva.append(minimatriz)
    print(nueva)
    return nueva
        
    
            
            
                
        
    
porcion=[[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)]]
mosaico=[[(4,5,6),(4,5,6),(4,5,6),(4,5,6),(4,5,6)],[(4,5,6),(4,5,6),(4,5,6),(4,5,6),(4,5,6)],[(4,5,6),(4,5,6),(4,5,6),(4,5,6),(4,5,6)],[(4,5,6),(4,5,6),(4,5,6),(4,5,6),(4,5,6)],[(4,5,6),(4,5,6),(4,5,6),(4,5,6),(4,5,6)]]

original=[[(11,2,3),(1,22,3),(1,2,33),(1,2,34),(1,2,35),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)]]

print(porcionar5(original))
