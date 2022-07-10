import math

#Exercício 1: Faça um Programa que peça dois números e imprima o maior deles.

def numero_maior():
    numero_1 = int(input("Digite um número: "))
    numero_2 = int(input("Digite outro número: "))
    if numero_1 > numero_2:
        return print(f"O número {numero_1} é maior que o número {numero_2}.")
    elif numero_1 < numero_2:
        return print(f"O número {numero_2} é maior que o número {numero_1}.")
    else:
        return print(f"Os números são iguais, {numero_1} = {numero_2}.")

# numero_maior()


#Exercício 2: Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

def positivo_negativo():
    numero = int(input("Digite um número positivo ou negativo: "))
    if numero >= 0:
        return print(f"O número {numero} possui valor positivo.")
    else:
        return print(f"O número {numero} possui valor negativo.")

# positivo_negativo()


#Exercício 3: Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

def genero():
    genero = input("Digite o seu gênero: F para feminino, M para masculino ou I para indefinido: ").upper()
    if genero == "F":
        return print("O seu gênero é feminino.")
    elif genero == "M":
        return print("O seu gênero é masculino.")
    elif genero == "I":
        return print("O seu gênero é indefinido.")
    else:
        return print("Sexo inválido")

# genero()


#Exercício 4: Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def vogal_consoante():
    letra = input("Digite uma letra: ").lower()
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return print(f"A letra '{letra}' é uma volga.")
    else:
        return print(f"A letra '{letra}' é uma consoante.")

# vogal_consoante()


#Exercício 5: Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

def media():
    nota_1 = float(input("Digite a primeira nota do aluno: "))
    nota_2 = float(input("Digite a segunda nota do aluno: "))
    total = nota_1 + nota_2
    media = total / 2
    if media == 10:
        return print("O aluno foi aprovado com distinção tendo a média 10.")
    elif media >= 7:
        return print(f"O aluno está aprovado com a média {media}.")
    else:
        return print(f"O aluno está reprovado com a média {media}.")

# media()


#Exercício 6: Faça um Programa que leia três números e mostre o maior deles.

def maior_numero():
    print("Digite 3 números.")
    numero_1 = int(input("Digite o primeiro número: "))
    numero_2 = int(input("Digite o segundo número: "))
    numero_3 = int(input("Digite o terceiro número: "))
    if numero_1 > numero_2 and numero_1 > numero_3:
        return print(f"O primeiro número digito, de valor {numero_1}, é o de maior valor.")
    elif numero_2 > numero_1 and numero_2 > numero_3:
        return print(f"O segundo número digitado, de valor {numero_2}, é o de maior valor. ")
    elif numero_3 > numero_1 and numero_3 > numero_2:
        return print(f"O terceiro número digitado, de valor {numero_3}, é o de maior valor.")
    else:
        return print(f"Algum dos números digitados é igual ao outro, {numero_1}, {numero_2}, {numero_3}.")

# maior_numero()


#Exercício 7: Faça um Programa que leia três números e mostre o maior e o menor deles.

def maior_menor():
    print("Digite 3 números.")
    numero_1 = int(input("Digite o primeiro número: "))
    numero_2 = int(input("Digite o segundo número: "))
    numero_3 = int(input("DIgite o terceiro número: "))
    if numero_1 >= numero_2 and numero_1 >= numero_3:
        maior_numero = numero_1
    elif numero_2 >= numero_1 and numero_2 >= numero_3:
        maior_numero = numero_2
    elif numero_3 >= numero_1 and numero_3 >= numero_2:
        maior_numero = numero_3

    if numero_1 <= numero_2 and numero_1 <= numero_3:
        menor_numero = numero_1
    elif numero_2 <= numero_1 and numero_2 <= numero_3:
        menor_numero = numero_2
    elif numero_3 <= numero_1 and numero_3 <= numero_2:
        menor_numero = numero_3

    return print(f"O maior número digitado foi o {maior_numero} e o menor número foi o {menor_numero}.")

