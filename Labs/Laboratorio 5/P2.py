import sys

cod=str(sys.stdin.readline())

codletra=""
frase=""

for n in cod:
    codletra=codletra + n
    if len(codletra)==8:
        ASCII=int(codletra, 2)
        letra=chr(ASCII)
        frase=frase+letra
        codletra=""

frase_invertida=frase[::-1]
print(frase_invertida)
