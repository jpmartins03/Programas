def gera_matriz(n):
	matriz = [[1]*n for i in range(n)]
	ci = 1
	cf = n-1
	li = 1
	lf = n-1
	meio = 2
	while li < lf and ci < cf:

		

		for linha in range(li, lf):
			for coluna in range(ci, cf):
				matriz[linha][coluna] = meio
		meio += 1
		li += 1
		lf -= 1
		ci += 1
		cf -= 1
		
	for linha in range(n):

		for coluna in range(n):
			if coluna == n-1:
				print(f'{matriz[linha][coluna]:>3}', end='')
			else:
				print(f'{matriz[linha][coluna]:>3}', end=' ')
		print()	
	print()


def main():

	n = int(input())
	while n != 0:

 		matriz = gera_matriz(n)

 		n = int(input())
main()