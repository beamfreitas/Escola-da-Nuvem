"""
2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""

Peso = float(input("\nInsira seu peso em kg: "))
Altura = float(input("\nInsira sua altura em metros: "))
classificação = ""

imc = Peso/(Altura ** 2)

if imc <18.5:
    classificação = "Abaixo do peso"
elif imc <25:
    classificação = "Peso normal"
elif imc <30:
    classificação = "Sobrepeso"
else:
    classificação = "Obeso"

print("\nCalculadora de IMC\n-------------------")
print(f"Peso: {Peso:.2f} kg")
print(f"Altura: {Altura:.2f} m")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificação}")