'''
Exemplo de código com laço while utlizando o else.
'''

print("Início do programa.")
numero = input("Digite um número: ")
divisor = 2

while divisor < numero:
    r = numero % divisor
    if r == 0:
        print("{} não é primo.".format(numero))
        break
    numero+=1
else:#bloco executado se, e somente se o while terminar sem entrar no if
    print("{}".format(numero))

print("Fim do programa.")