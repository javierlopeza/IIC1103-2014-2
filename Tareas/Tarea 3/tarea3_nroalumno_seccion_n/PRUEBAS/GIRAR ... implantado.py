import instaintro_gui
import copy

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
def mosaicos(original, lista_mosaicos):
    lista=[]
    coincidencias=0
    cambiada=copy.deepcopy(original)
    n_filas=len(original)
    n_columnas=len(original[0])
    for m in range(len(lista_mosaicos)):
        for i in range(0, n_filas, 5):
            for j in range(0, n_columnas, 5):
                total=0
                #el "total" corresponde a la diferencia de las porciones (suma de las diferencias de los colores de cada pixel correspondiente)
                for n in range(0,5):
                    for nn in range(0,5):
                        d=diferencia_colores(cambiada[i+n][j+nn], lista_mosaicos[m][n][nn])
                        total+=d
                lista.append(total)       
                #MUY CAMBIABLE
                    #esto
                if total<10000:
                    coincidencias+=1
                    print("COINCIDENCIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa!!!")
                    for t in range(0,5):
                        for tt in range(0,5):
                            cambiada[i+t][j+tt]=lista_mosaicos[m][t][tt]
        print(m)
    lista.sort()
    print("El mas chico es;",lista[0])
    print("coincidencias", coincidencias)
    return(cambiada)
                
        
def tarea():
	# Aqui empieza tu tarea
    while True:
        click=instaintro_gui.esperar_click()
        if click=="salir":
            instaintro_gui.salir()
        if click=="girar":
            matriz_pixeles=instaintro_gui.obtener_pixeles()
            if  matriz_pixeles!=None:
                matriz_imagen_girada=girar_imagen(matriz_pixeles)
                instaintro_gui.actualizar_imagen(matriz_imagen_girada)
        if click=="mosaico":
            matriz_pixeles=instaintro_gui.obtener_pixeles()
            matriz_cortada=cortar5x5(matriz_pixeles)
            instaintro_gui.actualizar_imagen(matriz_cortada)
            matriz_cortada=instaintro_gui.obtener_pixeles()
            lista_mosaicos= instaintro_gui.obtener_imagenes_mosaico()
            matriz_mosaicos=mosaicos(matriz_cortada, lista_mosaicos)
            instaintro_gui.actualizar_imagen(matriz_mosaicos)

app = instaintro_gui.Application("tarea")
app.title('InstaIntro')
app.loadProgram(tarea)
app.start()
