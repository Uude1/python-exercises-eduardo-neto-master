with open('names.txt', 'r') as arquivo:
    nomes = arquivo.read().splitlines()

contagem_nomes = {}
for nome in nomes:
    if nome in contagem_nomes:
        contagem_nomes[nome] += 1
    else:
        contagem_nomes[nome] = 1

for nome, contagem in contagem_nomes.items():
    print(f'{nome}: {contagem}')