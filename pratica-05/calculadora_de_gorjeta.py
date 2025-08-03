"""
1- Calculadora de Gorjeta
Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

* Defina o valor da conta (ex: R$ 100,00).  
* Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
* O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais.
"""

def calcular_gorjeta(valor_conta, porcentagem):
    return valor_conta * (porcentagem / 100)

valor_conta = float(input("\nDigite o valor da conta: "))
porcentagem = int(input("\nDigite a porcentagem da gorjeta: "))

gorjeta = calcular_gorjeta(valor_conta, porcentagem)

print(f"\nValor da conta: R$ {valor_conta:.2f}")
print(f"\nPorcentagem da gorjeta: {porcentagem}%")
print(f"\nValor da gorjeta: R$ {gorjeta:.2f}")