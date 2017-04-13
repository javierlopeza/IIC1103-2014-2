#______________________

class Tablero():
    fichas_en_tablero=[]
    def __init__(self,nombre_archivo):
        self.nombre_tablero=str(nombre_archivo)
        tablero_txt=open(str(nombre_archivo),"r")
        lista_tablero_txt=tablero_txt.readlines()
        tablero_txt.close()
        self.posiciones_prohibidas=lista_tablero_txt[1:]
        dimensiones=lista_tablero_txt[0].split(",")
        self.filasT=int(dimensiones[0])
        self.columnasT=int(dimensiones[1])
        for i in range(self.filasT):
            fila=[]
            for j in range(self.columnasT):
                fila.append("O")
            self.fichas_en_tablero.append(fila)
        #Hasta ahora tengo en variables a: nombre_tablero, posiciones_prohibidas, filasT, columnasT, fichas_en_tablero
    def mostrar_tablero(self):
        for i in range(len(self.fichas_en_tablero)):
            for j in range(len(self.fichas_en_tablero[i])):
                print(self.fichas_en_tablero[i][j], end=' ')
            print('')
            
    

tablero=Tablero("tablero_prueba.txt")
tablero.mostrar_tablero()
