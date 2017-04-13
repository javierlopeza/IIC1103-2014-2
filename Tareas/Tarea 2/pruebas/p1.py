ldn=[0, 1, 2]

for i in range(0,3):
    ldn[i]=bin(ldn[i])
    ldn[i]=ldn[i].split("b")
    ldn[i]=ldn[i][1]
    while len(ldn[i])<8:
        ldn[i]=("0"+ldn[i])
print("Lista", ldn)

cocatenado_ndesordenados_binarios=""
ccnb=cocatenado_ndesordenados_binarios
for nb in range(0, 3):
    ccnb=ccnb+ldn[nb]

print("Cocatenado", ccnb)
    
