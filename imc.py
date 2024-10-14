nome    = input("Digite seu nome: ")
altura  = input("Altura: ")
peso    = input("Peso: ")

imc = int(peso) / (float(altura) * float(altura))
print(f'{imc:,.2f}')

if imc <= 18.5:
    print("Magreza")
    if imc > 18.5 or imc < 24.9:
        print("Normal")
elif imc >= 25 or imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")