def main():
	l = int(input())
	O = str(input())
	matriz = geramatriz(l, O)

def geramatriz(l, O):
	M = [[0]*12 for i in range(12)]
	for i in range(12):
		for j in range(12):
			M[i][j] = float(input())
	soma = 0.0
	for i in range(len(M[l])):
		soma += M[l][i]
	if O == "S":
		print(soma)
	else:
		print(soma/12)
 
	#imprime_matriz(M)

def imprime_matriz(M):
	for i in range(12):
		for j in range(12):
			print(M[i][j], end = '\t')
		print("")

main()