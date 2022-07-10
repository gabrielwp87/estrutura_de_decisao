#Exercício 1: Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
# e continue pedindo até que o usuário informe um valor válido.

def pede_numero():
    while True:
        try:
            numero = int(input("Digite um numero inteiro de 0 a 10: "))
        except:
            print("Deve ser fornecido um numero inteiro.")
        else:
            if numero >= 0 and numero <= 10:
                print(f'O número informado é {numero}.')
                break
            else:
                print("O número deve estar entre 0 a 10.")

# pede_numero()

#Exercício 2: Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

def login():
    while True:
        usuario = input('Digite seu usuário: ')
        senha = input('Digite a senha: ')
        tentativa = usuario == senha
        if tentativa:
           print("Login ou senha incorretos ou inválidos.")
        else:
            print('Usuário e senha válidos.')
            break

# login()


#Exercício 3:Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

def identificacao():
    while True:
        nome = input('Digite o seu nome: ')

        if len(nome) > 3:
            try:
                idade = int(input('Digite sua idade: '))
            except ValueError:
                print('Digiete um número como idade')

            else:
                if idade >= 0 and idade <=150:

                    salario = float(input('Digite o valor do seu salário: '))
                    if salario > 0:

                        sexo = input('Digite o seu sexo, f para feminino e m para masculino: ').lower()

                        if sexo == 'f' or sexo == 'm':

                            estado_civil = input("""Digite o seu estado civil
                            s para soloteiro(a)
                            c para casado(a)
                            v para viúvo(a)
                            d para divorciado(a) -> """).lower()

                            if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
                                break

                            else:
                                print('Estado civil inválido.')

                        else:
                            print('Sexo inválido.')

                    else:
                        print('A salário precisa apresentar valor positivo.')

                else:
                    print('A idade deve ser entre 0 e 150')

        else:
            print('O nome deve possuir mais de 3 letras.')
    print('Dados apresentados são válidos.')

# identificacao()


#Exercício 4: Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual
# de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou
# iguale a população do país B, mantidas as taxas de crescimento.

def comparacao_populacao():
    populacao_pais_A = 80_000
    taxa_de_crescimento_da_populacao_A = 1.03
    populacao_pais_B = 200_000
    taxa_de_crescimento_da_populacao_B = 1.015
    conta_anos = 0

    while populacao_pais_A < populacao_pais_B:
        conta_anos += 1
        populacao_pais_A *= taxa_de_crescimento_da_populacao_A
        populacao_pais_B *= taxa_de_crescimento_da_populacao_B

    populacao_pais_A = int(populacao_pais_A)
    populacao_pais_B = int(populacao_pais_B)
    print(f'Foram necessários {conta_anos} anos para que a polução do país A igualasse ou superasse a '
          f'população do país B.')
    print(f'A população final do país A é de {populacao_pais_A}.')
    print(f'A população final do país B é de {populacao_pais_B}.')

# comparacao_populacao()

#Exercício 5: Altere o programa anterior permitindo ao usuário informar as populações e as taxas de
# crescimento iniciais. Valide a entrada e permita repetir a operação.


def comparacao_populacao_editavel():
    populacao_pais_A = int(input("Digite o tamanho da população do país A: "))
    taxa_de_crescimento_da_populacao_A = float((input("Digite a taxa de crescimento do país A: ")))
    populacao_pais_B = int(input("Digite o tamanho da população do país B: "))
    taxa_de_crescimento_da_populacao_B = float(input("Digite a taxa de crescimento do país B: "))
    conta_anos = 0
    while populacao_pais_A < populacao_pais_B:
        conta_anos += 1
        populacao_pais_A *= taxa_de_crescimento_da_populacao_A
        populacao_pais_B *= taxa_de_crescimento_da_populacao_B

    populacao_pais_A = int(populacao_pais_A)
    populacao_pais_B = int(populacao_pais_B)
    print(f'Foram necessários {conta_anos} anos para que a polução do país A igualasse ou superasse a '
          f'população do país B.')
    print(f'A população final do país A é de {populacao_pais_A}.')
    print(f'A população final do país B é de {populacao_pais_B}.')

# comparacao_populacao_editavel()


#Exercício 6: Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique
# o programa para que ele mostre os números um ao lado do outro.

def exercicio_6():
    for i in range(1,21):
        print(i)

    for k in range(1,21):
        print(k, end = " ")

# exercicio_6()


#Exercício 7: Faça um programa que leia 5 números e informe o maior número.

def maximo():
    maximo = float(input('Digite um número: '))

    for _ in range(4):
        maximo = max(maximo, float(input('Digite um número: ')))
        print(f'O número máximo encontrado é {maximo}.')

#maximo()


#Exercício 8: Faça um programa que leia 5 números e informe a soma e a média dos números.

def exercicio_8():
    numero = float(input('Didiginte um número: '))
    maximo = numero
    for n in range(2, 6):
        numero_adicional = float(input('Digite um número: '))
        maximo = max(maximo, numero_adicional)
        print(f'O número máximo encontrado é {maximo}.')

        numero += numero_adicional
        print(f'A soma total é de {numero}')

        media = numero / (n)
        print(f'A média é {media}')

#exercicio_8()


#Exercício 9: Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

def exercicio_9():
    for i in range(51):
        if i % 2 != 0:
            print(i)

#exercicio_9()


#Exercício 10: Faça um programa que receba dois números inteiros e gere os números inteiros que estão
# no intervalo compreendido por eles.

def exercicio_10():
    numero_1 = int(input('Digite um número inteiro: '))
    numero_2 = int(input('Digite outro número inteiro: '))

    for i in range(numero_1 + 1, numero_2):
        print(i)

#exercicio_10()


#Exercício 11: Altere o programa anterior para mostrar no final a soma dos números.

def exercicio_11():
    numero_1 = int(input('Digite um número inteiro: '))
    numero_2 = int(input('Digite outro número inteiro: '))
    resultado_final = 0
    for i in range(numero_1 + 1, numero_2):
        print(i)
        resultado_final += i
    print(f'A soma dos números é de {resultado_final}')

#exercicio_11()



#Exercício 12:
#Exercício 13:
#Exercício 14:
#Exercício 15:
#Exercício 16:
#Exercício 17:
#Exercício 18:
#Exercício 19:
#Exercício 20:
#Exercício 21:
#Exercício 22:
#Exercício 23:
#Exercício 24:
#Exercício 25:
#Exercício 26:
#Exercício 27:
#Exercício 28:
#Exercício 29:
#Exercício 30:
#Exercício 31:
#Exercício 32:
#Exercício 33:
#Exercício 34:
#Exercício 35:
#Exercício 36:
#Exercício 37:
#Exercício 38:
#Exercício 39:
#Exercício 40:
#Exercício 41:
#Exercício 42:
#Exercício 43:
#Exercício 44:
#Exercício 45:
#Exercício 46:
#Exercício 47:
#Exercício 48:
#Exercício 49:
#Exercício 50:
#Exercício 51:
