import instaintro_gui
import copy

#################################
#################################
#################################

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

#################################
#################################
#################################

def escala_grises(matriz):
    grises=copy.deepcopy(matriz)
    aux=copy.deepcopy(matriz)
    n_filas=len(matriz)
    n_columnas=len(matriz[0])
    for i in range(n_filas):
        for j in range(n_columnas):
            promedioRGB=((int(aux[i][j][0])+int(aux[i][j][1])+int(aux[i][j][2]))/3)
            grises[i][j]=(promedioRGB, promedioRGB, promedioRGB)
    return (grises)

#################################
#################################
#################################

#MULTIPLICACION DE TUPLAS POR ESCALAR (equivalente a escalar por vector)
def mult_tupla(e,tupla):
    t1=int(tupla[0])*e
    t2=int(tupla[1])*e
    t3=int(tupla[2])*e
    r=(t1,t2,t3)
    return (r)

#SUMA DE TUPLAS
def suma_tupla(f1,f2,f3,f4,f5,f6,f7,f8,f9):
    d1=int(f1[0])+int(f2[0])+int(f3[0])+int(f4[0])+int(f5[0])+int(f6[0])+int(f7[0])+int(f8[0])+int(f9[0])
    d2=int(f1[1])+int(f2[1])+int(f3[1])+int(f4[1])+int(f5[1])+int(f6[1])+int(f7[1])+int(f8[1])+int(f9[1])
    d3=int(f1[2])+int(f2[2])+int(f3[2])+int(f4[2])+int(f5[2])+int(f6[2])+int(f7[2])+int(f8[2])+int(f9[2])
    r=(d1,d2,d3)
    return (r)

#SUMA DE 2 TUPLAS
def suma_2_tupla(t1,t2):
    d1=int(t1[0])+int(t2[0])
    d2=int(t1[1])+int(t2[1])
    d3=int(t1[2])+int(t2[2])
    r=(d1,d2,d3)
    return (r)

#TUPLA ELEVADO A POTENCIA
def pot_tupla(e,tupla):
    t1=(tupla[0])**e
    t2=(tupla[1])**e
    t3=(tupla[2])**e
    r=((t1),(t2),(t3))
    return (r)

