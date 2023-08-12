def geramatriz(n):
	m = [[0]*n for i in range(n)]
	num = 1
	#primeira linha#
	for coluna in range(n):
		m[0][coluna] = 2 ** coluna
	#==================================
	#restante das colunas#
	for coluna in range(n):
		for linha in range(1, n):
			m[linha][coluna] = (m[linha-1][coluna])*2
	
	print(m[n-1][n-1])




	t = len(list(str(m[n-1][n-1])))
	print(t)
	for linha in range(n):
		for coluna in range(n):
			print(f'{m[linha][coluna]:>{t+1}}', end="")
		print()

def main():
	n = int(input())
	while n != 0:
		m = geramatriz(n)
		n = int(input())
main()
#falta arrumar saida#