'''
Este programa exibe os três números digitados pelo usuário em ordem crescente
e apresenta o maior número.
'''

print("")
print("Programa que exibe o menor de 3 números inteiros")
print("")
numberOne = int(input("Digite o primeiro número: "))
numberTwo = int(input("Digite o primeiro número: "))
numberThree = int(input("Digite o primeiro número: "))
print("Você digitou os números: {0} {1} {2}".format(numberOne,numberTwo,numberThree))
print("")

#Lógica de análise do maior número
if numberOne > numberTwo and numberOne > numberThree:
    highNumber = numberOne
    #Lógica para imprimir os números em ordem crescente
    if numberTwo > numberThree:
        pos1,pos2,pos3 = numberThree, numberTwo,numberOne
elif numberTwo > numberOne and numberTwo > numberThree:
    highNumber = numberTwo
    if numberOne > numberThree:
        pos1,pos2,pos3 = numberThree,numberOne,numberTwo
else:
    highNumber = numberThree
    if numberOne > numberTwo:
        pos1,pos2,pos3 = numberTwo, numberOne, numberThree
    else:
        pos1,pos2,pos3 = numberOne, numberTwo, numberThree

print("O maior número é: {0}".format(highNumber))
print("Números em ordem crescente: {0}, {1}, {2}".format(pos1,pos2,pos3))