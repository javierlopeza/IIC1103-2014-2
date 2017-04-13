def girar_imagen(matriz):
        n_filas=len(matriz)
        n_columnas=len(matriz[0])
        #AGREGAR CANTIDAD DE COLUMNAS:
        original_girada=[]
        for i in range(n_columnas):
                AG=[None]
                original_girada.append(AG)   
        #AGREGAR CANTIDAD DE FILAS:
        for j in range(len(original_girada)):
                for k in range(n_filas-1, -1, -1):
                        AG=matriz[k][j]
                        original_girada[j].append(AG)
        #BORRAR ELEMENTO REPETIDO:
        for h in range(len(original_girada)):
                del original_girada[h][0]
        return(original_girada)


original=[[(1,2,3),(11,22,33)],[(22,222,222),(3,33,3)],[(4,44,4),(1,11,11)],[(123,21,2),(4,5,4)],[(4,6,9),(0,1,5)],[(1,7,0),(1,5,9)],[(1,4,0),(1,44,72)]]
print(original)
print(girar_imagen(original))
