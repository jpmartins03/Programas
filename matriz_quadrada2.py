def gera_matriz(n):
	matriz = [[0]*n for i in range(n)]
#==================================================================
#diagonal principal#

	for linha in range(n):
		for coluna in range(n):
			if linha == coluna:
				matriz[linha][coluna]= 1

#==================================================================
#abaixo da diagonal principal#
	c = -1
	l = 0
	contador = 1
	while contador <= n:
		l = contador -1
		c = -1
		while l < n-1:
			l += 1
			c += 1
			matriz[l][c] = contador + 1
		contador += 1
#=================================================================
#acima da diagonal principal#
	l = -1
	c = 0
	contador = 1
	while contador <= n:
		c = contador -1
		l = -1
		while c < n - 1:
			l += 1
			c += 1
			matriz[l][c] = contador + 1
		contador += 1







#==================================================================
	for i in range(n):
		for j in range(n):
			if j == n-1:
				print(f'{matriz[i][j]:>3}', end='')
			else:	

				print(f'{matriz[i][j]:>3}', end=' ')
		print()
	print()
def main():
	n = int(input())

	while n != 0:
		gera_matriz(n)

		n = int(input())

main()