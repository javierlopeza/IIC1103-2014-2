import sys

texto=str(sys.stdin.readline().strip())

contadorizq=0
contadorder=0

VF=1

for c in range(len(texto)):
    
    if texto[c]=="(":
        contadorizq+=1
    if texto[c]==")":
        contadorder+=1
    if texto[c]=="(" and texto[c+1]==")":
        print ("False")
        VF=0
    if texto[c]=="(" and texto[c+1]==" ":
        mas=1
        while texto[c+mas]==" ":
            if texto[c+mas+1]==")":
                print("False")
                VF=0
            mas+=1

if VF==1 and contadorizq==contadorder:
    print("True")

if VF==1 and contadorizq!=contadorder:
    print("False")
        

