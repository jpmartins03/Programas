hi, hf = map(int, input().split())

inicio = hi 
fim = hf 

if inicio < fim:
	duração = fim - inicio
else:
	duração = 24 - inicio + fim

print(f'O JOGO DUROU {duração} HORAS')