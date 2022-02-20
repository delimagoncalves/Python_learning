'''
Exemplo de código que realiza a somatória de todos os números
digitados pelo usuário, e contabiliza a quantidade de entradas
exceto o valor zero(0) que encerra o programa.
'''

valor = int(input("Digite um número: "))
contador = 0
somatorio = 0

while valor != 0:
    somatorio += valor
    if valor != 0:
        contador +=1
    valor = int(input("Digite um número: "))


print("Soma total: %d"%somatorio)
print("Quantidade de entradas válidas: %d"%contador)