# maior_menor()


#Exercício 8: Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

def produto_mais_barato():
    print("Digite o nome e depois o valor de 3 produtos.")
    nome_produto_1 = input("Qual é o primeiro produto? ")
    produto_1 = float(input("Qual o valor do primeiro produto? "))
    nome_produto_2 = input("Qual é o segundo produto? ")
    produto_2 = float(input("qual o valor do segundo produto? "))
    nome_produto_3 = input("Que é o terceiro produto? ")
    produto_3 = float(input("Qual o valor do terceiro produto? "))

    if produto_1 < produto_2 and produto_1 < produto_3:
        return print(f"O produto {nome_produto_1} é o mais barato no valor de R$ {produto_1}.")
    elif produto_2 < produto_1 and produto_2 < produto_3:
        return print(f"O produto {nome_produto_2} é o mais barato no valor de R$ {produto_2}.")
    elif produto_3 < produto_1 and produto_3 < produto_1:
        return print(f"O produto {nome_produto_3} é o mais barato no valor de R$ {produto_3}.")
    else:
        if produto_1 == produto_2 and produto_1 != produto_3:
            return print(f"Os produtos {nome_produto_1} e {nome_produto_2}é o mais barato no valor de R$ {produto_1}.")
        if produto_1 == produto_3 and produto_1 != produto_3:
            return print(f"Os produtos {nome_produto_1} e {nome_produto_3}é o mais barato no valor de R$ {produto_1}.")
        if produto_2 == produto_3 and produto_1 != produto_2:
            return print(f"Os produtos {nome_produto_2} e {nome_produto_3}é o mais barato no valor de R$ {produto_2}.")
        else:
            return print(f"Os 3 produtos apresentam o mesmo valor de R$ {produto_1}.")

# produto_mais_barato()


#Exercício 9: Faça um Programa que leia três números e mostre-os em ordem decrescente.

def ordem_crescente():
    print("Digite 3 números:")
    numero_1 = int(input("Digite o primeiro número: "))
    numero_2 = int(input("Digite o segundo número: "))
    numero_3 = int(input("Digite o terceiro número: "))

    if numero_1 >= numero_2 and numero_1 >= numero_3:
        numero_maior = numero_1
        if numero_2 >= numero_3:
            numero_medio = numero_2
            numero_menor = numero_3
        else:
            numero_medio = numero_3
            numero_menor = numero_2

    elif numero_2 >= numero_1 and numero_2 >= numero_3:
        numero_maior = numero_2
        if numero_1 >= numero_3:
            numero_medio = numero_1
            numero_menor = numero_3
        else:
            numero_medio = numero_3
            numero_menor = numero_1

    else:
        numero_maior = numero_3
        if numero_1 >= numero_2:
            numero_medio = numero_1
            numero_maior = numero_2
        else:
            numero_medio = numero_2
            numero_menor = numero_1

    return print(f"A ordem crescente dos números digitado é: {numero_menor}, {numero_medio} e {numero_maior}.")

# ordem_crescente()


#Exercício 10: Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino
# ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def turno_estudo():
    print("Qual o turno dos seus estudos?")
    turno = input("Digite M para matutino, V para vespertino e N para noturno: ").upper()
    if turno == "M":
        return print("Bom Dia!")
    elif turno == "V":
        return print("Boa Tarde!")
    elif turno == "N":
        return print("Boa Noite!")
    else:
        return print("Valor Inválido")

# turno_estudo()


#Exercício 11: As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram
# para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

