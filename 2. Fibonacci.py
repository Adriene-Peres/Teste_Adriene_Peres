'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem 
que desejar onde, informado um número, ele calcule a sequência de Fibonacci e 
retorne uma mensagem avisando se o número informado pertence ou não a sequência

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência 
ou pode ser previamente definido no código;

'''


def fibonacci(number):
    fib = [0, 1]
    while len(fib) < number:
        next_number = fib[-1] + fib[-2]
        fib.append(next_number)
    return fib


def is_number_in_fibonacci(number, sequence):
    if number in sequence:
        print(f'O número {number} pertence à sequência de Fibonacci.')
    else:
        print(f'O número {number} NÃO pertence à sequência de Fibonacci.')


number = int(input('Digite um número: '))
result = fibonacci(number)
print(result)
is_number_in_fibonacci(number, result)
