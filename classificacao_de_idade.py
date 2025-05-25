# --- Classificador de Idade ---

# Entrada: idade do usuário
idade = int(input("Digite a idade: "))

# Classificação da idade
if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")
print("-" * 30)