def gxy(a,b,c,d,e,f,g,h,ii,A):
    cero=(0,0,0)
    BN=escala_grises(A)
    Ap=copy.deepcopy(A)
    n_filas=len(A)
    n_columnas=len(A[0])
    for i in range(n_filas):
        for j in range(n_columnas):
            if (i-1)>(-1) and (j-1)>(-1) and (i+1)<(n_filas) and (j+1)<(n_columnas):
                aa=BN[i-1][j-1]
                bb=BN[i-1][j]
                cc=BN[i-1][j+1]
                dd=BN[i][j-1]
                ee=BN[i][j]
                ff=BN[i][j+1]
                gg=BN[i+1][j-1]
                hh=BN[i+1][j]
                iii=BN[i+1][j+1]
                NV1=(mult_tupla(a,aa))
                NV2=(mult_tupla(b,bb))
                NV3=(mult_tupla(c,cc))
                NV4=(mult_tupla(d,dd))
                NV5=(mult_tupla(e,ee))
                NV6=(mult_tupla(f,ff))
                NV7=(mult_tupla(g,gg))
                NV8=(mult_tupla(h,hh))
                NV9=(mult_tupla(ii,iii))
            #SOBREPASA ARRIBA
            elif not((i-1)>(-1)) and (j-1)>(-1) and (i+1)<(n_filas) and (j+1)<(n_columnas):
                dd=BN[i][j-1]
                ee=BN[i][j]
                ff=BN[i][j+1]
                gg=BN[i+1][j-1]
                hh=BN[i+1][j]
                iii=BN[i+1][j+1]
                NV1=cero
                NV2=cero
                NV3=cero
                NV4=(mult_tupla(d,dd))
                NV5=(mult_tupla(e,ee))
                NV6=(mult_tupla(f,ff))
                NV7=(mult_tupla(g,gg))
                NV8=(mult_tupla(h,hh))
                NV9=(mult_tupla(ii,iii))
            #SOBREPASA IZQUIERDA
            elif ((i-1)>(-1)) and not((j-1)>(-1)) and (i+1)<(n_filas) and (j+1)<(n_columnas):
                bb=BN[i-1][j]
                cc=BN[i-1][j+1]
                ee=BN[i][j]
                ff=BN[i][j+1]
                hh=BN[i+1][j]
                iii=BN[i+1][j+1]
                NV1=cero
                NV2=(mult_tupla(b,bb))
                NV3=(mult_tupla(c,cc))
                NV4=cero
                NV5=(mult_tupla(e,ee))
                NV6=(mult_tupla(f,ff))
                NV7=cero
                NV8=(mult_tupla(h,hh))
                NV9=(mult_tupla(ii,iii))
            #SOBREPASA ABAJO
            elif ((i-1)>(-1)) and ((j-1)>(-1)) and not((i+1)<(n_filas)) and (j+1)<(n_columnas):
                aa=BN[i-1][j-1]
                bb=BN[i-1][j]
                cc=BN[i-1][j+1]
                dd=BN[i][j-1]
                ee=BN[i][j]
                ff=BN[i][j+1]
                NV1=(mult_tupla(a,aa))
                NV2=(mult_tupla(b,bb))
                NV3=(mult_tupla(c,cc))
                NV4=(mult_tupla(d,dd))
                NV5=(mult_tupla(e,ee))
                NV6=(mult_tupla(f,ff))
                NV7=cero
                NV8=cero
                NV9=cero
            #SOBREPASA DERECHA
            elif (i-1)>(-1) and (j-1)>(-1) and (i+1)<(n_filas) and not((j+1)<(n_columnas)):
                aa=BN[i-1][j-1]
                bb=BN[i-1][j]
                dd=BN[i][j-1]
                ee=BN[i][j]
                gg=BN[i+1][j-1]
                hh=BN[i+1][j]
                NV1=(mult_tupla(a,aa))
                NV2=(mult_tupla(b,bb))
                NV3=cero
                NV4=(mult_tupla(d,dd))
                NV5=(mult_tupla(e,ee))
                NV6=cero
                NV7=(mult_tupla(g,gg))
                NV8=(mult_tupla(h,hh))
                NV9=cero
            #ESQUINA ARRIBA IZQUIERDA
            elif not((i-1)>(-1)) and not((j-1)>(-1)) and (i+1)<(n_filas) and (j+1)<(n_columnas):
                ee=BN[i][j]
                ff=BN[i][j+1]
                hh=BN[i+1][j]
                iii=BN[i+1][j+1]
                NV1=cero
                NV2=cero
                NV3=cero
                NV4=cero
                NV5=(mult_tupla(e,ee))
                NV6=(mult_tupla(f,ff))
                NV7=cero
                NV8=(mult_tupla(h,hh))
                NV9=(mult_tupla(ii,iii))
            #ESQUINA ABAJO IZQUIERDA
            elif ((i-1)>(-1)) and not((j-1)>(-1)) and not((i+1)<(n_filas)) and ((j+1)<(n_columnas)):
                bb=BN[i-1][j]
                cc=BN[i-1][j+1]
                ee=BN[i][j]
                ff=BN[i][j+1]
                NV1=cero
                NV2=(mult_tupla(b,bb))
                NV3=(mult_tupla(c,cc))
                NV4=cero
                NV5=(mult_tupla(e,ee))
                NV6=(mult_tupla(f,ff))
                NV7=cero
                NV8=cero
                NV9=cero
            #ESQUINA ARRIBA DERECHA
            elif not((i-1)>(-1)) and ((j-1)>(-1)) and ((i+1)<(n_filas)) and not((j+1)<(n_columnas)):
                dd=BN[i][j-1]
                ee=BN[i][j]
                gg=BN[i+1][j-1]
                hh=BN[i+1][j]
                NV1=cero
                NV2=cero
                NV3=cero
                NV4=(mult_tupla(d,dd))
                NV5=(mult_tupla(e,ee))
                NV6=cero
                NV7=(mult_tupla(g,gg))
                NV8=(mult_tupla(h,hh))
                NV9=cero
            #ESQUINA ABAJO DERECHA
            elif ((i-1)>(-1)) and ((j-1)>(-1)) and not((i+1)<(n_filas)) and not((j+1)<(n_columnas)):
                aa=BN[i-1][j-1]
                bb=BN[i-1][j]
                dd=BN[i][j-1]
                ee=BN[i][j]
                NV1=(mult_tupla(a,aa))
                NV2=(mult_tupla(b,bb))
                NV3=cero
                NV4=(mult_tupla(d,dd))
                NV5=(mult_tupla(e,ee))
                NV6=cero
                NV7=cero
                NV8=cero
                NV9=cero
            NV=suma_tupla(NV1,NV2,NV3,NV4,NV5,NV6,NV7,NV8,NV9)
            Ap[i][j]=NV
    return(Ap)
            
