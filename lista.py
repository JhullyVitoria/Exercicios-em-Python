n = [1, 3, 5, 7, 9]
print(n)
# muda valor da pos. 2 da lista *OBS: tupla () é imutável
n[2] = 11
print(n)
#add um valor a lista
n.append(13)
n.sort(reverse=True)
# inseri na pos. 0 o valor 17
n.insert(0, 17)
#remove um elemento da lista na pos. 6
n.pop(6)
#remove um elemento da lista que é igual a 3
n.remove(3)
print(n)

print(f"A lista possui {len(n)} elementos")

i = int(input("Digite um valor que está em n para ser removido:"))

if i in n:
    n.remove(i)
    print(f"O valor {i} foi removido com sucesso!")
    print("Nova lista:", n)
else:
    print(f"Desculpe, mas este elemento {i} não foi encontrado na lista. Tente outro valor!")

print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

letras = list()    
for l in range (0, 5):
    letras.append(str(input('Digite uma letra qualquer:')))

for i, j in enumerate(letras):
    print(f"Na pos. {i} está a letra {j}")
    