# Exercício 1:Classe Bola: Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class CirculoPerfeito:
    def __init__(self):
        self.cor = 'azul'
        self.circunferencia = 4
        self.material = 'papel'

    def mostra_cor(self):
        return self.cor

    def troca_cor(self, cor):
        self.cor = cor

'''circulo_primeiro = CirculoPerfeito()
circulo_segundo = CirculoPerfeito()

circulo_segundo.troca_cor('amarelo')

print(type(circulo_primeiro))
print(circulo_primeiro is circulo_segundo)

print(circulo_primeiro.mostra_cor())
print(circulo_segundo.mostra_cor())'''


# Exercício 2: Classe Quadrado: Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado():
    def __init__(self, lado = 1):
        self.lado = lado

    def set_valor_do_lado(self, lado):
        self.lado = lado

    def get_lado(self):
        return self.lado

    def calculo_area(self):
        return self.lado ** 2

'''quadrado = Quadrado(4)
print(quadrado.lado, quadrado.calculo_area())'''


# Exercício 3:

# Exercício 4:Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
        self.idade += 1

    def envelhece_quantidade_de_anos(self, anos):
        if self.idade < 21:
            taxa_de_crecimento = (21 - self.idade) * 0.5
            self.crescer(taxa_de_crecimento)
        self.idade += anos

    def engordar(self, kg: float):
        self.peso += kg

    def emagrecer(self, kg: float):
        self.peso -= kg

    def crescer(self, cm: float):
        self.altura += cm
'''
gabriel = Pessoa('Gabriel', 2, 12, 80)
for _ in range(22):
    gabriel.envelhecer()
    print(f'Idade de {gabriel.nome} é: {gabriel.idade} anos. E sua altura é {gabriel.altura} cm.')
gabriel = Pessoa('Gabriel', 2, 12, 80) 
gabriel.envelhece_quantidade_de_anos(23)
print(f'Idade de {gabriel.nome} é: {gabriel.idade} anos. E sua altura é {gabriel.altura} cm.')'''


# Exercício 5:
# Exercício 6:
# Exercício 7:
# Exercício 8:
# Exercício 9:

# Exercício 10:Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
# Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# tipoCombustivel.
# valorLitro
# quantidadeCombustivel
# Possua no mínimo esses métodos:
# abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi
# colocada no veículo
# abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago
# pelo cliente.
# alterarValor( ) – altera o valor do litro do combustível.
# alterarCombustivel( ) – altera o tipo do combustível.
# alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class BombaCombustivel:
    def __init__(self, tipo_combustivel: str, valor_litro: float, quantidade_combustivel: float):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastercer_por_valor(self, valor:float):
        litros_abastecidos = valor / self.valor_litro
        self._apresenta_abastecimento_se_possivel(litros_abastecidos, valor)

    def _apresenta_abastecimento_se_possivel(self, litros_abastecidos:float, valor:float):
        if litros_abastecidos > self.quantidade_combustivel:
            print(f'Não é possível abastecer, faltam {litros_abastecidos - self. quantidade_combustivel:.2f} litros.')
            print('Reabasteça a bomba.')
        else:
            self.quantidade_combustivel -= litros_abastecidos
            print(f'Foram abastecidos {litros_abastecidos:.2f} litros a um valor de  R$ {valor:.2f}.')
            print(f'Sobraram na bomba {self.quantidade_combustivel:.2f} litros de {self.tipo_combustivel}.')

    def abastecer_pro_litros(self, litros_abastecidos:float):
        valor = litros_abastecidos * self.valor_litro
        self._apresenta_abastecimento_se_possivel(litros_abastecidos, valor)

    def adicionar_mais_combustivel(self, quantidade:float):
        if quantidade >= 0:
            self.quantidade_combustivel += quantidade
        else:
            print('Malandrinho, você não vai roubar combustivel dessa bomba!')

bomba = BombaCombustivel('Gasolina', 4.59, 100.0)

bomba.abastercer_por_valor(100)

bomba.abastecer_pro_litros(50)

bomba.valor_litro = 5.59
bomba.abastecer_pro_litros(50)

bomba.adicionar_mais_combustivel(100)
bomba.abastecer_pro_litros(50)

bomba.adicionar_mais_combustivel(-100)

# Exercício 11:
# Exercício 12:
# Exercício 13:
# Exercício 14:
# Exercício 15:
# Exercício 16:
# Exercício 17:
