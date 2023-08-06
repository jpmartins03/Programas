def gera_matriz(linhas, colunas):
	matriz = [[0]*colunas for linhas in range(linhas)]
	#===================================================
	for linha in range(linhas):
		matriz[linha] = list(map(int, input().split()))

	#===================================================
	for linha in range(linhas):
		for coluna in range(colunas):
			if linha == 0 and coluna == 0:
				maior = matriz[linha][coluna]
			if matriz[linha][coluna] > maior:
				maior = matriz[linha][coluna]
	#print(matriz)
	print(maior)

def main():
	linhas, colunas = map(int, input().split())
	gera_matriz(linhas, colunas)
main()