def aumento_salarial():
    salario_antigo = float(input("Informe o salário a ser ajustado: "))

    if salario_antigo <= 280:
        percentual = 20
        aumento = round(salario_antigo * 0.20, 2)
        salario_novo = round(salario_antigo * 1.20, 2)
    elif salario_antigo <= 700:
        percentual = 15
        aumento = round(salario_antigo * 0.15, 2)
        salario_novo = round(salario_antigo * 1.15, 2)
    elif salario_antigo <= 1500:
        percentual = 10
        aumento = round(salario_antigo * 0.10, 2)
        salario_novo = round(salario_antigo * 1.10, 2)
    else:
        percentual = 5
        aumento = round(salario_antigo * 0.05, 2)
        salario_novo = round(salario_antigo * 1.05, 2)

    return print(f"O salario antes do ajuste é de R$ {salario_antigo}, assim ele sofre o ajuste "
                 f"de {percentual}% aumentando de R$ {aumento}, totalizando em R$ {salario_novo}.")

# aumento_salarial()


#Exercício 12: Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto
# de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11%
# do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
# menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

def folha_de_pagamento():
    salario_bruto = float(input("Digite aqui o valor do salário bruto recebido: "))

    if salario_bruto <= 1500 and salario_bruto > 900:
        IR = 0.05
    elif salario_bruto <= 2500:
        IR = 0.1
    else:
        IR = 0.2
    IR_percentual = int(IR * 100)
    IR_valor = IR * salario_bruto
    INSS = salario_bruto * 0.1
    FGTS = salario_bruto * 0.11
    descontos = IR_valor + INSS
    salario_liquido = salario_bruto - descontos
    return print(f"""Salário Bruto:              R$ {salario_bruto}
IR ({IR_percentual}%):                    R$ {IR_valor}
INSS (10%):                 R$ {INSS}
FGTS (11%):                 R$ {FGTS}
Total de descontos:         R$ {descontos}
Salário líquido:            R$ {salario_liquido}""")

# folha_de_pagamento()


#Exercício 13: Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

def dia_da_semana():
    dia = int(input("Digite um valor de 1 a 7 para obter um dia da semana: "))

    if dia == 1:
        dia_da_semana = "Domingo"
    elif dia == 2:
        dia_da_semana = "Segunda-feria"
    elif dia == 3:
        dia_da_semana = "Terça-feira"
    elif dia == 4:
        dia_da_semana = "Quarta-feira"
    elif dia == 5:
        dia_da_semana = "Quinta-feira"
    elif dia == 6:
        dia_da_semana = "Sexta-feira"
    elif dia == 7:
        dia_da_semana = "Sábado"
    else:
        return print("O valor digitado é inválido.")

    return print(f"O dia correspondente é {dia_da_semana}.")

# dia_da_semana()


#Exercício 14: Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um
# semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
 #Média de Aproveitamento  Conceito
  #Entre 9.0 e 10.0        A
  #Entre 7.5 e 9.0         B
  #Entre 6.0 e 7.5         C
  #Entre 4.0 e 6.0         D
  #Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
# conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

def calcula_media():
    nota_1 = float(input("Digite a primeira nota do aluno: "))
    nota_2 = float(input("Digite a segunda nota do aluno: "))
    total = nota_1 + nota_2
    media = round(total / 2, 2)
    if media >= 9:
        conceito = "A"
        resultado = "Aprovado"
    elif media >= 7.5:
        conceito = "B"
        resultado = "Aprovado"
    elif media >= 6:
        conceito = "C"
        resultado = "Aprovado"
    elif media >= 4:
        conceito = "D"
        resultado = "Reprovado"
    else:
        conceito = "E"
        resultado = "Reprovado"

    return print(f"Com as notas {nota_1} e {nota_2}, apresentano a média {media} o aluno conseguiu o conceito {conceito}"
                 f" estando {resultado}.")

# calcula_media()


#Exercício 15: Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem
# ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;


