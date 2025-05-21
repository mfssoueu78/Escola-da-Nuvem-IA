# --- Calculadora de Soma com Entrada do Usuário ---

# Solicita ao usuário para digitar o primeiro valor inteiro
# input() lê a entrada como texto, int() converte para número inteiro
print(f"--- Calculadora de Soma ---")
A = int(input("Digite o primeiro valor inteiro (A): "))

# Solicita ao usuário para digitar o segundo valor inteiro
B = int(input("Digite o segundo valor inteiro (B): "))

# Efetua a soma de A e B
X = A + B

# Imprime o resultado formatado como "X = [valor de X]"
print(f"X = {X}")
print("-" * 30)