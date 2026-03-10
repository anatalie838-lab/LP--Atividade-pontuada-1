import os 
os.system ("cls")

renda_mensal = float(input("Digite a renda mensal do solicitante: R$ "))
valor_emprestimo = float(input("Digite o valor total do empréstimo: R$ "))
num_prestacoes = int(input("Digite o número de prestações desejadas: "))

valor_prestacao = valor_emprestimo / num_prestacoes
limite_emprestimo = renda_mensal * 10
limite_prestacao = renda_mensal * 0.30

print(f"\n--- Resumo da Análise ---")
print(f"Valor da prestação: R$ {valor_prestacao:.2f}")
print(f"Limite de prestação (30% da renda): R$ {limite_prestacao:.2f}")
print(f"Limite total do empréstimo (10x renda): R$ {limite_emprestimo:.2f}")

if valor_emprestimo <= limite_emprestimo and valor_prestacao <= limite_prestacao:
    print("\nRESULTADO: Empréstimo CONCEDIDO!")
else:
    print("\nRESULTADO: Empréstimo NEGADO.")
    