def triangulo():
    lado_1 = float(input("Digite o valor de um lado: "))
    lado_2 = float(input("Digite o valor de outro lado: "))
    lado_3 = float(input("Digite o valor do último lado: "))
    if lado_1 > 0 and lado_2 > 0 and lado_3 > 0:
        if lado_1 == lado_2 and lado_2 == lado_3:
            triangulo = "Equilátero"
        elif lado_1 == lado_2 and lado_1 != lado_3:
            triangulo = "Isósceles"
        elif lado_2 == lado_3 and lado_2 != lado_1:
            triangulo = "Isóceles"
        elif lado_1 == lado_3 and lado_1 != lado_2:
            triangulo = "Isóceles"
        elif lado_1 != lado_2 and lado_2 != lado_3:
            triangulo = "Escaleno"
    else:
        return print("Valores não formam um trinângulo.")

    return print(f"O triângulo de lados {lado_1}, {lado_2} e {lado_3} é um triângulo {triangulo}.")

# triangulo()


#Exercício 16: Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax^2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes
# situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir
# os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

def raizes():
    print("Uma equação de segundo grau tem a seguinte forma Ax² + Bx + C.")
    valor_de_a = int(input("Digite o valor de A: "))
    if valor_de_a == 0:
        return print("Essa não é uma equação de segundo grau!")
    valor_de_b = int(input("Digite o valor de B: "))
    valor_de_c = int(input("Digite o valor de C: "))

    delta = valor_de_b ** 2 - 4 * valor_de_a * valor_de_c
    if delta < 0:
        return print("Essa equação não possui raízes reais!")

    if delta == 0:
        resultado = (valor_de_b * -1) / 2 * valor_de_a
        return print(f"Essa equação possui apenas uma raiz real que é {resultado}.")
    raiz_de_delta = math.sqrt(delta)
    resultado_1 = (valor_de_b * -1 + raiz_de_delta) / 2 * valor_de_a
    resultado_2 = (valor_de_b * -1 - raiz_de_delta) / 2 * valor_de_a

    return print(f"Essa equação possui as raizes {resultado_1} e  {resultado_2}.")

# raizes()


#Exercício 17: Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe
# se este ano é ou não bissexto.

def bissexto():
    ano = int(input("Informe o ano: "))

    if ano % 4 == 0 and ano % 100 != 0:
        return print(f"O ano {ano} é bissexto.")
    elif ano % 400 == 0:
        return print(f"O ano {ano} é bissexto.")

    return print(f"O ano {ano} não é bissexto.")

# bissexto()


#Exercício 18: Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

def data_valida():
    print("Preencha uma data dd/mm/aaaa.")
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))

    if ano % 4 == 0 and ano % 100 != 0:
        ano_bissexto = 1
    elif ano % 400 == 0:
        ano_bissexto = 1
    else:
        ano_bissexto = 0


    if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12:
        if mes == 2: # caso de fevereiro
            if ano_bissexto:
                if dia > 29:
                    return print("Data inválida.")
            else:
                if dia > 28:
                    return print("Data inválida.")

        elif mes % 2 == 0: # caso dos meses que tem apenas 30 dias
            if dia > 30:
                return print("Data inválida.")

    else:
        return print("Data inválida.")

    if ano < 0:
        ano *= -1
        complemento = "AC"
    else:
        complemento = "DC"

    dia_string = str(dia).zfill(2)
    mes_string = str(mes).zfill(2)
    ano_string = str(ano).zfill(4)

    return print(f"A data {dia_string}/{mes_string}/{ano_string} {complemento} é válida.")


# data_valida()


#Exercício 19: Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas
# e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

