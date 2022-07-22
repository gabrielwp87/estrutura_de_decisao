# Exercícios

def contar_caracteres(s):
    """Função que conta os caracters de uma string

    Ex.:
    >>> contar_caracters('renzo')
    e: 1
    n: 1
    r: 1
    o: 1
    z: 1
    >>> contar_caracters('banana')
    a: 3
    b: 1
    n: 2

    :param s: string a ser contada

    """
    caracteres_ordenados = sorted(s) #o método sorted() pode ser aplicado a qualquer iterável, e a string é iterável

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1

    print(f'{caracter_anterior}: {contagem}')
    """como o for trabalha com o caracter anteior o último caracter fica fora do loop, assim é necessário usar o print
    mais uma vez"""

if __name__ == '__main__':
    print('Versão inicial do contador de caractéres')
    contar_caracteres('renzo')
    print()
    contar_caracteres('banana')
    print()
    contar_caracteres('gabriel')
    print()
    print()




def contar_caracteres_com_dicionario(s):
    """Função que conta os caracters de uma string

    Ex.:
    >>> contar_caracters('renzo')
    {'e': 1, 'n': 1, 'r': 1, 'o': 1, 'z': 1,} #essa virgula no fim é opcional, deixei para lembrar disso
    >>> contar_caracters('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada

    """
    caracteres_ordenados = sorted(s) #o método sorted() pode ser aplicado a qualquer iterável, e a string é iterável

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    resultado = {}

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            resultado[caracter_anterior] = contagem
            caracter_anterior = caracter
            contagem = 1

    resultado[caracter_anterior] = contagem
    return resultado

    """como o 'for' trabalha com o caracter anteior o último caracter fica fora do loop, assim é necessário acrescentar
    o último caracter no dicionário."""

if __name__ == '__main__':
    print('Versão 1 usando dicionário')
    print(contar_caracteres_com_dicionario('renzo'))
    print()
    print(contar_caracteres_com_dicionario('banana'))
    print()
    print(contar_caracteres_com_dicionario('gabriel'))
    print()
    print()



def contar_caracteres_com_dicionario_versao2(s):
    """Função que conta os caracters de uma string

    Ex.:
    >>> contar_caracters('renzo')
    {'e': 1, 'n': 1, 'r': 1, 'o': 1, 'z': 1,} #essa virgula no fim é opcional, deixei para lembrar disso
    >>> contar_caracters('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada

    Essa é um versão aprimorada, mais enxuta.
    """
    resultado = {}

    for caracter in s:
        contagem = resultado.get(caracter, 0)
        contagem += 1
        resultado[caracter] = contagem

    return resultado


if __name__ == '__main__':
    print('Versão 2 usando dicionário')
    print(contar_caracteres_com_dicionario_versao2('renzo'))
    print()
    print(contar_caracteres_com_dicionario_versao2('banana'))
    print()
    print(contar_caracteres_com_dicionario_versao2('gabriel'))
    print()
    print()



def contar_caracteres_com_dicionario_versao3(s):
    """Função que conta os caracters de uma string

    Ex.:
    >>> contar_caracters('renzo')
    {'e': 1, 'n': 1, 'r': 1, 'o': 1, 'z': 1,} #essa virgula no fim é opcional, deixei para lembrar disso
    >>> contar_caracters('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada

    Essa é um versão aprimorada, mais enxuta.
    """
    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado
"""Nessa versão deixou-se o código mais enxuto, mas a ideia dele é igual a da versão 2, só em vez de ter a variável 
auxilar (contagem) foi feito tudo direto, e já foi somado de mais 1."""

if __name__ == '__main__':
    print('Versão 3 usando dicionário')
    print(contar_caracteres_com_dicionario_versao2('renzo'))
    print()
    print(contar_caracteres_com_dicionario_versao2('banana'))
    print()
    print(contar_caracteres_com_dicionario_versao2('gabriel'))
