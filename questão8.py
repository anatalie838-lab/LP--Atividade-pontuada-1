import os 
os.system ("cls")

precos = {
    "verde": 10.00,
    "azul": 20.00,
    "amarelo": 30.00,
    "vermelho": 40.00
}

print("--- SISTEMA DE CONSULTA DE PREÇOS (CDs) ---")
print("Cores disponíveis: Verde, Azul, Amarelo, Vermelho")
cor_escolhida = input("Digite a cor do selo do CD: ").strip().lower()

if cor_escolhida in precos:
    valor = precos[cor_escolhida]
    print(f"\nO CD de cor {cor_escolhida.upper()} custa: R$ {valor:.2f}")
else:
    print("\nErro: Cor inválida! Por favor, escolha uma cor da tabela.")