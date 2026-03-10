import os
os.system("cls")

# Leitura dos valores (convertendo para inteiro)
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

if a == b:
    c = a + b
else:
    c = a * b
print(f"O conteúdo da variável C é: {c}")