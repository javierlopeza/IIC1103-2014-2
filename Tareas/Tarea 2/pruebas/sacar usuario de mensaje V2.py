msg=str(input())


contador_arrobas=0
for i in range(len(msg)-1):
    if msg[i]=="@":
        contador_arrobas+=1
count=contador_arrobas

while contador_arrobas>0:
    usu="@"
    for i in range(len(msg)-1):
        if msg[i]=="@":
            sig=1
            VV=1
            while not((i+sig)==len(msg)) and VV==1:
                if msg[i+sig]!=" ":
                    usu += msg[i+sig]
                    sig += 1
                elif msg[i+sig]==" ":
                    VV=0
                    usu += " @"
                    contador_arrobas-=1

usu=usu.split(" ")


listausu=[]
while (count-1)>=0:
    usua=usu[count-1]
    listausu.append(usu)
    msg=msg.replace(str(usua), "")
    count-=1

msg=str(msg)

msg1=msg.replace("  ", " ")
msg2=msg1.replace("   ", " ")
msg3=msg2.replace("    ", " ")
msg4=msg3.replace("     ", " ")
msg5=msg4.replace("      ", " ")
msg6=msg5.replace("       ", " ")
msg=msg6.replace("  ", " ")


print(msg)
