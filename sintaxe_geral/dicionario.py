# Exemplo estrutura dicionário em python

contatosTelefone = {
    "Joao": "11-99999-9999",
    "Maria": "11-98888-8888"
}

#Exibindo chaves do dicionário
print("Keys: ",contatosTelefone.keys())

#Exibindo valores do dicioário
print("Valores: ",contatosTelefone.values())

#Exibindo chaves e valoreas através do laço for
for chave,valor in contatosTelefone.items():
    print(chave,"->",valor)
