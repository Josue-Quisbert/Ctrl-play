# nota1 = float(input("Digite a nota: "))
# nota2 = float(input("Digite a nota: "))
# nota3 = float(input("Digite a nota: "))
# nota4 = float(input("Digite a nota: "))

# notas = [nota1,nota2,nota3,nota4]


# media = sum(notas) /len(notas)
# print(f"A media é: {media}")

nota1 = float(input("Digite a nota: "))
peso1 = float(input("Digite o peso: "))

nota2 = float(input("Digite a nota: "))
peso2 = float(input("Digite o peso: "))

notas = [nota1, nota2]
peso = [peso1, peso2]

somaPonderada = sum(notas)
somaPesos = sum(peso)

mediaPonderada = somaPonderada /somaPesos

print(f"A media ponderada das notas é: {mediaPonderada}")


