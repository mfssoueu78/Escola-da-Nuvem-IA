# --- Calculadora de IMC ---

# Entradas: peso (kg) e altura (metros)
peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Classificação do IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

# Saída
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
print("-" * 30)