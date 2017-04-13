
msje=str(input())

cocatenado_de_binarios=""
cdb=cocatenado_de_binarios

for l in range(len(msje)):
    #Codificacion ASCII:
    ASCII=ord(msje[l])
    #Codificacion Binaria:
    BIN=str(bin(ASCII))
    #Eliminacion letra "b":
    BIN=BIN.split("b")
    #Uso unicamente de la parte larga del numero binario:
    BIN=BIN[1]
    #Agregar ceros a la izquierda hasta que tenga 8 digitos:
    while len(BIN)<8:
        BIN=("0"+BIN)
    #Cocatenado de numeros binarios correspondientes a cada palabra:
    cdb=cdb+BIN

mbin=cdb

print(mbin)
    
    
    
