import math

#Exercício 1: Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print('Olá mundo!')


#Exercício 2: Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

def mostra_numero():
    numero = input("Digite um número: ",)
    return print(f"O número digitado foi: {numero}")

# mostra_numero()


#Exercício 3: Faça um Programa que peça dois números e imprima a soma.

def soma():
    numero_1 = int(input("Digite um número: ", ))
    numero_2 = int(input("Digite um número: ", ))
    total = numero_1 + numero_2
    return print (f"{numero_1} + {numero_2} = {total}")

# soma()


#Exercício 4: Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def media_notas():
    nota_1 = float(input("Digite a nota do primeiro bimestre: "))
    nota_2 = float(input("Digite a nota do segundo bimestre: "))
    nota_3 = float(input("Digite a nota do terceiro bimestre: "))
    nota_4 = float(input("Digite a nota do quarto bimestre: "))
    total = nota_1 + nota_2 + nota_3 + nota_4
    media = total/4
    return print(f"A méida é: {media}")

# media_notas()


#Exercício 5: Faça um Programa que converta metros para centímetros.

def metros_para_centimetros(metros): # 1 metro = 100 centimetros
    centimetros = 100 * metros
    return print(f"{metros} metros é igual a {centimetros} centímetros.")

# metros_para_centimetros(55.5)


#Exercício 6: Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

def area_circulo(): # Pi * r²
    raio = float(input("Digite o raio do círculo: "))
    area = 3.1415 * raio ** 2
    return print(f'A área do circulo é: {area} m².')

# area_circulo()


#Exercício 7: Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def area_quadrado():
    aresta = float(input("Digite o valor da aresta do quadrado: "))
    area = aresta ** 2
    dobro_area = area * 2
    return print(f'A area desse quadrado é: {area}, e o dobro dessa área é: {dobro_area}')

# area_quadrado()


#Exercício 8: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

def salario_mensal():
    salario_hora = float(input("Digite o valor do seu salário hora: "))
    horas_trabalhadas = int(input("Digite quantas horas você trabalhou no mês: "))
    salario = salario_hora * horas_trabalhadas
    return print(f"O seu salário desse mês é de: {salario}")

# salario_mensal()


#Exercício 9: Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

def fahrenheit_celsius():
    fahrenheit = float(input("Digite o valor da temperatura em fahrenheit: "))
    celsius = round(5 * ((fahrenheit - 32)/9), 2)
    return print(f'A temperatura em celsius é de {celsius} ºC.')

# fahrenheit_celsius()


#Exercício 10: Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

def celsius_fahrenheti():
    celsius = float(input("Digite o valor da temperatura em fahrenheit: "))
    fahrenheit = round((celsius*9/5)+32, 2)
    return print(f'A temperatura em farenheits é de {fahrenheit} ºF.')

# celsius_fahrenheti()


#Exercício 11: Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo.
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.

def contas():
    numero_1 = int(input("Digite um número inteiro: "))
    numero_2 = int(input("Digite outro número inteiro: "))
    numero_3 = float(input("Digite um número real: "))
    resposta_a = (2 * numero_1) * (numero_2 / 2)
    resposta_b = (3 * numero_1) + numero_3
    resposta_c = numero_3 ** 3
    return print(f"""A resposta da questão a: (2 * {numero_1}) * ({numero_2}/2) = {resposta_a}
A resposta da questão b: (3 * {numero_1}) + {numero_3} = {resposta_b}
A resposta da questão c: {numero_3}³ = {resposta_c}""")

# contas()


#Exercício 12: Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
# (72.7 * altura) - 58

def peso_ideal():
    altura = float(input("Digite a sua altura em metros: "))
    peso_ideal = round(altura * 72.7 - 58, 2)
    return print(f"O seu peso ideal é de: {peso_ideal} kg.")

# peso_ideal()


#Exercício 13: Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

