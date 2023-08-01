#------------------------------------------------------------
#verificar se é letra --> se for letra andar 3 para frente#
def cript1():
	n = int(input())
	for i in range(1, n+1):
		a = input()
		a = list(a)
		for i in range(len(a)):
			if (ord(a[i]) >= 65 and ord(a[i]) <= 90) or (ord (a[i]) >= 97 and ord(a[i]) <= 122):
				a[i] = (chr(ord(a[i])+3))
		cript2(a)

#-------------------------------------------------------------------------------------------------
#inverter toda a lista#
def cript2(b: list):
	i = 0
	j = len(b) - 1
	while i < j:
		mem = b[i]
		b[i] = b[j]
		b[j] = mem
		j -= 1
		i += 1
	cript3(b)

#----------------------------------------------------------------------------------------------
#todo caracter da metade para frente deve andar uma para tras#
def cript3(c: list):
	for i in range(len(c)//2, len(c)):
		c[i] = chr(ord(c[i])-1)
	print("".join(c))


#------------------------------------------------------------------------------------------------
def main():
	cript1()
#-------------------------------------------------------------------------------------------------
main()
#faltou consertar a saida#