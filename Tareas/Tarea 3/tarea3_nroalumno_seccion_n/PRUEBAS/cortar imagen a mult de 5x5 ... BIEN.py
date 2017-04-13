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
