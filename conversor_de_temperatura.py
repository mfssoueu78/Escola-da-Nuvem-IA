# --- Conversor de Temperatura ---

# Entradas: temperatura, unidade de origem e unidade de destino
temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C/F/K): ").upper()
destino = input("Unidade para converter (C/F/K): ").upper()

# Lógica de conversão
if origem == 'C':
    if destino == 'F':
        convertida = (temp * 9/5) + 32
        print(f"{temp}°C é {convertida:.2f}°F")
    elif destino == 'K':
        convertida = temp + 273.15
        print(f"{temp}°C é {convertida:.2f}K")
elif origem == 'F':
    if destino == 'C':
        convertida = (temp - 32) * 5/9
        print(f"{temp}°F é {convertida:.2f}°C")
    elif destino == 'K':
        convertida = (temp - 32) * 5/9 + 273.15
        print(f"{temp}°F é {convertida:.2f}K")
elif origem == 'K':
    if destino == 'C':
        convertida = temp - 273.15
        print(f"{temp}K é {convertida:.2f}°C")
    elif destino == 'F':
        convertida = (temp - 273.15) * 9/5 + 32
        print(f"{temp}K é {convertida:.2f}°F")
else:
    print("Unidades inválidas.")
print("-" * 30)