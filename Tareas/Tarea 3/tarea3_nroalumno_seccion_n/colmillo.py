import instaintro_gui

def tarea():
        while True:
                cmd = instaintro_gui.esperar_click()

                if cmd == "salir":
                        instaintro_gui.salir()

                elif cmd == "gris":
                        imagen = instaintro_gui.obtener_pixeles()

                        #print(len(imagen),",",len(imagen[0]))
                        #print(imagen[20][20])

                        for i in range(len(imagen)):
                                for j in range(len(imagen[0])):
                                        media=(imagen[i][j][0]+imagen[i][j][1]+imagen[i][j][2])//3
                                        imagen[i][j]=(media,media,media)

                        instaintro_gui.actualizar_imagen(imagen)

                elif cmd == "girar":
                        imagen = instaintro_gui.obtener_pixeles()

                        imagen_creada = []

                        for i in range(len(imagen[0])):
                                imagen_creada.append([])
                                for j in range(len(imagen)):
                                        imagen_creada[i].append([])
                                        imagen_creada[i][j] = imagen[len(imagen) -1 -j][i]

                        instaintro_gui.actualizar_imagen(imagen_creada)

                

                        
                elif cmd == "bordes":
                        imagen = instaintro_gui.obtener_pixeles()

                        B=[[-1,0,1],[-2,0,2],[-1,0,1]]
                        B2=[[1,2,1],[0,0,0],[-1,-2,-1]]
                        G=[]
                        G2=[]
                        
                        for i in range(len(imagen)):
                                for j in range(len(imagen[0])):
                                        media=(imagen[i][j][0]+imagen[i][j][1]+imagen[i][j][2])//3
                                        imagen[i][j]=(media,media,media)

                        instaintro_gui.actualizar_imagen(imagen)
                        
                        for i in range(len(imagen)):
                                F=[]
                                for j in range(len(imagen[0])):
                                        suma=0
                                        for k in range(3):
                                                for l in range(3):
                                                        if (i+k-l)<len(imagen)and(j+l-1)<len(imagen):
                                                                a=(B[k][l])*(imagen[i+k-l][j+l-1][0])
                                                                suma=suma+(3*a)
                                                                if i==0 and j==0:
                                                                        print(suma)
                                        
                                        F.append(suma)
                                G.append(F)
                            
                        print(G[0][0])
                        print(B)

                        for i in range(len(G)):
                                for j in range(len(G[0])):
                                        a=(G[i][j][0])**2
                                        b=(G[i][j][1])**2
                                        c=(G[i][j][2])**2
                                        G[i][j]=(a,b,c)

                        for i in range(len(imagen)):
                                F=[]
                                for j in range(len(imagen[0])):
                                        suma=(0,0,0)
                                        for k in range(3):
                                                for l in range(3):
                                                        if (i+k-l)<len(imagen)and(j+l-1)<len(imagen):
                                                                a=(B2[k][l])*(imagen[i+k-l][j+l-1][0])
                                                                b=(B2[k][l])*(imagen[i+k-l][j+l-1][1])
                                                                c=(B2[k][l])*(imagen[i+k-l][j+l-1][2])
                                                                t=(a,b,c)
                                                                aa=suma[0]+t[0]
                                                                bb=suma[1]+t[1]
                                                                cc=suma[2]+t[2]
                                                                suma=(aa,bb,cc)
                                                        F.append(suma)
                                G2.append(F)

                        for i in range(len(G2)):
                                for j in range(len(G2[0])):
                                        a=(G2[i][j][0])**2
                                        b=(G2[i][j][1])**2
                                        c=(G2[i][j][2])**2
                                        G2[i][j]=(a,b,c)
                                        
                        for i in range(len(G2)):
                                for j in range(len(G2[0])):
                                        a=G2[i][j][0]+G2[i][j][0]
                                        b=G2[i][j][1]+G2[i][j][1]
                                        c=G2[i][j][2]+G2[i][j][2]
                                        G[i][j]=(a,b,c)

                        for i in range(len(G)):
                                for j in range(len(G[0])):
                                        a=(G[i][j][0])**1/2
                                        b=(G[i][j][1])**1/2
                                        c=(G[i][j][2])**1/2
                                        G[i][j]=(a,b,c)
                                        if i==0 and j==0:
                                                print(a,b,c)

                        for i in range(len(G)):
                            for j in range(len(G[0])):
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
                                G[i][j]=(nT1,nT2,nT3)          
                            

                        
                        instaintro_gui.actualizar_imagen(G)


                #elif cmd == "mosaico"       
                        
                #        pass
                

app = instaintro_gui.Application("tarea")
app.title('InstaIntro')
app.loadProgram(tarea)
app.start()
