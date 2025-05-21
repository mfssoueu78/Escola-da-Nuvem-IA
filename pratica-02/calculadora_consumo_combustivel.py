"""
Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

- Distância percorrida: 300 km
- Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""

# Calculadora de Consumo de Combustível

# Dados da viagem
distancia_percorrida = 300 # em quilômetros (km)
combusivel_gastos = 25 # em litros (l)

# Calculo do consumo médio
consumo_medio = distancia_percorrida / combusivel_gastos

# Exibição
print(f"Dados da viagem:")
print(f"Distância percorrida: {distancia_percorrida} quilômetros (km)")
print(f"Combustível gasto: {combusivel_gastos} litros (l)")
print("Concumo médio:", round(consumo_medio, 2), "km/l")