def ordem_numero():
    numero = int(input("Digite um numero inteiro: "))

    centena_str = dezena_str = unidade_str = ''

    centena_int, numero = divmod(numero, 100) # essa função vai pegar o valor de número, dividir por 100 e colocar
    # a parte inteira na primeira variável (centena_int) e o resto na segunda variável (numero)
    # é como se fosse a feito: primeira_variavel = numero // 100 e segunda_variavel = numero % 100

    partes_numericas = 0

    if centena_int == 1:
        centena_str = "1 centena"
        partes_numericas += 1
    elif centena_int > 1:
        centena_str = f"{centena_int} centenas"
        partes_numericas += 1

    dezena_int, numero = divmod(numero, 10)
    if dezena_int == 1:
        dezena_str = "1 dezena"
        partes_numericas += 1
    elif dezena_int > 1:
        dezena_str = f"{dezena_int} dezenas"
        partes_numericas += 1

    if numero == 1:
        unidade_str = "1 unidade"
        partes_numericas += 1
    elif numero > 1:
        unidade_str = f"{numero} unidades"
        partes_numericas += 1

    if partes_numericas == 0:
        print('Número 0 não possui centenas, dezenas ou unidades.')

    elif partes_numericas == 1:
        print(centena_str + dezena_str + unidade_str)

    elif partes_numericas == 3:
        print(f'{centena_str}, {dezena_str} e {unidade_str}')

    elif partes_numericas == 2:
        if centena_str != '':
            segunda_parte = dezena_str + unidade_str
            print(f'{centena_str} e {segunda_parte}')
        else:
            print(f'{dezena_str} e {unidade_str}')

# ordem_numero()


#Exercício 20: Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular
# a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

def calcula_media_3():
    nota_1 = float(input("Digite o valor da primeira nota: "))
    nota_2 = float(input("Digite o valor da segunda nota: "))
    nota_3 = float(input("Digite o valor da terceira nota: "))
    total = nota_1 + nota_2 + nota_3
    media = total / 3

    if media == 10:
        return print("Aluno aprovado com distinção.")
    elif media >= 7:
        return print("Aluno aprovado.")
    else:
        return print("Aluno reprovado.")

# calcula_media_3()


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


#Exercício 22: Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).

def par_impar():
    numero = int(input("Digite um número: "))
    resultado = numero % 2
    if resultado == 0:
        print(f'O {numero} é par.')
    else:
        print(f'O {numero} é ímpar.')

# par_impar()


#Exercício 23: Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.

def inteiro_ou_decimal():
    numero = float(input("Digite um numero: "))
    interiro, decimal = divmod(numero, 1)
    if decimal != 0:
        print(f'O número {numero} é decimal')
    else:
        print(f'O número {numero} é inteiro')

# inteiro_ou_decimal()



#Exercício 24: Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

def ler_dois_numeros():
    numero_1 = float(input("Digite um número: "))
    numero_2 = float(input("Digite outro número: "))
    print("Escolha uma operação:")
    escolha = int(input("""Digite 1 para somar,
    2 para subtrair, 
    3 para multiplicar,
    4 para dividir.
    """))
    if escolha == 1:
        resultado = numero_1 + numero_2
        operacao = 'soma'
    elif escolha == 2:
        resultado = numero_1 - numero_2
        operacao = 'subtração'
    elif escolha == 3:
        resultado = numero_1 * numero_2
        operacao = 'multiplicação'
    elif escolha == 4:
        resultado = numero_1 / numero_2
        operacao = 'divisão'
    else:
        print("O número ou a escolha não são válidos.")

    par_ou_impar = resultado % 2

    if par_ou_impar == 0:
        par_impar = 'par'
    else:
        par_impar = 'ímpar'

    if resultado >= 0:
        positivo_negativo = 'positivo'
    else:
        positivo_negativo = 'negativo'

    valor_inteiro = math.ceil(resultado)

    if valor_inteiro == resultado:
        inteiro_decimal = 'inteiro'
    else:
        inteiro_decimal = 'decimal'

    print(f'O resultado da {operacao} é {resultado}, o qual é {par_impar}, {positivo_negativo} e {inteiro_decimal}.')

# ler_dois_numeros()


#Exercício 25: Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação
# da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada # como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def classificacao():
    print("Responda 'S' para sim e 'N' para não nas perguntas a seguir:")
    telefone = input("Telefonou para a vítima? ").upper()
    local = input("Esteve no local do crime? ").upper()
    mora = input("Mora perto da vítma? ").upper()
    divida = input("Devia para a vítima? ").upper()
    trabalho = input("Já trabalhou com a vítima? ").upper()

    suspeito = 0

    if telefone == 'S':
        suspeito += 1
    if local == 'S':
        suspeito += 1
    if mora == 'S':
        suspeito += 1
    if divida == 'S':
        suspeito += 1
    if trabalho == 'S':
        suspeito += 1

    if suspeito == 2:
        print("Pessoa classificada como Suspeita.")
    elif suspeito == 3 or suspeito == 4:
        print("Pessoa classificada como Cúmplice.")
    elif suspeito == 5:
        print("Pessoa classificada como Assassino.")
    else:
        print("Pessoa classificada como Inocente.")

