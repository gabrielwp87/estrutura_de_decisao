#Exercício 1: Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
def exercicio_1():
    lista = []
    for _ in range(5):
        numero = int(input('Digite um número inteiro: '))
        lista.append(numero)
    print(lista)

#exercicio_1()


#Exercício 2: Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

def exercicio_2():
    lista = []
    for i in range(10):
        numero = float(input('Digite um número real: '))
        lista.append(numero)
    lista.reverse()
    print(lista)

#exercicio_2()


#Exercício 3: Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

def exercicio_3():
    lista = []
    soma_das_notas = 0
    for _ in range(4):
        notas = float(input('Digite as notas: '))
        lista.append(notas)
        soma_das_notas += notas
    lista.append(f'a soma das notas é de: {soma_das_notas}')
    media = round(soma_das_notas / 4, 2)
    lista.append(f'a média das notás é de: {media}')
    print(lista)

#exercicio_3()


#Exercício 4: Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
# Imprima as consoantes.

def exercicio_4():
    lista = ['g', 'a', 'b', 'r', 'i', 'e', 'l', 'w', 'p', 'i']
    lista_2 = []
    numero_de_consoantes = 0
    for i in range(len(lista)):
        letra = lista[i]
        if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
            numero_de_consoantes += 1
            lista_2.append(letra)

    print(f'Há {numero_de_consoantes} consoante nesse vetor.')
    print(lista_2)
    print(len(lista)) #conferindo o tamanho da lista

#exercicio_4()


#Exercício 5: Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares
# no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

def exercicio_5():
    lista = []
    lista_par = []
    lista_impar = []
    for numero in range(1, 21):
        #numero = int(input('Digite um número inteiro: '))
        lista.append(numero)
        if numero % 2 == 0:
            lista_par.append(numero)
        else:
            lista_impar.append(numero)
    print(f'A lista original é: {lista}.')
    print(f'A lista de pares é: {lista_par}.')
    print(f'A lsita de ímpares é: {lista_impar}.')

#exercicio_5()


#Exercício 6: Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média
# de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

def exercicio_6():
    pass





#Exercício 7: Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

def exercicio_7():
    lista = []
    soma = 0
    multiplicacao = 1

    for i in range(5):
        numero = int(input('Diginte um número inteiro: '))
        lista.append(numero)
        soma += lista[i]
        multiplicacao *= lista[i]
    print(soma)
    print(multiplicacao)
    print(lista)

#exercicio_7()


#Exercício 8: Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no
# seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.





#Exercício 9: Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a
# soma dos quadrados dos elementos do vetor.






#Exercício 10: Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.





#Exercício 11: Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.





#Exercício 12:
#Exercício 13:
#Exercício 14:
#Exercício 15: Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

def exercício_15():
    lista = []
    lista_inversa = []
    soma = 0
    while True:
        notas = float(input('Digite a nota: '))

        if notas == -1:
            break
        else:
            lista.append(notas)
            lista_inversa.append(notas)
            soma = sum(lista)
    notas_str = ' '.join([str(nota) for nota in lista])
    notas_inversas_str ="\n".join([str(nota) for nota in lista_inversa])

    quantidade_de_notas = len(lista)
    lista_inversa.reverse()
    media = round(soma / quantidade_de_notas, 2)

    valores_acima_da_media_str = ' '.join([str(nota) for nota in lista if nota > media])
    valores_abaixo_de_sete_str = ' '.join([str(nota) for nota in lista if nota < 7])

    print(f'''Foram armazenadas {quantidade_de_notas} notas no total, as quais foram as seguinte: {notas_str}
a ordem inversa das notas é:
{notas_inversas_str},
 a soma das notas é: {soma} e a sua média é: {media},
os valores calculados acima da média são: {valores_acima_da_media_str} e os abaixo de sete são: {valores_abaixo_de_sete_str}.''')

    print('Encerrado programa de estatisticas de notas.')

#exercício_15()


#Exercício 16: Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em
# comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo,
# um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total
# de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários
# nos seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

def exercicio_16():
    salarios = [200, 250, 320, 413, 516, 680, 791, 877, 999, 1000, 2000, 3000]
    contagem_de_faixa_salarial = [0] * 9
    for salario in salarios:
        indice = salario // 100 -2
        indice_maximo = len(contagem_de_faixa_salarial) -1
        indice = min(indice, indice_maximo)
        contagem_de_faixa_salarial[indice] += 1

    print(contagem_de_faixa_salarial)

exercicio_16()



#Exercício 17:
#Exercício 18:
#Exercício 19:
#Exercício 20:
#Exercício 21:
#Exercício 22:
#Exercício 23:
#Exercício 24:
