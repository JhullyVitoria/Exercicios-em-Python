# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado.

qtd_km = float(input("Digite a quantidade de km percorridos pelo carro:"))
qtd_dias  = int(input("Digite a quantidade de dias que o carro foi alugado:"))

valor_pg = 60*qtd_dias + 0.15*qtd_km
print("O preço a pagar pelo aluguel do carro é: R${}".format(valor_pg))