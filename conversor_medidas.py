## Conversor de medidas
valor = float(input("Digite o valor em metros para transformá-lo em outras medidas:"))

print("{} metros é igual a {} km".format(valor, valor / 1000))
print("{} metros é igual a {} hm".format(valor, valor / 100))
print("{} metros é igual a {} dam".format(valor, valor / 10))
print("{} metros é igual a {} dm".format(valor, valor * 10))
print("{} metros é igual a {} cm".format(valor, valor * 100))
print("{} metros é igual a {} mm".format(valor, valor * 1000))