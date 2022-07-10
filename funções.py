# Exercício 1: Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def triangula_de_numeros(numero: int):
    for i in range(1, numero + 1):
        for _ in range(i):
            print(i, end='   ')
        print()

#triangula_de_numeros(3)


# Exercício 2: Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def triangula_de_numeros_variaveis(numero: int):
    for linha in range(1, numero + 1):
        for coluna in range(1, linha + 1):
            print(coluna, end= '   ')
        print()

triangula_de_numeros_variaveis(4)

# Exercício 3:
# Exercício 4:
# Exercício 5:
# Exercício 6:
# Exercício 7:
# Exercício 8:
# Exercício 9:
# Exercício 10:
# Exercício 11:
# Exercício 12:
# Exercício 13:
# Exercício 14:
