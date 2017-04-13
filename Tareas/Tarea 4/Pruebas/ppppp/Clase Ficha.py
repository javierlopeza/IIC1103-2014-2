def posicion_valida(filas, columnas, posicion_evaluada):
    lista_p=posicion_evaluada.split(",")
    filap=int(lista_p[0])
    colp=int(lista_p[1])
    if filap<int(filas) and colp<int(columnas):
        if filap>=0 and colp>=0:
            return True
    else:
        return False

#______________________

class Ficha():
    def __init__(self,nombre_archivo):
        self.nombre_ficha=str(nombre_archivo)
        self.posicion=None
    def posicionar_en(self, ubicacion, filasT, columnasT): #Recibe donde quiero posicionarla (un par ordenado en string) y las dimensiones del tablero en cuestion
        es_valido=posicion_valida(filasT, columnasT, ubicacion)
        if es_valido==True:
            self.posicion=ubicacion
            print("La ficha "+self.nombre_ficha+" ha sido posicionada correctamente en "+str(self.posicion))
            return True
        else:
            print("Posición inválida...")
            return False
    def lista_movimientos(self): #Me entrega una lista con los movimientos posibles.
        self.movimientos=open(str(self.nombre_ficha),"r")
        lista_movimientos=self.movimientos.readlines()
        self.movimientos.close()
        return (lista_movimientos)

cab=Ficha("caballo.txt")

    
