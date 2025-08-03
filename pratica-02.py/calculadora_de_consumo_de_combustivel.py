"""4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais."""

Distancia_Percorrida = 300  
Combustivel_Gasto = 25  
Consumo_Medio = Distancia_Percorrida / Combustivel_Gasto

print(f"Distância Percorrida: {Distancia_Percorrida}")
print(f"Combustível Gasto:{Combustivel_Gasto}")
print(f"Consumo Médio: {Consumo_Medio:.2f} km/l")