# --- Calculadora de Consumo de Combustível ---

# Dados da viagem
distancia_percorrida = 300  # Distância em quilômetros
combustivel_gasto = 25      # Combustível em litros

# Calcula o consumo médio (quilômetros por litro)
# Divide a distância percorrida pelo combustível gasto
consumo_medio = distancia_percorrida / combustivel_gasto

# Exibe os dados da viagem e o consumo médio
print(f"--- Calculadora de Consumo de Combustível ---")
print(f"Distância Percorrida: {distancia_percorrida} km")
print(f"Combustível Gasto: {combustivel_gasto} litros")
print(f"Consumo Médio: {consumo_medio:.2f} km/l") # Formata para duas casas decimais
print("-" * 30)