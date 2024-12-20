## Tabuada

print("Digite o intervalo de tabuadas que você deseja (início e fim entre 1 e 1000):")
ini = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

if 1 <= ini <= 1000 and 1 <= fim <= 1000 and ini <= fim:
    print(f"\nTabuadas de {ini} até {fim}:")
    for x in range(ini, fim + 1): 
        print(f"\nTabuada do {x}:")
        for i in range(1, 11): 
            print(f"{x} x {i} = {x * i}")
else:
    print("Intervalo inválido! Tente novamente.")