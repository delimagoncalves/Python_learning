'''
Exemplo de tratamento de execeções em pythonn, utilizando bloco try:
''' 

print("Início do programa")
a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))

try:#bloco try 
   r =  a / b
   print("Resultado de {0} / {1}: {2}".format(a,b,r))
except:
    print("Não foi possível calcular a divisão por zero.")

print("Fim do programa")