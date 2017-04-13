import sys
def palindromo(x):
    i=0
    while i<len(x)/2:
        if x[i]!=x[len(x)-i-1]:
            return False
        i+=1
    return True
pal=sys.stdin.readline().strip()
pal=pal.lower()
pal=pal.replace(" ","")
pal=pal.replace("?","")
pal=pal.replace("¿","")
pal=pal.replace("!","")
pal=pal.replace("¡","")
pal=pal.replace(".","")
pal=pal.replace(",","")
pal=pal.replace("´","")
pal=pal.replace("á","a")
pal=pal.replace("é","e")
pal=pal.replace("í","i")
pal=pal.replace("ó","o")
pal=pal.replace("ú","u")
pal=pal.replace(":","")
pal=pal.replace(";","")
pal=pal.replace("-","")
pal=pal.replace("_","")
pal=pal.replace("-","")
pal=pal.replace("+","")
pal=pal.replace("#","")
pal=pal.replace("$","")
pal=pal.replace("%","")
pal=pal.replace("&","")
pal=pal.replace("/","")
pal=pal.replace("*","")
pal=pal.replace("(","")
pal=pal.replace(")","")
pal=pal.replace(" ","")
print(palindromo(pal))
