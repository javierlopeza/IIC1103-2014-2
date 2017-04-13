import copy

def cortar5x5(original):
    cortada=copy.deepcopy(original)
    n_filas=len(original)
    n_columnas=len(original[0])
    print(n_filas,n_columnas)
    filas5=(int((n_filas)/5))*5
    columnas5=(int((n_columnas)/5))*5
    print(filas5,columnas5)
    cortada=cortada[:filas5]
    for i in range(filas5):
        cortada[i]=cortada[i][:columnas5]
    return cortada

#funcion que calcula la diferencia entre 2 pixeles
def diferencia_colores(p1,p2):
    r1=p1[0]
    g1=p1[1]
    b1=p1[2]
    r2=p2[0]
    g2=p2[1]
    b2=p2[2]
    R=((r1-r2)**2)+((g1-g2)**2)+((b1-b2)**2)
    return (R)

#calcular las diferencias entre las porciones de la imagen y 1 mosaico
#y cambiar alguna de esas porciones por el mosaico si su diferencia es menor a 10
def diferencia(original, lista_mosaicos):
    cambiada=copy.deepcopy(original)
    n_filas=len(original)
    n_columnas=len(original[0])
    for m in range(len(lista_mosaicos)):
        for i in range(0, n_filas, 5):
            for j in range(0, n_columnas, 5):
                total=0
                for n in range(0,5):
                    for nn in range(0,5):
                        d=diferencia_colores(original[i+n][j+nn], lista_mosaicos[m][n,nn])
                        total+=d
                        
                #MUY CAMBIABLE
                    #esto
                VF=1
                while VF==1:
                    for rango in range(0, 10):
                        if total+rango==0 or total-rango==0::
                            for t in range(0,5):
                                for tt in range(0,5):
                                    cambiada[i+n][j+nn]=lista_mosaicos[m][t][tt]
                            VF=0
    return cambiada


            
            
        
