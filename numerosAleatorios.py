'''
Exemplo de utilização do módulo (random) para gerar números aleatórios
'''

#import do módulo random
import random


n = int(input("Digite a quantidade de núemros aleatórios: "))

somatorio = 0

for i in range(1,(n+1)):
    numeroAleatorio = random.randint(1,51)#Utlizamos a função randint() para determinar o intervalo dos valores
    somatorio+= numeroAleatorio
    print("Número aleatorio: ",numeroAleatorio)

print("Soma Total: ",somatorio)

