
binario = int(input())
decimal = 0
exp = 0 
while binario != 0:                                                   #tira o ultimo bit# 
	resto = binario % 10                                              #da o valor do resto da divisao do binario por 10#
	binario //= 10                                                    #binario recebe seu novo valor sem ultimo bit#
	decimal = decimal + resto * 2 ** exp                              #conversao do bin/deci#
	exp += 1                             #expoente aumenta um para cada bit#
print(decimal)	