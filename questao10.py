import os 

os.system("cls")

PRECO_GASOLINA = 6.59
PRECO_ALCOOL = 3.79

litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").strip().upper()

if tipo == 'A':
    if litros <= 25:
        percentual_desconto = 0.02  # 2%
    else:
        percentual_desconto = 0.04  # 4%
    
    preco_com_desconto = PRECO_ALCOOL * (1 - percentual_desconto)
    nome_combustivel = "Álcool"

elif tipo == 'G':
    if litros <= 25:
        percentual_desconto = 0.03  # 3%
    else:
        percentual_desconto = 0.05  # 5%
    
    preco_com_desconto = PRECO_GASOLINA * (1 - percentual_desconto)
    nome_combustivel = "Gasolina"

else:
    preco_com_desconto = 0
    print("Erro: Tipo de combustível inválido!")
if preco_com_desconto > 0:
    total_a_pagar = litros * preco_com_desconto
    print(f"\n--- Resumo do Abastecimento ---")
    print(f"Combustível: {nome_combustivel}")
    print(f"Quantidade: {litros:.2f} L")
    print(f"Desconto aplicado: {percentual_desconto * 100:.0f}%")
    print(f"Total a pagar: R$ {total_a_pagar:.2f}")