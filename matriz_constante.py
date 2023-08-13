def constant_tester(m, n):
	constante = True
	#determinar qual numero servirá de teste#
	num = 0
	for i in range(n):
		num += m[0][i]
	#testar se toda linha tem soma igual a num#
	for linha in range(n):
		soma_linha = 0
		for coluna in range(n):
			soma_linha += m[linha][coluna]
		if soma_linha != num:
			constante = False
	#testar cada coluna#
	for coluna in range(n):
		soma_coluna = 0
		for linha in range(n):
			soma_coluna += m[linha][coluna]
		if soma_coluna != num:
			constante = False
	#testar diagonal principal#
	soma_diagonal1 = 0
	for linha in range(n):
		for coluna in range(n):
			if linha == coluna:
				soma_diagonal1 += m[linha][coluna]
	if soma_diagonal1 != num:
		constante = False
	#testar diagonal secundaria#
	soma_diagonal2 = 0
	linha = 0
	coluna = n-1
	c = n-1


	while linha < n:
		while coluna == c:
			soma_diagonal2 += m[linha][coluna]
			
			coluna -= 1
		c -= 1
		linha += 1

	
	if soma_diagonal2 != num:
		constante = False
	return constante



def main():
	n = int(input())
	m = [[] for i in range(n)]
	for i in range(n):
		m[i] = list(map(int, input().split()))

	constante = constant_tester(m,n)
	if constante == True:
		print("SIM")
	else:
		print("NAO")
main()