'''
Este primiro códgo de exemplo verifica se o número digitado é primo,
'''

print("Início do programa: ")
n = int(input("Digite um número: "))
contador = 0
i = 2

while i < n:
    r = n % i
    if r == 0:
        contador +=1
    i+=1
if contador == 0:
    print("{} é primo.".format(n))
else:
    print("{} não é primo.".format(n))

print("Fim do programa.")