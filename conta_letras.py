def main():
    alfabeto = [0]*26
    frase = list(input())
    contaletras(alfabeto, frase)

def contaletras(alfabeto, frase):

    for i in range(0, len(frase)):
        for j in range(0, 27):
            if frase[i] == chr(65+j) or frase[i] == chr(97+j):
                alfabeto[j]+= 1
    for i in range(0, 26):
        if alfabeto[i]!=0:
            print(f'{chr(65+i)} = {alfabeto[i]}')

main()