x = float(input())
n = int(input())


e = 1
aux = 1 
fat = 1

while aux <= n:
	e += (x ** aux)/(aux*fat)
	fat = (aux * fat) #fatorial do numero anterior#
	aux += 1
print(f'{e:.4f}')