num_test = int(input())
tempo = 0

for i in range(num_test):
	PA, PB, G1, G2 = map(float, input().split())

	while PA <= PB:
		APA = int(PA * (G1/100))
		APB = int(PB * (G2/100))
		PA += APA
		PB += APB
		tempo += 1

		if tempo > 100:
			break

	if tempo > 100:
		print("Mais de 1 seculo.")
		tempo = 0	
	
	elif tempo <= 100:
		print(f'{tempo} anos.')
		tempo = 0


	