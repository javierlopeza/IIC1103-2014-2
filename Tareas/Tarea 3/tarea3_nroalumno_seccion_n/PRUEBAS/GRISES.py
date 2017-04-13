def escala_grises(matriz):
    grises=matriz
    n_filas=len(matriz)
    n_columnas=len(matriz[0])
    for i in range(n_filas):
        for j in range(n_columnas):
            promedioRGB=int((int(matriz[i][j][0])+int(matriz[i][j][1])+int(matriz[i][j][2]))/3)
            grises[i][j]=(promedioRGB, promedioRGB, promedioRGB)
    return (grises)
                

original=[[(1,2,3),(11,22,33)],[(22,222,222),(3,33,3)],[(4,44,4),(1,11,11)],[(123,21,2),(4,5,4)],[(4,6,9),(0,1,5)],[(1,7,0),(1,5,9)],[(1,4,0),(1,44,72)]]
print(original)
print(escala_grises(original))
