texto = input("Digite uma palavra da sua escolha: ")

texto_invertido = texto[::-1]

if texto == texto_invertido:
    print("A palavra escolhida é um palíndromo!")
else:
    print("A palavra escolhida não é um palíndromo.")