def peso_ideal_genero():
    altura = float(input("Digite a sua altura em metros: "))
    genero = input("Digite o seu gênero, homem ou mulher: ")
    if genero == "homem":
        peso = round(altura * 72.7 - 58, 2)
    elif genero == "mulher":
        peso = round(altura * 62.1 - 44.7, 2)
    else:
        return print("Erro no digitar o gênero.")

    return print(f"O seu peso ideal é: {peso} kg.")

# peso_ideal_genero()


#Exercício 14: João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que
# João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

def rendimento():
    peso_peixes = float(input("Digite o peso em kg dos peixes pescados: "))
    limite = 50
    multa_valor = 4.00
    multa = 0 # valor da multa que João deverá pagar
    excesso = 0 # quantidade de quilos além do limite
    if peso_peixes <= limite:
        return print("O peso dos peixes não excedeu o limte.")
    else:
        excesso = peso_peixes - limite
        multa = excesso * multa_valor
        return print(f"Foram pescados {peso_peixes} kg de peixes, excedendo de {excesso} kg do limite permitido gerando uma multa a pagar no valor de {multa} R$.")

# rendimento()


#Exercício 15: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.
# e) calcule os descontos e o salário líquido, conforme a tabela abaixo:

def conta_salarial():
    salario_hora = float(input("Digite o seu salário/hora: "))
    horas_trabalhadas_mes = int(input("Digite quantas horas você trabalhou no mês: "))
    salario_bruto = horas_trabalhadas_mes * salario_hora
    INSS = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    IR = salario_bruto * 0.11
    salario_liquido = salario_bruto - IR - sindicato - INSS
    return print(f"O salário bruto recebido é de {salario_bruto} R$, portanto é devido o pagamento do INSS de {INSS} R$, "
                 f"o pagamento do sindicato de {sindicato} R$, com tais descontos e o Imposto de Renda o salário "
                 f"liquido fica no valor de {salario_liquido} R$.")

# conta_salarial()


#Exercício 16: Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
# a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
# em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas
# e o preço total.

def compra_tinta():
    metros = int(input("Digite quantos metros quadrados a area a ser pintada possui: "))
    latas = math.ceil(metros/54)
    return print(f"Serão necessárias {latas} latas de tinta para pintar a área de {metros} m².")

# compra_tinta()



#Exercício 17: Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
# a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida
# em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
# os valores para cima, isto é, considere latas cheias.

def compra_tinta_2():
    metros = float(input("Digite quantos metros quadrados serão pintados: "))
    area_com_folga = metros * 1.1
    litro = area_com_folga / 6
    latas = math.ceil(litro / 18)
    valor_latas = latas * 80.00
    galao = math.ceil(litro / 3.6)
    valor_galoes = galao * 25.00
    min_latas = litro // 18
    min_galoes = math.ceil((litro % 18) / 3.6)
    valor_min_latas = min_latas * 80.00
    valor_min_galoes = min_galoes * 25.00
    valor_min_total = valor_min_latas + valor_min_galoes
    return print(f"""Para pintar {metros} m² será necessário:
    {latas} latas se forem compradas apenas latas de tinta, totalizando no valor de: {valor_latas} R$,
    {galao} galões se forem comprados apenas galões de tinta, totalizando no valor de {valor_galoes} R$,
    ou {min_latas} latas e {min_galoes} galões se forem combinados, totalizando no valor de {valor_min_total} R$.""")

# compra_tinta_2()


#Exercício 18: Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link
# de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

def velocidade_download():
    tamanho = float(input("Digite o tamanho do arquivo em MB: "))
    internet = float(input("Digite a velocidade da sua internet em Mbps: "))
    segundos = (1_048_576 * tamanho) / (internet * 131_072) # 1_048_576 / 8 = 131_072
    minutos = round(segundos / 60)
    return print(f"O download levará {minutos} minutos.")

# velocidade_download()

teste1 = type(math.floor(19.99/2))
print(teste1)
teste2 = type(19.99//2)
print(teste2)
