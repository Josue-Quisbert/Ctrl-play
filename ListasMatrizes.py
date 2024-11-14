#Listas sao multiplos objetos dentro de apenas um local

convidados = ["raphael", "cleiton", "jorge", "joao"]

print(convidados[0])

#Alteracao de objeto pelo indice

convidados[0] ="betariz"

print(convidados[0])

#Adicionando itens numa lista 

convidados.append("Joca")

print(convidados)

#Inserindo em uma posicao especifica

convidados.insert(0, "Savio")
print(convidados)

#Removendo convidados

convidados.pop()

print(convidados)

#Removendo convidados de posicao especifica

del convidados[0]

print (convidados)

##organizando lista

convidados.sort()

print(convidados)

##organizando lista em ordem inversa


convidados.sort(reverse= True)

print(convidados)

##funcao lenght

print(len(convidados))

#Funcao sum     
Lista = [1,2,3,4,5,6,7,8,9,10]

soma = sum(Lista)

print(soma)

#matrizes

timexPessoas = [["palmeiras", "internacional", "corinthians"],["jose", "maria", "paulo"]]

print(timexPessoas[1][2])

