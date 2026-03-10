import os 
os.system("cls")

nome= input("Digite seu nome: ")
sexo= input("Digite seu sexo (F ou M): ")
estado_civil=input ("Digite seu estado civil: ")
tempo_de_casada= "Não se aplica"

if sexo == "F" and estado_civil == "casada":
    tempo_de_casada = float(input("digite o tempo de casamento em anos: "))
print("¨¨¨¨¨¨¨¨¨¨¨¨exposição dos dados¨¨¨¨¨¨¨¨¨¨¨¨¨¨")   
print(f"Digite seu nome: {nome}")
print(f"Digite seu sexo: {sexo}")
print(f"Digite seu estado civil: {estado_civil}")