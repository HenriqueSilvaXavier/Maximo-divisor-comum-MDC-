n=input("Digite os números separados por espaço: ")
n=n.split()
for k in range(0, len(n)):
	n[k]=int(n[k])
r=n[:]
fatoração=[]
while len(n)>1:
	c=2
	p=1
	k=[n[0], n[1]]
	while n[0]!=1 or n[1]!=1:
		if min(k)<c:
			break
		elif n[0]%c==0 and n[1]%c==0:
			n[0]=n[0]/c
			n[1]=n[1]/c
			p=p*c
		else:
			c=c+1
	del n[1]
	n[0]=p
print("O MDC de {} é {}".format(r, p))