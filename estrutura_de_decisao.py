
#Exercício 21: Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque
# e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão
# as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve
# se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
# uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
# quatro notas de 10, uma nota de 5 e quatro notas de 1.

def caixa_eletronico():
    valor_do_saque = int(input('Quantos reais desejas sacar? '))

    centenas_str = quinzenas_str = dezenas_str = cinco_str = unidades_str = ''

    if valor_do_saque < 10 or valor_do_saque > 600:
        return print("Valor indisponível")
    centenas_int, numero = divmod(valor_do_saque, 100)
    quinzenas_int, numero = divmod(numero, 50)
    dezenas_int, numero = divmod(numero, 10)
    cinco_int, numero = divmod(numero, 5)

    partes_numericas = 0

    if centenas_int == 1:
        centenas_str = "uma nota de 100"
        partes_numericas += 1
    elif centenas_int > 1:

        if centenas_int == 2:
            centena_escrito = 'duas'
        elif centenas_int == 3:
            centena_escrito = 'três'
        elif centenas_int == 4:
            centena_escrito = 'quatro'
        elif centenas_int == 5:
            centena_escrito = 'cinco'
        elif centenas_int == 6:
            centena_escrito = 'seis'

        centenas_str = f'{centena_escrito} notas de 100'
        partes_numericas += 1

    if quinzenas_int == 1:
        quinzenas_str = 'uma nota de 50'
        partes_numericas += 1

    if dezenas_int == 1:
        dezenas_str = 'uma nota de 10'
        partes_numericas += 1
    elif dezenas_int > 1:

        if dezenas_int == 2:
            dezena_escrito = 'duas'
        elif dezenas_int == 3:
            dezena_escrito = 'três'
        elif dezenas_int == 4:
            dezena_escrito = 'quatro'

        dezenas_str = f'{dezena_escrito} notas de 10'
        partes_numericas += 1

    if cinco_int == 1:
        cinco_str = 'uma nota de 5'
        partes_numericas += 1

    if numero == 1:
        unidades_str = 'uma nota de 1.'
        partes_numericas += 1
    elif numero > 1:

        if numero == 2:
            unidade_escrito = 'duas'
        elif numero == 3:
            unidade_escrito = 'três'
        elif numero == 4:
            unidade_escrito = 'quatro'

        unidades_str = f'{unidade_escrito} notas de 1.'
        partes_numericas += 1


    if partes_numericas == 1:
        print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str
              + quinzenas_str + dezenas_str + ".")

    elif partes_numericas == 5:
        print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str + ", "
              + quinzenas_str + ", " + dezenas_str + ", " + cinco_str + " e " + unidades_str)

    elif partes_numericas == 4:
        if centenas_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' +
                  quinzenas_str + ", " + dezenas_str + ", " + cinco_str + " e " + unidades_str)
        elif quinzenas_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str + ", "
                  + dezenas_str + ", " + cinco_str + " e " + unidades_str)
        elif dezenas_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str + ", "
                  + quinzenas_str + ", " + cinco_str + " e " + unidades_str)
        elif cinco_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str + ", "
                  + quinzenas_str + ", " + dezenas_str + " e " + unidades_str)
        else:
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str + ", "
                  + quinzenas_str + ", " + dezenas_str + " e " + cinco_str + ".")

    elif partes_numericas == 3:
        if centenas_str == '' and quinzenas_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece '
                  + dezenas_str + ", " + cinco_str + " e " + unidades_str)
        elif quinzenas_str == '' and dezenas_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str + ", "
                   + cinco_str + " e " + unidades_str)
        elif dezenas_str == '' and cinco_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str + ", "
                  + quinzenas_str + " e " + unidades_str)
        elif cinco_str == '' and unidades_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str + ", "
                  + quinzenas_str + " e " + dezenas_str + ".")
        elif unidades_str == '' and centenas_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + quinzenas_str + ", "
                  + dezenas_str + " e " + cinco_str + ".")

        elif centenas_str == '' and dezenas_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + quinzenas_str + ", "
                  + cinco_str + " e " + unidades_str)
        elif centenas_str == '' and cinco_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + quinzenas_str + ", "
                   + dezenas_str + " e " + unidades_str)

        elif quinzenas_str == '' and cinco_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str + ", "
                  + dezenas_str + " e " + unidades_str)
        elif quinzenas_str == '' and unidades_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str + ", "
                  + dezenas_str + " e " + cinco_str + ".")

        elif dezenas_str == '' and unidades_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str + ", "
                  + quinzenas_str + " e " + cinco_str + ".")
        elif dezenas_str == '' and centenas_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + quinzenas_str + ", "
                  + cinco_str + " e " + unidades_str)

        elif cinco_str == '' and centenas_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + quinzenas_str + ", "
                  + dezenas_str + " e " + unidades_str)
        elif cinco_str == '' and quinzenas_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str + ", "
                  + dezenas_str + " e " + unidades_str)

        elif unidades_str == '' and quinzenas_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str + ", "
                  + dezenas_str + " e " + cinco_str + ".")
        elif unidades_str == '' and dezenas_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str + ", "
                  + quinzenas_str + " e " + cinco_str + ".")


    elif partes_numericas == 2:
        if centenas_str == '' and quinzenas_str == '' and dezenas_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + cinco_str + " e "
                  + unidades_str)
        elif centenas_str == '' and quinzenas_str == '' and cinco_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + dezenas_str + " e "
                      + unidades_str)
        elif centenas_str == '' and quinzenas_str == '' and unidades_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + dezenas_str + " e "
                  + cinco_str + ".")

        elif quinzenas_str == '' and dezenas_str == '' and cinco_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str + " e "
                  + unidades_str)
        elif quinzenas_str == '' and dezenas_str == '' and unidades_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str + " e "
                  + cinco_str + ".")


        elif dezenas_str == '' and cinco_str == '' and unidades_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str + " e "
                  + quinzenas_str + ".")
        elif dezenas_str == '' and cinco_str == '' and centenas_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + quinzenas_str + " e "
                  + unidades_str)

        elif cinco_str == '' and unidades_str == '' and centenas_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + quinzenas_str + " e "
                  + dezenas_str + ".")
        elif cinco_str == '' and unidades_str == '' and quinzenas_str == '':
            print(f'Para sacar a quantia de {valor_do_saque} reais, o programa fornece ' + centenas_str + " e "
                  + dezenas_str + ".")

# caixa_eletronico()
