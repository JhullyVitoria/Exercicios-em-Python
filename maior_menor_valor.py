# nesse caso aqui, eu tenho uma ligação enre x e y. Logo, se eu mudar
# algo em y será refletido em x
x = [1, 2, 3, 4, 5]
y = x

x[4] = 6
print(x)
print(y)

 
a = [2, 4, 6, 8]
# para solucinar o problema ant. fazemos uma cópia de a em b
b = a[:]
b[1] = 10 
print(f'\nlista a: {a}')
print(f'lista b: {b}')

# Programa q lê 5 valores num. e guarda em uma lista
lista = list()
maior = 0
menor = 0

for i in range(0, 5):
    lista.append(int(input("\nDigite um valor: ")))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
    
for x, y in enumerate(lista):
    print(f" \n O numero {y} está na pos. {x}")

print(f"\nO maior valor é: {maior}")
print(f"O menor valor é: {menor}")