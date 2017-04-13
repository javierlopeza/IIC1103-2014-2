import instaintro_gui


def tarea():
	def sum(tup1,tup2):
		a=tup1[0]+tup2[0]
		b=tup1[1]+tup2[1]
		c=tup1[2]+tup2[2]
		return(a,b,c)
	def mult_escalar(escalar,tupla):
		tupla2=[]
		for i in range(3):
			tupla2.append(escalar*tupla[i])
		return(tupla2)
	def normalizar(aux):
		x,y,z=aux
		aux1=[x,y,z]
		aux1.append(255)
		ordenada=aux1.sort()
		n=(aux1[3])/255
		return((aux[0])/n,(aux[1])/n,(aux[2])/n)
	def raiz_cuadrad(ax,ay):
		suma_cuadrad0=(((ax[0])**2 + (ay[0])**2)**0.5)//1
		suma_cuadrad1=(((ax[1])**2 + (ay[1])**2)**0.5)//1
		suma_cuadrad2=(((ax[2])**2 + (ay[2])**2)**0.5)//1
		return(suma_cuadrad0,suma_cuadrad1,suma_cuadrad2)
	def girar_imagen(imagen):
		img_rotada=[]
		aux=[]
		n_columnas=len(imagen[0])-1
		n_filas=len(imagen)-1
		i=0
		p=0
		while i<=n_columnas:
			p=0
			while p<=n_filas:
				aux.append(imagen[n_filas-p][i])
				p+=1
			img_rotada.append(aux)
			aux=[]
			i+=1
		return(img_rotada)
	def bw_imagen(imagen):
		img_bw=[]
		aux=aux2=aux3=[]
		n_columnas=len(imagen[0])-1
		n_filas=len(imagen)-1
		i=0
		p=0
		while i<=n_filas:
			p=0
			while p<=n_columnas:
				aux=imagen[i]
				promedio=(aux[p][0]+aux[p][1]+aux[p][2])/3
				aux2=(promedio,promedio,promedio)
				aux3.append(aux2)
				p+=1
			img_bw.append(aux3)
			aux=aux1=aux2=aux3=[]
			i+=1
		return(img_bw)
	def convolusion(matriz,matriz_pixel):
		aux=[]
		pixel_final=[]
		for k in range(3):
			for i in range(3):
				aux.append(mult_escalar(matriz[k][i],matriz_pixel[k][i]))
			pixel_final.append(aux)
			aux=[]
			suma_parcial=(0,0,0)
		for k in range(len(pixel_final)):
			for i in range(3):
				suma_parcial=(sum(suma_parcial,pixel_final[k][i]))	
		return(suma_parcial)
	def matriz_expand(imagen):
		col=len((imagen)[0])
		fil=len(imagen)
		matriz_auxi=[(0,0,0)]
		matriz_expandida=[]
		fila_ceros=[]
		for i in range(col+2):
			fila_ceros.append((0,0,0))
		#Ahora agregar ceros a la izquierda y derecha de cada fila
		matriz_expandida.append((fila_ceros))
		for k in range(fil):
			matriz_auxi=[(0,0,0)]
			for i in range(col):
				matriz_auxi.append(imagen[k][i])
			matriz_auxi.append((0,0,0))
			matriz_expandida.append(matriz_auxi)
		matriz_expandida.append(fila_ceros)
		return(matriz_expandida)
	def matriz_expand_mosaico(imagen):
		col=len((imagen)[0])
		fil=len(imagen)
		matriz_auxi=[(0,0,0)]
		matriz_expandida=[]
		fila_ceros=[]
		for i in range(col+2):
			fila_ceros.append((0,0,0))
		#Ahora agregar ceros a la izquierda y derecha de cada fila
		matriz_expandida.append((fila_ceros))
		for k in range(fil):
			matriz_auxi=[(0,0,0)]
			for i in range(col):
				matriz_auxi.append(imagen[k][i])
			matriz_auxi.append((0,0,0))
			matriz_expandida.append(matriz_auxi)
		matriz_expandida.append(fila_ceros)
		return(matriz_expandida)
	def detectar_bordes(foto):
		imagen=matriz_expand(foto)
		bx=[(-1,0,1),(-2,0,2),(-1,0,1)]
		by=[(1,2,1),(0,0,0),(-1,-2,-1)]
		gx=gy=gx_sinbordes=gy_sinbordes=matriz_aux=matriz_gx_aux=matriz_gy_aux=[]
		matriz_aux=matriz_gx_aux=matriz_gy_aux=[]
		#Matriz gx:
		for k in range(1,(len(imagen)-1)):
			for i in range(1,(len(imagen[0])-1)):
				matriz_aux=(imagen[k-1][i-1:i+2],imagen[k][i-1:i+2],imagen[k+1][i-1:i+2])
				matriz_gx_aux.append(convolusion(bx,matriz_aux))
			gx.append(matriz_gx_aux)
			matriz_gx_aux=[]
		print("gx done")
		#Matriz gy:
		for k in range(1,(len(imagen)-1)):
			for i in range(1,(len(imagen[0])-1)):
				matriz_aux=(imagen[k-1][i-1:i+2],imagen[k][i-1:i+2],imagen[k+1][i-1:i+2])
				matriz_gy_aux.append(convolusion(by,matriz_aux))
			gy.append(matriz_gx_aux)
			matriz_gy_aux=[]
		print("gy done")
		g=[]
		aux=[]
		for i in range(len(foto)):
			for j in range(len(foto[0])):
				aux.append(normalizar(raiz_cuadrad(gx[i][j],gy[i][j])))
			g.append(aux)
			aux=[]
		return(g)
	def diferencia_cuadrado(base_mosaico,pixel5x5):
		u=x=0
		for k in range(5):
			for i in range(5):
				for b in range(3):
					u+=(base_mosaico[k][i][b]-pixel5x5[k][i][b])**2
		return(u)
	def comparar_mosaico(matriz5x5):
		lista_mosaicos=instaintro_gui.obtener_imagenes_mosaico()
		a=len(lista_mosaicos)
		lista_diferencias=matriz_aux=[]
		for x in range(a):
			matriz_aux=lista_mosaicos[x]
			lista_diferencias.append((diferencia_cuadrado(matriz_aux,matriz5x5),x))
		lista_diferencias.sort()
		return(lista_mosaicos[lista_diferencias[0][1]])
	def mosaico(imagen):
		print("Procesamiento de mosaico iniciado")
		col=len(imagen[0])
		filas=len(imagen)
		a=col%5
		b=filas%5
		porcentaje=0
		for k in range(2,(filas-b),5):
			for i in range(2,(col-a),5):
				matriz_aux=(imagen[k-2][i-2:i+3],imagen[k-1][i-2:i+3],imagen[k][i-2:i+3],imagen[k+1][i-2:i+3],imagen[k+2][i-2:i+3])
				(imagen[k-2][i-2:i+3],imagen[k-1][i-2:i+3],imagen[k][i-2:i+3],imagen[k+1][i-2:i+3],imagen[k+2][i-2:i+3])=comparar_mosaico(matriz_aux)
			porcentaje=((k*100)//filas)
			print(str(porcentaje)+"%")
		return(imagen)
	tecla=instaintro_gui.esperar_click()
	while tecla!="salir":
		if tecla=="gris":
			instaintro_gui.actualizar_imagen(bw_imagen(instaintro_gui.obtener_pixeles()))
		if tecla=="girar":
			instaintro_gui.actualizar_imagen(girar_imagen(instaintro_gui.obtener_pixeles()))
		if tecla=="bordes":
			b=instaintro_gui.obtener_pixeles()
			a=bw_imagen(b)
			instaintro_gui.actualizar_imagen(detectar_bordes(a))
		if tecla=="mosaico":
			instaintro_gui.actualizar_imagen(mosaico(instaintro_gui.obtener_pixeles()))


		tecla=instaintro_gui.esperar_click()
	instaintro_gui.salir()




	pass


app = instaintro_gui.Application("tarea")
app.title('InstaIntro')
app.loadProgram(tarea)
app.start()
 
