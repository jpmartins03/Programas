#-------------------------------------------------------
def fib(testes):
	fibonacci = [0, 1]
	for i in range(1, 60):
		fibonacci.append(fibonacci[i-1]+fibonacci[i])
	return fibonacci
#------------------------------------------------------

def main():
	testes = int(input())
	fib(60)
	fibonacci = fib(testes)
	for i in range(testes):
		num = int(input())
		print(f'Fib({num}) = {fibonacci[num]}')
main()