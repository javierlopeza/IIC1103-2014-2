import copy

def super5filas(matriz):
    n_filas=len(matriz)
    n_columnas=len(matriz[0])
    nueva=[]
    aux=copy.deepcopy(matriz)
    f5=n_filas/5
    c5=n_columnas/5
    porciones=int(f5*c5)
    for i in range(0,5):
        nueva.append(aux[i])
    return nueva
        
original=[[(11,2,3),(1,22,3),(1,2,33),(1,2,34),(1,2,35),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)],[(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3),(1,2,3)]]

print(super5filas(original))
print(len(super5filas(original)))

def super5columnas(matriz):
    n_filas=len(matriz)
    n_columnas=len(matriz[0])
    nueva=[]
    aux=copy.deepcopy(matriz)
    f5=n_filas/5
    c5=n_columnas/5
    porciones=int(f5*c5)
    for i in range(0,5):
        fila=[]
        for j in range(0,5):
            fila.append(aux[i][j])
        nueva.append(fila)
    return nueva

print(super5columnas(original))
print(len(super5columnas(original)))
