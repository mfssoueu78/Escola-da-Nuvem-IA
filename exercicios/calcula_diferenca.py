# Esse código tem como objetivo ler valores inteiros inputados pelo usuário e calcular a diferença

# Ler os valores inteiros fornecidos pelo usuário
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

# Calculo da diferença
diferenca = (A * B) - ( C * D)

# Exibir resultado
print("A fórmula para a diferença é: DIFERENÇA = (A * B) - ( C * D)")
print(f"Substituindo os valores fornecidos: DIFERENÇA = ({A} * {B}) - ( {C} * {D})")
print(f"O resultado da diferença é: DIFERENÇA = {diferenca}")