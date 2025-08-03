"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes."""

Nome_Produto = "Camiseta"
Preco_Original = 50.00
Porcentagem_Desconto = 20

desconto = (Porcentagem_Desconto/100) * Preco_Original
Preco_Final = Preco_Original - desconto

print(f"Produto: {Nome_Produto}")
print(f"Preço Original: R$ {Preco_Original:.2f}")
print(f"Porcentagem de Desconto: {Porcentagem_Desconto}%")
print(f"Valor do Desconto: R$ {desconto:.2f}")
print(f"Preço Final: R$ {Preco_Final:.2f}")