frutas = [
    "maçã", "banana", "laranja", "maçã", "uva",
    "banana", "maçã", "pera", "laranja", "uva",
    "banana", "maçã", "pera", "laranja", "uva",
    "banana", "maçã", "pera", "laranja", "uva",
    "banana", "maçã", "pera", "laranja", "uva",
    "banana", "maçã", "pera", "laranja", "uva",
]

fruta_escolhida = input("Digite a fruta que você quer consultar: ").strip().lower()

quantidades = {}
for fruta in frutas:
    if fruta in quantidades:
        quantidades[fruta] += 1
    else:
        quantidades[fruta] = 1

if fruta_escolhida in quantidades:
    print(f"A fruta '{fruta_escolhida}' aparece {quantidades[fruta_escolhida]} vezes.")
else:
    print(f"A fruta '{fruta_escolhida}' não foi encontrada na lista.")

print(f"Total de frutas: {len(frutas)}")
for fruta, quantidade in quantidades.items():
    print(f"{fruta}: {quantidade}")
