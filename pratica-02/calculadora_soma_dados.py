"""
Calculadora de Soma com Entrada do Usuário

Leia 2 valores inteiros e armazene-os nas variáveis `A` e `B`. Efetue a soma de `A` e `B`, atribuindo o seu resultado à variável `X`. **Entrada:** A entrada contém **2 valores inteiros** informados pelo usuário. **Saída:**

Imprima a mensagem `"X = "` (letra X maiúscula) seguido pelo valor da variável `X` e pelo final de linha.
"""
# Calculadora de soma com entrada do usuário

# Leitura dos valores fornecidos pelo usuário
A = int(input("Por favor insira o primeiro número: "))
B = int(input("Por favor insira o segundo número: "))

# Efutuar a soma
X = A + B

# Exibição dos valores
print(f"X = {X}")