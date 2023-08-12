def geramatriz(l, c):
	M = [[]for i in range(l)]
	for linha in range(l):
		M[linha] = list(map(int, input().split()))
	#print(M)
	#print(M[1])
	transpositor(M, l, c)
	
def transpositor(M, l, c):
	new_M = [[]for i in range(len(M[0]))]
	#print(new_M)

	for coluna in range(len(M[0])):
		for linha in range(len(M)):
			new_M[coluna].append(M[linha][coluna])
			#print(new_M)
 
	
	for linha in range(len(new_M)):
		for coluna in range(len(new_M[0])):
			if coluna == len(new_M[0])-1:
				print(f'{new_M[linha][coluna]}', end='')
			else:
				print(f'{new_M[linha][coluna]}', end=' ')
		print()

def main():
	l, c = map(int, input().split())
	if l == 0 or c == 0:
		print()
	else:
		geramatriz(l, c)
main()