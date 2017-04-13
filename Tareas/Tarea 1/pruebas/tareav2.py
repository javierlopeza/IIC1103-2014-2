import tableroGUI
tablero = None 
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = (0,)*16
puntaje = 0
def inicia_juego():
    global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p = tablero.inicia_juego()

def actualizar_tablero():
    global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p
    tablero.update(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p, puntaje)

def esperar_presionar_tecla():
    return tablero.esperarPresionarTecla()  
    
def aleatorio():
    return tablero.aleatorio()

def tarea(tablero):
    global puntaje,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p
    
    #Aqui empieza tu tarea

    inicia_juego()
    import random
    actualizar_tablero()
    tecla=esperar_presionar_tecla()
    tecla
    for izquierda in tecla:
        if ((a==b and a>2 and b>2) or (a==1 and b==2) or (a==2 and b==1)):
            a+=b
            b=c
            c=d
            d=0
        elif a==0:
            a=b
            b=c
            c=d
            d=0
        elif b==0:
            b=c
            c=d
            d=0
        elif c==0:
            c=d
            d=0
        d=aleatorio()
        actualizar_tablero()
        

    #Aqui termina tu tarea
    
tablero = tableroGUI.Application("tarea")
tablero.title('DCC - Threes')
tablero.loadProgram(tarea)
tablero.start()
