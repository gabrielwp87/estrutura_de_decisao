# Exercício 1:Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do
# seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
#
# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

def compara_strings():
    string_1 = input('Digite uma string: ')
    string_2 = input('Digite outra string: ')
    tamanho_da_string_1 = len(string_1)
    tamanho_da_string_2 = len(string_2)

    print(f'String 1: {string_1}')
    print(f'String 2: {string_2}')

    print(f'Tamnhao de "{string_1}": {tamanho_da_string_1} caracteres')
    print(f'Tamnhao de "{string_2}": {tamanho_da_string_2} caracteres')


    if tamanho_da_string_1 == tamanho_da_string_2:
        print("As duas strings são de tamanhos iguais.")
    else:
        print("As duas strings são de tamanhos diferentes.")

    if string_1 == string_2:
        print("As duas strings possuem conteúdo iguais.")
    else:
        print("As duas strings possuem conteúdo diferente.")

#compara_strings()

# Exercício 2:Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e
# em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se
# que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

def nome_ao_contrario():
    nome = 'Gabriel Wagner Piazenski'.upper()
    nome_invertido_por_letras_versao_1 = nome[::-1]
    nome_invertido_por_letras_versao_2 = ''.join(reversed(nome))
    nome_invertido_por_palavras = ' '.join(reversed(nome.split()))

    print(f'Nome maisculo: {nome}')
    print(f'Nome invertido por letras, primeira versão: {nome_invertido_por_letras_versao_1}')
    print(f'Nome invertido por letras, segunda versão: {nome_invertido_por_letras_versao_2}')
    print(f'Nome invertido por palavras: {nome_invertido_por_palavras}')

#nome_ao_contrario()


# Exercício 3:Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
# F
# U
# L
# A
# N
# O

def quebra_string():
    palavra = 'DevPro'.upper()
    for i in palavra:
        print(i)

#quebra_string()


# Exercício 4:Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
# F
# FU
# FUL
# FULA
# FULAN
# FULANO

def triangulo_letras():
    palavra = 'DevPro'.upper()
    tamanho = len(palavra)
    letra = 1
    while letra <= tamanho:
        print(palavra[:letra])
        letra += 1

#triangulo_letras()


# Exercício 5:Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
# FULANO
# FULAN
# FULA
# FUL
# FU
# F


def triangulo_letras_inverso():
    palavra = 'DevPro'.upper()
    while palavra != '':
        print(palavra)
        palavra = palavra[:-1]

#triangulo_letras_inverso()


# Exercício 6:
# Exercício 7:
# Exercício 8:
# Exercício 9:
# Exercício 10:

# Exercício 11:Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo
# texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
#
# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!
#
# Digite uma letra: O
# A palavra é: _ _ _ _ O
#
# Digite uma letra: E
# A palavra é: _ E _ _ O
#
# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!

def forca():
    palavra = "DevPro".upper()

    print('Jogo da Forca')
    print('Descubra a palavra')

    print('A palabra é: ', end='')
    for letra in palavra:
        print('_ ', end='')

    conjunto_letras_palavras = set(palavra)
    conjunto_letras_digitadas = set()
    erros = 0

    while (not conjunto_letras_palavras.issubset(conjunto_letras_digitadas)) and erros < 7:
        print()
        print()
        letra_digitada = input('Digite uma letra: ').upper()
        conjunto_letras_digitadas.add(letra_digitada)
        if letra_digitada in conjunto_letras_palavras:
            print('A palavra é: ', end='')
            for letra in palavra:
                if letra in conjunto_letras_digitadas:
                    print(f'{letra} ', end='')
                else:
                    print('_ ', end='')
        else:
            erros += 1
            if erros < 7:
                print(f'-> Você errou pela {erros}ª vez de 6. Tente de novo!')
            else:
                print(f'-> Você errou pela {erros}ª vez de 6.')

        print()
        print('Letras já digitadas: ', conjunto_letras_digitadas)

    if erros < 7:
        print('Parabéns, você ganhou!!!')
    else:
        print('Infelizmento você perdeu!')

#forca()






# Exercício 12:
# Exercício 13:
# Exercício 14:
