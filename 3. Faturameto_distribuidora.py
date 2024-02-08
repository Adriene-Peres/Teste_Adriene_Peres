'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, 
faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior 
à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados.
Estes dias devem ser ignorados no cálculo da média;
'''
import json


def lower_value(dados):
    return min(dados, key=lambda f: f['valor'])


def highest_value(dados):
    return max(dados, key=lambda f: f['valor'])


def monthly_average(dados):
    cont = 0
    soma = 0
    for dado in dados:
        if dado['valor'] != 0.0:
            cont += 1
            soma = + dado['valor']

    return soma/cont


def days_higher_than_average(dados, media):
    cont = 0
    for dado in dados:
        if dado['valor'] > media:
            cont += 1

    return cont


with open('dados.json', 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)

x = lower_value(dados)
print(f'Menor faturamento: {x["valor"]}')
x = highest_value(dados)
print(f'Maior faturamento: {x["valor"]}')
media = monthly_average(dados)
x = days_higher_than_average(dados, media)
print(f'Dias de valor de faturamento diário superior à média mensal: {x}')
