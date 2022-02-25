'''
Sequência de Fibonacci utilizando Python3
'''

n = 0

while n <2:
    try:
        #Defiindo um valor de entrada para determinar os termos da sequência
        n = int(input("Digite um numero > 1: "))
        if n < 2:
            print("Digite um número >=2: ")
    except:
        print("O dado digitado deve ser um número inteiro.")
    a = 0
    b = 1
    print("0, 1,",end="")
    i =0
    while i < n-2:
        c = a + b
        print(" {}, ".format(c),end="")
        a = b
        b = c
        i+=1

print("\n\nFim do Programa")