import os 
os.system("cls")

# Programa para calcular média escolar e status do aluno

# Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média
media = (nota1 + nota2) / 2

# Exibição da média formatada
print(f"\nMédia final: {media:.1f}")

# Estrutura de decisão para verificar a situação
if media >= 6.0:
    print("Parabéns! Você foi aprovado!")
elif media >= 4.0:
    print("O aluno está em recuperação.")
else:
    print("O aluno foi reprovado.")