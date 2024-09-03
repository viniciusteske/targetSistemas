""" 
Questão 1
 Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?
"""
indice = 13
soma = 0
k = 0
while(k < indice):
    k += 1
    soma += k
    
print("Resposta questão 1:")
print(soma)

""" 
Questão 2
 Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o 
 próximo valor sempre será a soma dos 2 valores anteriores 
 (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa 
 na linguagem que desejar onde, informado um número, ele calcule a 
 sequência de Fibonacci e retorne uma mensagem avisando se o número 
 informado pertence ou não a sequência.
"""
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
print("Resposta questão 2:")
print(pertence(m))

"""
Questão 3
3) Dado um vetor que guarda o valor de faturamento diário de uma 
distribuidora, faça um programa, na linguagem que desejar, que calcule 
e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior 
à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento 
mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e 
feriados. Estes dias devem ser ignorados no cálculo da média;

# Json ou XML não disponível.

# import json

# with open('data.json', 'r') as file:
#     dados = json.load(file)
"""
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

print("Resposta questão 3:")
print(menor(dados))
print(maior(dados))
print(superior(dados))

"""
Questão 4
4) Dado o valor de faturamento mensal de uma distribuidora, 
detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o 
percentual de representação que cada estado teve dentro do valor
total mensal da distribuidora. 
"""
faturamento = {'SP': 67836.43,
              'RJ': 36678.66,
              'MG': 29229.88,
              'ES': 27165.48,
              'Outros': 19849.53}
total = 0
for value in faturamento.values():
    total += value
print("Resposta questão 4:")
for key, value in faturamento.items():
    print(f'{key}: {value/total:.2%}')

"""
Questão 5
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua 
preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""
palavra = input("Insira a palavra: ")
invertida = ''
for i in range(len(palavra)-1 , -1, -1):
    invertida += palavra[i]

print("Resposta questão 5:")
print(invertida)
