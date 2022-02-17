'''Exemplo de cógio que imprime no console
 se o número digiado pelo usuário é Par ou ìmpar.
'''

x = 1

while x != 0:#Enquanto o usuário não digitar 0, o programa segue pedindo outra entrada.
    x = int(input("Digite um número: "))
    if x % 2 == 0:
        print("%d é par."%x)
    else:
        print("%d é ímpar."%x)