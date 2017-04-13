#MULTIPLICACION DE TUPLAS POR ESCALAR (equivalente a escalar por vector)
def mult_tupla(e,tupla):
    t1=int(tupla[0])*e
    t2=int(tupla[1])*e
    t3=int(tupla[2])*e
    r=(t1,t2,t3)
    return (r)

#SUMA DE TUPLAS
def suma_tupla(t1,t2):
    d1=int(t1[0])+int(t2[0])
    d2=int(t1[1])+int(t2[1])
    d3=int(t1[2])+int(t2[2])
    r=(d1,d2,d3)
    return (r)

#TUPLA ELEVADO A POTENCIA
def pot_tupla(e,tupla):
    t1=int(tupla[0])**e
    t2=int(tupla[1])**e
    t3=int(tupla[2])**e
    r=(t1,t2,t3)
    return (r)


