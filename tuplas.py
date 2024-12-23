lanche = ('Hamburguer', 'refrigerante', 'batata frita', 'pastel')

for i in (lanche):
    print(i)

for cont in range(0, len(lanche)):
    print(f'{lanche[cont]}, está na posicao: {cont}')

for pos, food in enumerate(lanche):
    print(f"Eu vou comer {food}, está na posição:{pos}")
    
# imprime em ordem
print(sorted(lanche))

x = (2, 4, 8, 10)
y = (1, 3, 5, 7, 9)

print(x + y)
# resultado: (2, 4, 8, 10, 1, 3, 5, 7, 9)
print(len(x+y))

z = x+y
# qts vezes o 8 aparece na soma de x e y
print(z.count(8))

# pos. do 10 na tupla z
print(z.index(10))

# pos. do 10 na tupla z a partir da pos. 1
print(z.index(10, 1))

# na tupla eu posso ter dados de vários tipos, string, numero, ..

pessoa = ('José', 29, 'M', 1.90, 'Uberlândia')
print(pessoa)
del(pessoa)