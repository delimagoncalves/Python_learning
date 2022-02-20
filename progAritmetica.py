'''
Exemplo de código que exibe os 10 primeiros
termos de uma progressão aritmética.
'''

from traceback import print_tb


print("Início do Programa")
p = int(input("Digite o primeiro termo: "))
r = int(input("Digite o segundo termo: "))
contador = 1

while contador <= 10:
    print(p)
    p = p + r
    contador+=1

print("Fim do Programa")