import sys
vf=True
u=0
while vf==True:
	a=(sys.stdin.readline().strip())
	if a=="donar"or a=="reportar":
		if a=="donar":
			k=int(sys.stdin.readline().strip())
			u=u+k
		if a=="reportar":
			print(u)
	if a=="0":
		vf=False


