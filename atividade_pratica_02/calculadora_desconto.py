# --- Calculadora de Desconto ---

# Informações do produto
nome_produto = "Camiseta"       # Nome do item
preco_original = 50.00          # Preço sem desconto
porcentagem_desconto = 20       # Porcentagem de desconto (20%)

# Calcula o valor do desconto
valor_do_desconto = (preco_original * porcentagem_desconto) / 100 # Multiplica o preço original pela porcentagem de desconto e divide por 100

# Calcula o preço final após o desconto
preco_final = preco_original - valor_do_desconto # Subtrai o valor do desconto do preço original

# Exibe os detalhes do produto e o resultado do cálculo
print(f"--- Calculadora de Desconto ---")
print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print(f"Valor do Desconto: R$ {valor_do_desconto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")
print("-" * 30)