#      style  text   background
#\033[  0:     33:       44m
# 0 = none; 1 = bold; 4 = underline, 7 = negative
# text = 30 á 37 -> cores do texto / back = 40 á 47 -> cores do background

x = int(input("Digite um valor:"))
y = str(input("Digite uma palavra:"))
print("\n A palavra é: \033[1:32:47m {} e o valor é: \033[4:32:45m{}".format(y, x))