def bordes(A):
    print("Procesando bordes...")
    G=copy.deepcopy(A)
    gx=gxy(-1,0,1,-2,0,2,-1,0,1,A)
    gy=gxy(1,2,1,0,0,0,-1,-2,-1,A)
    n_filas=len(A)
    n_columnas=len(A[0])
    for i in range(n_filas):
        for j in range(n_columnas):
            C1=pot_tupla(2,gx[i][j])
            C2=pot_tupla(2,gy[i][j])
            S=suma_2_tupla(C1,C2)
            R=pot_tupla(1/2, S)
            G[i][j]=(R)
    H=copy.deepcopy(G)
    #Normalizacion de las tuplas
    for i in range(n_filas):
        for j in range(n_columnas):
            L=[]
            t1=G[i][j][0]
            t2=G[i][j][1]
            t3=G[i][j][2]
            L.append(t1)
            L.append(t2)
            L.append(t3)
            L.append(255)
            L.sort()
            Vmax=L[len(L)-1]
            nt=Vmax/255
            nT1=t1/nt
            nT2=t2/nt
            nT3=t3/nt
            H[i][j]=(nT1,nT2,nT3)          
    return(H)

#################################
#################################
#################################

#Funcion que corta la imagen original dejandola con cantidades filas y columnas multiplos de 5.
def cortar5x5(original):
    cortada=copy.deepcopy(original)
    n_filas=len(original)
    n_columnas=len(original[0])
    filas5=(int((n_filas)/5))*5
    columnas5=(int((n_columnas)/5))*5
    cortada=cortada[:filas5]
    for i in range(filas5):
        cortada[i]=cortada[i][:columnas5]
    return cortada

#Funcion que calcula la diferencia entre 2 pixeles
def diferencia_colores(p1,p2):
    r1=p1[0]
    g1=p1[1]
    b1=p1[2]
    r2=p2[0]
    g2=p2[1]
    b2=p2[2]
    R=((r1-r2)**2)+((g1-g2)**2)+((b1-b2)**2)
    return (R)

#Calculo de la diferencia entre cada porcion con todos los mosaicos y se determina cual mosaico es el más similar.
def mosaicos(original, lista_mosaicos):
    cambiada=copy.deepcopy(original)
    n_filas=len(original)
    n_columnas=len(original[0])
    for i in range(0, n_filas, 5):
        print("Procesando mosaicos...")
        porcentaje=(int(i)/int(n_filas))*100
        print((str(porcentaje)+"000")[0:4]+"%")
        for j in range(0, n_columnas, 5):
            lista=[]
            for m in range(len(lista_mosaicos)):
                total=0
                #Donde 'total' corresponde a la diferencia de la porcion con el mosaico, es decir, la suma de las diferencia de los colores de los pixeles respectivos.
                for n in range(0,5):
                    for nn in range(0,5):
                        d=diferencia_colores(cambiada[i+n][j+nn], lista_mosaicos[m][n][nn])
                        total+=d
                lista.append((total,m))
            lista.sort()
            total_chico=lista[0][0]
            mosaico_util=lista[0][1]
            for t in range(0,5):
                for tt in range(0,5):
                    cambiada[i+t][j+tt]=lista_mosaicos[mosaico_util][t][tt]
    return(cambiada)

#################################
#################################
#################################
            
def tarea():
	# Aqui empieza tu tarea
    while True:
        click=instaintro_gui.esperar_click()
        if click=="salir":
            print("Click en salir")
            instaintro_gui.salir()
        if click=="girar":
            print("Click en girar")
            matriz_pixeles=instaintro_gui.obtener_pixeles()
            matriz_imagen_girada=girar_imagen(matriz_pixeles)
            instaintro_gui.actualizar_imagen(matriz_imagen_girada)
            print("Imagen girada")
        if click=="gris":
            print("Click en gris")
            matriz_pixeles=copy.deepcopy(instaintro_gui.obtener_pixeles())
            matriz_grises=escala_grises(matriz_pixeles)
            instaintro_gui.actualizar_imagen(matriz_grises)
            print("Imagen transformada a escala de grises")
        if click=="bordes":
            print("Click en bordes")
            matriz_pixeles=instaintro_gui.obtener_pixeles()
            matriz_bordes=bordes(matriz_pixeles)
            instaintro_gui.actualizar_imagen(matriz_bordes)
            print("Mostrando bordes de la imagen")
        if click=="mosaico":
            print("Click en mosaico")
            matriz_pixeles=instaintro_gui.obtener_pixeles()
            matriz_cortada=cortar5x5(matriz_pixeles)
            lista_mosaicos= instaintro_gui.obtener_imagenes_mosaico()
            matriz_mosaicos=mosaicos(matriz_cortada, lista_mosaicos)
            instaintro_gui.actualizar_imagen(matriz_mosaicos)
            print("Imagen en mosaicos")
       
            
            
app = instaintro_gui.Application("tarea")
app.title('InstaIntro')
app.loadProgram(tarea)
app.start()
