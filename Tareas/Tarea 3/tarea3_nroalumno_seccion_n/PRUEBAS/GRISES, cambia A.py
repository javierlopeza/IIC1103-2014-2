def escala_grises(matriz):
    grises=matriz[:]
    aux=matriz[:]
    n_filas=len(grises)
    n_columnas=len(grises[0])
    for i in range(n_filas):
        for j in range(n_columnas):
            promedioRGB=int(((aux[i][j][0])+(aux[i][j][1])+(aux[i][j][2]))/3)
            grises[i][j]=(promedioRGB, promedioRGB, promedioRGB)
            print(matriz)
    return (grises)
                

original=[[(1,2,3),(11,22,33)],[(22,222,222),(3,33,3)],[(4,44,4),(1,11,11)],[(123,21,2),(4,5,4)],[(4,6,9),(0,1,5)],[(1,7,0),(1,5,9)],[(1,4,0),(1,44,72)]]
b=escala_grises(original)
print("ORIGINAL REAL", original, "\n")
print("GRISES", b,"\n")
print("ORIGINAL, se cambian los valores \n", original)
