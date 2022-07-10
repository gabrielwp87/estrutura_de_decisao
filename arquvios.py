# Exercício 1: Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
# contendo um relatório dos endereços IP válidos e inválidos.
# O arquivo de entrada possui o seguinte formato:
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256
# O arquivo de saída possui o seguinte formato:
# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4
#
# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5
# 192.168.0.256

def validar(ip:str) -> bool:
    numeros = ip.split('.') #o numeros serão dividos onde há ponto, lembrando esses números são strings

    if len(numeros) != 4: #um número de ip tem que ter 4 conjuntos de números
        return False

    for n in numeros:
        if not (0 <= int(n) <= 255):
            return False
    return True


def exercicio_1():
    ips_validos = []
    ips_invalidos = []
    with open('exercicio_1.txt', 'r') as arquivo:
        for linha in arquivo:
            ip = linha.strip()
            if validar(ip):
                ips_validos.append(ip)
            else:
                ips_invalidos.append(ip)

    with open('exercicio_1_saida.txt', 'w') as arquivo:
        arquivo.writelines('[Endereços válidos:]\n')

        for ip in ips_validos:
            arquivo.writelines(f'{ip}\n')

        arquivo.writelines('\n \n')

        arquivo.writelines('[Endereços inválidos:]\n')

        for ip in ips_invalidos:
            arquivo.writelines(f'{ip}\n')

#exercicio_1()


# Exercício 2: A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor
# de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos
# usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet,
# ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere
# um relatório, chamado "relatório.txt", no seguinte formato:
# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso
#
# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%
#
# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de
# forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá
# ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de
# uso também deverá ser feito através de uma função, que será chamada pelo programa principal.


def transforma_em_megabytes(tamanho_em_bytes: str) -> float:
    return int(tamanho_em_bytes) / (2**10)**2

def porcentagem_memoria(memoria_utilizada, memoria_total):
    memoria_utlizada = float(memoria_utilizada)
    memoria_total = float(memoria_total)
    porcentagem = round((memoria_utlizada / memoria_total) * 100, 2)
    porcentagem_str = str(porcentagem) + '%'
    return porcentagem_str

def exercicio_2():
    lista_de_dados = []
    with open('usuario.txt', 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            usuario = linha[:15]
            tamanho_em_disco = transforma_em_megabytes(linha[16:])
            lista_de_dados.append((usuario, tamanho_em_disco))
    print(lista_de_dados)
    cabecalho = '''ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
'''

    with open('relatório.txt', 'w') as arquivo:
        tamanho_total_consumido = sum([tamanho for _, tamanho in lista_de_dados])
        media = tamanho_total_consumido / len(lista_de_dados)
        arquivo.writelines(cabecalho)
        for indice, dados in enumerate(lista_de_dados, start=1):
            usuario, tamanho_em_disco = dados
            arquivo.writelines(f'{indice:<4} {usuario} {tamanho_em_disco:9.2f} MB         '
                               f'{tamanho_em_disco / tamanho_total_consumido:>6.2%}\n')
        arquivo.writelines('\n')
        arquivo.writelines(f'Espaço total ocupado: {tamanho_total_consumido:.2f} MB\n')
        arquivo.writelines(f'Espaço médio ocupado: {media:.2f} MB')

exercicio_2()
