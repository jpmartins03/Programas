f = list(input())
p = list(input())
i = j = k = 0
flag = 0
while i <= len(f)-1:
	

	if j == len(p)-1:
		flag += 1
		print(posiçao)
		j = 0
		i = posiçao + 1


	elif p[j] == f[i]:
		if j ==0:
			posiçao = i
		j += 1
		i += 1

	else:
		i += 1
		j = 0
		
if flag == 0:
	print("NOT FOUND")