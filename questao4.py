import os 

os.system("cls")

# Entrada de dados (quantidade em Kg)
kg_morango = float(input("Digite a quantidade de morangos (Kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (Kg): "))

if kg_morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

if kg_maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

valor_morango = kg_morango * preco_morango
valor_maca = kg_maca * preco_maca

total_kg = kg_morango + kg_maca
valor_bruto = valor_morango + valor_maca

# Aplicação do desconto de 10%
# Condição: Mais de 10kg de fruta OU valor total acima de R$ 15,00
if total_kg > 10 or valor_bruto > 15.00:
    valor_final = valor_bruto * 0.90  # Aplica 10% de desconto
else:
    valor_final = valor_bruto

# Exibição do resultado
print("-" * 30)
print(f"Total de frutas: {total_kg:.2f} Kg")
print(f"Valor a pagar: R$ {valor_final:.2f}")
print("-" * 30)