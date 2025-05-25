# --- Calculadora de Comissão ---

# Entradas: nome, salário fixo e total de vendas
nome = input()
salario_fixo = float(input())
total_vendas = float(input())

# Cálculo da comissão (15%) e total a receber
comissao = total_vendas * 0.15
total_a_receber = salario_fixo + comissao

# Saída formatada
print(f"TOTAL = R$ {total_a_receber:.2f}")
print("-" * 30)