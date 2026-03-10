import os 
os.system("cls")


# Entrada de dados
a = int(input("Digite o valor de A: "))
op = input("Digite a operação (+, -, *, /): ")
b = int(input("Digite o valor de B: "))

# Processamento
if op == '+':
    resultado = a + b
elif op == '-':
    resultado = a - b
elif op == '*':
    resultado = a * b
elif op == '/':
    if b != 0:
        resultado = a / b
    else:
        resultado = "Erro (divisão por zero)"
else:
    resultado = "Operação inválida"

# Saída
print(f"Resultado: {resultado}")