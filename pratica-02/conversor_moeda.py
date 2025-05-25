"""
Conversor de Moeda
Crie um programa que vonverte um valor em reais para dólares e euros. Use os seguintes dados:
- Valor em reais: R$ 100.00
- Taxa do dólar: R$ 5.70
- Taxa do euro: R$ 6.40
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas devimais.
"""

# Conversor de moeda

# Valores das moedas
valor_em_reais = 100.00
taxa_dolar = 5.70
taxa_euro = 6.40

# Conversões
valor_em_dolares = valor_em_reais / taxa_dolar
valor_em_euros = valor_em_reais / taxa_euro

# Exibição dos resultados
print(f"Valor em Reais: R$ {valor_em_reais:.2f}")
print(f"Valor em Dólares: $", round(valor_em_dolares, 2))
print(f"Valor em Euros: $", round(valor_em_euros, 2))

