def main():
	c = int(input())
	o = str(input())
	M = gera_matriz()
	soma = 0.0
	for i in range(12):
		soma += M[i][c]
	if o == "S":
		print(f'{soma:.1f}')
	else:
		print(f'{(soma/12):.1f}')



def gera_matriz():
	M = [[0]*12 for i in range(12)]
	for i in range(12):
		for j in range(12):
			M[i][j] = float(input())

	return M
main()