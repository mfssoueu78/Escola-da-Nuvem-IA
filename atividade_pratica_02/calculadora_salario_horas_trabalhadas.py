# --- Calculadora de Salário por Horas Trabalhadas ---

# Solicita ao usuário o número do funcionário (inteiro)
numero_funcionario = int(input("Digite o número do funcionário: "))

# Solicita a quantidade de horas trabalhadas (inteiro)
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))

# Solicita o valor recebido por hora (pode ter casas decimais, por isso float)
valor_por_hora = float(input("Digite o valor recebido por hora: "))

# Calcula o salário total
salario = horas_trabalhadas * valor_por_hora

# Exibe o número do funcionário e o salário formatado com duas casas decimais
# O :.2f garante 2 casas decimais, e os espaços são colocados manualmente
print(f"--- Calculadora de Salário ---")
print(f"NÚMERO = {numero_funcionario}")
print(f"SALÁRIO = R$ {salario:.2f}")
print("-" * 30)