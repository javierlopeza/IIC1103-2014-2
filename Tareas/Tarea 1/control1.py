import tableroGUI
tablero = None 
a, b, c, d = (0,)*4
puntaje = 0
def inicia_juego():
    global a,b,c,d
    a,b,c,d = tablero.inicia_juego()

def actualizar_tablero():
    global a,b,c,d
    tablero.update(a,b,c,d, puntaje)

def esperar_presionar_tecla():
    return tablero.esperarPresionarTecla()  
    
def aleatorio():
    return tablero.aleatorio()

def tarea(tablero):
    global puntaje,a,b,c,d
    
    #Aqui empieza tu tarea

    inicia_juego()
    import random
    a=7
    b=0
    c=9
    d=7
    while a!=0 and d!=0:
        tecla=esperar_presionar_tecla()
        cont=True
        while cont==True:
            aleat=random.randint(1, 3)
            if aleat==1:
                z=4
            elif aleat==2:
                z=6
            elif aleat==3:
                z=8
            if tecla=='izquierda':
                if b==0 and c==9:
                    a-=1
                    b=c
                    c=0
                    d-=1
                elif b==0 and c==0:
                    puntaje+=a
                    a=9
                    b=0
                    c=0
                    d-=1
                elif b==0 and c==0 and d==9:
                    a-=1
                    b=0
                    c=9
                    d=z
                actualizar_tablero()
                cont=False
        
            if tecla=='derecha':
                if b==0 and c==9:
                    puntaje+=d
                    a-=1
                    b=0
                    c=0
                    d=9
                elif b==9 and c==0:
                    a-=1
                    b=0
                    c=9
                    d-=1
                elif a==9 and b==0 and c==0:
                    a=z
                    b=9
                    c=0
                    d-=1
                actualizar_tablero()
                cont=False
                    

                       
    actualizar_tablero()
            

    #Aqui termina tu tarea
    
tablero = tableroGUI.Application("tarea")
tablero.title('DCC - Threes')
tablero.loadProgram(tarea)
tablero.start()
