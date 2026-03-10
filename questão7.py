# Entrada de dados
nome_produto = input("Digite a descrição do produto: ")
quantidade = int(input(f"Digite a quantidade de {nome_produto} adquirida: "))
preco_unitario = float(input("Digite o preço unitário: R$ "))

total_bruto = quantidade * preco_unitario

if quantidade <= 5:
    percentual_desconto = 0.02  # 2%
elif quantidade <= 10:
    percentual_desconto = 0.03  # 3%
else:
    percentual_desconto = 0.05  # 5%

valor_desconto = total_bruto * percentual_desconto
total_a_pagar = total_bruto - valor_desconto

print("\n" + "="*30)
print(f"PRODUTO: {nome_produto}")
print(f"Total Bruto: R$ {total_bruto:.2f}")
print(f"Desconto ({percentual_desconto*100:.0f}%): R$ {valor_desconto:.2f}")
print(f"Total a Pagar: R$ {total_a_pagar:.2f}")
print("="*30)