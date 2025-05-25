# --- Conversor de Moeda ---

# Dados fornecidos para a conversão
valor_reais = 100.00  # Valor inicial em Reais
taxa_dolar = 5.20    # Quantos Reais valem 1 Dólar
taxa_euro = 6.15     # Quantos Reais valem 1 Euro

# Calcula o valor em Dólares
valor_em_dolar = valor_reais / taxa_dolar # Divide o valor em Reais pela taxa do Dólar

# Calcula o valor em Euros
valor_em_euro = valor_reais / taxa_euro # Divide o valor em Reais pela taxa do Euro

# Exibe os resultados formatados com duas casas decimais
# f-string é usada para formatar a saída de forma legível
print(f"--- Conversor de Moeda ---")
print(f"Valor em Reais: R$ {valor_reais:.2f}") # O ":.2f" formata para 2 casas decimais
print(f"Convertido para Dólar: US$ {valor_em_dolar:.2f}")
print(f"Convertido para Euro: € {valor_em_euro:.2f}")
print("-" * 30) # Linha divisória para melhor visualização