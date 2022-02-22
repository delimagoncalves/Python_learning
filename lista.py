'''
Exemplo de lista simples em python e como percorrer sobre a lista
utilizando a instrução (for in range())
'''

#Definição da lista
marcasDeCarro = ["BMW","FORD","GM","JEEP","FIAT"]

#Iterando sobre a lista
for marca in marcasDeCarro:
    print(marca)


#adicionando item a lista
marcasDeCarro.append("VOLKS")

print("")

for marca in marcasDeCarro:
    print(marca)

#removendo a primeira ocorência do item da lista
marcasDeCarro.remove("JEEP")

print("")

for marca in marcasDeCarro:
    print(marca)