# classificacao()


#Exercício 26:Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool: até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina: até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago
# pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90

def abastecimento():
    print("Qual o tipo de combustível será usado?")
    combustivel = input("Digite A para álcool e G para gasolina: ").upper()
    quantidade = float(input("Quantos litros serão abastecidos? "))

    if combustivel == 'A' and quantidade <= 20:
        preco = (quantidade * 1.9) * 0.97
    elif combustivel == 'A' and quantidade > 20:
        preco = (quantidade * 1.9) * 0.95
    elif combustivel == 'G' and quantidade <= 20:
        preco = quantidade * 2.5 * 0.96
    elif combustivel == 'G' and quantidade > 20:
        preco = quantidade * 2.5 * 0.94
    else:
        print("Erro, favor repetir a operação!")
    preco = round(preco, 2)

    print(f'O valor a ser pago é de R$ {preco}.')

# abastecimento()


#Exercício 27: Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda
# um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
# (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

def fruteira():
    print("Digite 1 para comprar morgano e 2 para comprar maçã.")
    fruta = int(input("Fruta escolhida é: "))
    quantidade = float(input("Qual a quantidade desejada? "))

    if fruta == 1:
        fruta_str = 'morango'
        if quantidade <= 5:
            preco = 2.5
        else:
            preco = 2.2

    elif fruta == 2:
        fruta_str = 'maçã'
        if quantidade <= 5:
            preco = 1.8
        else:
            preco = 1.5
    else:
        print("Erro na escolha, por favor tente novamente!")

    pagar = round(quantidade * preco, 2)
    if pagar > 25 or quantidade > 8:
        pagar = round(quantidade * preco * 0.9, 2)



    print(f'O valor total a ser pago pela {fruta_str} é de R$ {pagar}')

# fruteira()



#Exercício 28: O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
# receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne
# comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne,
# preço total, tipo de pagamento, valor do desconto e valor a pagar.

def carnes():
    print("""Escolha o seu tipode carne: 
    1 para File Duplo
    2 para Alcatra
    3 para Picanha""")
    carne = int(input("Qual o número da carne escolhida? "))
    quantidade = float(input("Qual a quantidade de kg desejada? "))
    cartao = input("Será usado o cartão tabajara como pagamento? S para sim e N para não: ").upper()

    if carne == 1:
        carne_str = 'File Duplo'
        if quantidade <= 5:
            preco = 4.9
        else:
            preco = 5.8

    elif carne == 2:
        carne_str = 'Alcatra'
        if quantidade <= 5:
            preco = 5.9
        else:
            preco = 6.8

    elif carne == 3:
        carne_str = 'Picanha'
        if quantidade <= 5:
            preco = 6.9
        else:
            preco = 7.8

    else:
        print("Problemas com as informações recebidas, por favor repetir a operação!")

    valor_a_pagar = round(quantidade * preco, 2)

    if cartao == 'S':
        valor_a_pagar = round(valor_a_pagar * 0.95, 2)
        desconto = round(valor_a_pagar * 0.05, 2)
        print(f"Pela quantidade de {quantidade}kg a {carne_str} custa R$ {valor_a_pagar}, sendo paga com o cartão"
              f" tabajara e apresentando um desconto de R$ {desconto}")
    else:
        print(f"Pela quantidade de {quantidade}kg a {carne_str} custa R$ {valor_a_pagar}, sendo paga com cartão"
              f" normal e sem desconto especial.")

# carnes()





