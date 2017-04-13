def verificar_par_ordenado(par_verificar):
    h=p.find("")
    if h!=-1 and h!=0 and h!=len(par_verificar)-1:
        lista=p.split(",")
    else:
        return("ERROR")
    if len(lista)==2:
        for i in range(0,2):
            ver=0
            for c in lista[i]:
                if ord(str(c))>47 and ord(str(c))<58:
                    ver+=1
            if ver!=len(lista[i]):
                return("ERROR")
    else:
        return("ERROR")
    n1=int(lista[0])
    n2=int(lista[1])
    return(n1,n2)
    
p="111"
print(verificar_par_ordenado(p)[0])
print(verificar_par_ordenado(p)[1])
print(str(verificar_par_ordenado(p)[0])+","+str(verificar_par_ordenado(p)[1]))
