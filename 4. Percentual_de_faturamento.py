'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por 
estado:

SP - R$67.836,43
RJ - R$36.678,66
MG - R$29.229,88
ES - R$27.165,48
Outros - R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de 
representação que cada estado teve dentro do valor total mensal da 
distribuidora.
'''

faturamentos = [{'estado': 'SP', 'valor': 67836.43},
                {'estado': 'RJ', 'valor': 36678.66},
                {'estado': 'MG', 'valor': 29229.88},
                {'estado': 'ES', 'valor': 27165.48},
                {'estado': 'Outros', 'valor': 19849.53},
                ]


def total_(faturamento):
    total = 0
    for item in faturamento:
        total += item['valor']
    return total


def percentage_of_each_state(faturamento, total):
    return [
        {**item, 'valor': round((item['valor']/total)*100, 2)}
        for item in faturamentos
    ]


total = total_(faturamentos)
percentage = percentage_of_each_state(faturamentos, total)
print('O percentual de representação de cada estado é: ')
for item in percentage:
    print(item)
