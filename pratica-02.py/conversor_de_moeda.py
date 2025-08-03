""" 1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

Valor_Real = 100.00
Taxa_Dolar = 5.20
Taxa_Euro = 6.15

Valor_Dolares = Valor_Real / Taxa_Dolar
Valor_Euro = Valor_Real / Taxa_Euro

print(f"Valor em Reais: R$ {Valor_Real:.2f}")
print(f"Valor em Dólares: $ {Valor_Dolares:.2f}")
print(f"Valor em Euros: € {Valor_Euro:.2f}")  