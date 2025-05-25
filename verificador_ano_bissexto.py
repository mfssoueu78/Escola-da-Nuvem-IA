# --- Verificador de Ano Bissexto ---

# Entrada: ano
ano = int(input("Digite um ano: "))

# Verificação se é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
print("-" * 30)