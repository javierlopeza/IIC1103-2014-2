msg=str(input())
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

msg=msg.replace(usu, "")

msg=msg.strip()
    
print(msg)
print(usu)
