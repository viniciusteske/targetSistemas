# Questão 1
indice = 13
soma = 0
k = 0
while(k < indice):
    k += 1
    soma += k
    
print(soma)

# Questão 2
def fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def pertence(m):
    if(m < 0): return 'não pertence'

    i = 0
    while(1):
        aux = fibonacci(i)
        if aux == m:
            return 'pertence'
        elif aux > m:
            return 'não pertence'
        i += 1

m = int(input("Informe o número: "))
print(pertence(m))

# Questão 3
# Json ou XML não disponível.

# import json

# with open('data.json', 'r') as file:
#     dados = json.load(file)

# Supondo os dados em um vetor chamado dados e que os
# dias sem faturamento tenham valor 0
def menor(dados):
    menor = dados[0]
    for i in range(len(dados)):
        if dados[i] < menor:
            menor = dados[i]
    return menor

def maior(dados):
    maior = dados[0]
    for i in range(len(dados)):
        if dados[i] > maior:
            maior = dados[i]
    return maior

def superior(dados):
    pass
    media = [d for d in dados if d != 0]
    media = sum(media)/len(media)
    dias = 0
    for d in dados:
        if d > media:
            dias += 1
    return dias

# Toy example
dados = [21, 15, 1, 3, 11, 12, 13, 14, 15, 0, 0, 17, 18, 19]
print(menor(dados))
print(maior(dados))
print(superior(dados))

# Questão 4
faturamento = {'SP': 67836.43,
              'RJ': 36678.66,
              'MG': 29229.88,
              'ES': 27165.48,
              'Outros': 19849.53}
total = 0
for value in faturamento.values():
    total += value
for key, value in faturamento.items():
    print(f'{key}: {value/total:.2%}')

#Questão 5
palavra = input("Insira a palavra: ")
invertida = ''
for i in range(len(palavra)-1 , -1, -1):
    invertida += palavra[i]
print(invertida)
