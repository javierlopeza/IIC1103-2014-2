
msje=str(input())

cocatenado_de_binarios=""
cdb=cocatenado_de_binarios

for l in range(len(msje)):
    print(msje[l])
    #Codificacion ASCII:
    ASCII=ord(msje[l])
    print(ASCII)
    #Codificacion Binaria:
    BIN=str(bin(ASCII))
    #Eliminacion letra "b":
    BIN=BIN.split("b")
    #Uso unicamente de la parte larga del numero binario:
    BIN=BIN[1]
    #Agregar ceros a la izquierda hasta que tenga 8 digitos:
    while len(BIN)<8:
        BIN=("0"+BIN)
    print(BIN)
    #Cocatenado de numeros binarios correspondientes a cada palabra:
    cdb=cdb+BIN

print(cdb)
    
    
    
