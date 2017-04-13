import sys
a=str(sys.stdin.readline().strip())
while a!="salir":
	if a=="es_perfecto":
		n=int(sys.stdin.readline().strip())
		p=0
		k=0
		while k<n:
			k=k+1
			if n%k==0 and k<n:
				p=p+k
		if p==n:
			print("True")
		else:
			print("False")
	if a=="es_par":
		n=int(sys.stdin.readline().strip())
		if n%2==0:
			print("True")
		else:
			print("False")
	if a=="mcd":
		n1=int(sys.stdin.readline().strip())
		n2=int(sys.stdin.readline().strip())
		k=0
		p=0
		while k<n1 and k<n2:
			k=k+1
			if n1%k==0 and n2%k==0:
				p=k
		print(p)
	if a=="es_cuadrado_perfecto":
		n=int(sys.stdin.readline().strip())
		p=False
		k=0
		while k<n:
			k=k+1
			if k**2==n:
				p=True
		print(p)
	a=str(sys.stdin.readline().strip())
print("bye!")



	
