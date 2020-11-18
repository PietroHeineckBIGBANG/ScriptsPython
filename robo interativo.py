from time import sleep
'\033[32m'
print('=====Robo interativo======')
print(' ')
print('Qual voce quer ir?')
print('Digite uma opçao:')
print(' ')
print('1 = Transformador de graus celsius para graus ºF:')
sleep(0.6)
print('2 = Consulta de tabuada:')
sleep(0.6)
print('3 = Perguntas do robo:')
sleep(0.6)
print('4 = Créditos:')
sleep(0.6)
print('5 = Jogo da adivinhaçao:')
sleep(0.6)
print('6 = Dowload do script')
sleep(0.6)
print('7 = Radar interativo')
sleep(0.6)
print('8 = sorteador')
sleep(0.6)
print('9 = calculadora')
sleep(0.6)
print('10 = Pedra, Papel, Tesoura')
print(' ')
num1 = int(input('Qual irá escolher? ').strip())


if num1 == 1:
    print('CARREGANDO MODULO...')
    sleep(2.3)
    print('MODULO CARREGADO COM SUCESSO!')
    sleep(1.3)
    print(' ')
    temp = float(input('Informe a temperatura em °C: ').strip())
    calc = (temp * 9 / 5 + 32)
    print('A temperatura em {}°C corresponde a {}ºF'.format(temp, calc))
    sleep(50)
    print('50')


elif num1 == 2:
    print('CARREGANDO MODULO...')
    sleep(2.3)
    print('MODULO CARREGADO COM SUCESSO!')
    sleep(1.3)
    print(' ')
    a = int(input('Digite um número para saber a tabuada: ').strip())
    print(' ')
    print('Tabuada do {}'.format(a))
    print('===========')
    print('{} x  1 = {}'.format(a,a))
    print('{} x  2 = {}'.format(a,(a*2)))
    print('{} x  3 = {}'.format(a,(a*3)))
    print('{} x  4 = {}'.format(a,(a*4)))
    print('{} x  5 = {}'.format(a,(a*5)))
    print('{} x  6 = {}'.format(a,(a*6)))
    print('{} x  7 = {}'.format(a,(a*7)))
    print('{} x  8 = {}'.format(a,(a*8)))
    print('{} x  9 = {}'.format(a,(a*9)))
    print('{} x 10 = {}'.format(a,(a*10)))
    print('===========')
    sleep(50)
    print('.....')


elif num1 == 3:
    print('INICIANDO ROBO... POR FAVOR ESPERE UM MOMENTO')
    sleep(2.30)
    print('ROBO CARREGADO COM SUCESSO!')
    sleep(1.20)
    print('(no final eu irei falar todas informaçoes recebidas)')
    print(' ')
    print('Responda:')
    print(' ')
    nome = input('Qual seu primeiro nome?')
    sobNome = input('E o seu sobrenome?')
    print('ANALISANDO SEU NOME...')
    sleep(2)
    print('É um prazer de conheçer {}{} {}{}'.format('\033[2;31m', nome, sobNome, '\033[2;31m'))
    print(' ')
    print('\033[32m''Seu nome ao todo tem \033[2;35m{} \033[32mletras'.format(nome.__len__(), sobNome.__len__()))
    print('\033[32m''Seu nome em maiúsculos é: \033[2;36m{}'.format(nome.upper(), sobNome.upper()))
    print('\033[32m''Seu nome em minúsculos é: \033[2;36m{}'.format(nome.lower(), sobNome.lower()))
    separa = nome.split()
    separa2 = sobNome.split()
    print('\033[32m''Seu primeiro nome é {} e ele tem \033[2;36m{} letras '.format(separa[0], len(separa[0])))
    print('\033[32m'' ')
    sleep(1.30)
    idade = input('\033[32m''Qual sua idade?')
    print('Bom saber! eu tenho 1 dia de vida :D')
    print(' ')
    sleep(1.30)
    print('Quando voce nasceu?')
    sleep(1)
    dia = input('Dia = ')
    mes = input('Mes = ')
    ano = input('Ano = ')
    correct = input('Entao voce nasceu no dia {} de {} de {} correto?'.format(dia, mes, ano))
    if correct == 'sim':
        print('Que bom!')
    else:
        print('Ah, serio?')
    print(' ')
    sleep(1.5)
    hobby = input('o que voce gosta de fazer?')
    print('olha que legal! ja conheço bastante de voce!')
    print(' ')
    sleep(1.5)
    filme = input('Qual seu filme favorito?')
    print('Que bom gosto!')
    print(' ')
    sleep(1.5)
    sim = input('Preparado para eu falar todas as informaçoes recebidas?')
    if sim == 'nao':
        print('ah, esperei que quisesse saber :c')
    else:
        print('PROCESSANDO...')
        sleep(1)
        print('O processo terminará em 3 segundos!')
        sleep(1)
        print('O processo terminará em 2 segundos!')
        sleep(1)
        print('O processo terminará em 1 segundos!')
        sleep(1)
        print(
            '\033[35m''Nome completo:{} {}, Idade:{} anos, Nascimento:{} de {} de {}, Gosta de fazer:{}, Filme Favorito:{}'.format(
                nome,
                sobNome, idade, dia, mes, ano, hobby, filme))
        sleep(50)
        print('....')

elif num1 == 4:
    print(' ')
    print('Creditos ao criador:')
    print('')
    sleep(1.4)
    print('Pietro Heineck')
    print('Iniciante no mundo da programaçao')
    print('Aprendendo Python')
    print('Discord para suporte: BIG BANG#0728 ')
    sleep(50)
    print('.....')


elif num1 == 5:
    from random import randint
    from time import sleep
    print('CARREGANDO MODULO...')
    sleep(2.3)
    print('MODULO CARREGADO COM SUCESSO!')
    sleep(1.3)
    print(' ')
    comp = randint(0, 5)
    print('-=-' * 20)
    print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
    print('-=-' * 20)
    player = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    sleep(1.20)
    if player == comp:
        print('PARABÉNS! Voce conseguiu me vencer!')
        sleep(50)
        print('...')
    else:
        print('GANHEI! Eu pensei no número {} e nao no {}!'.format(comp, player))
        sleep(50)
        print('...')


elif num1 == 6:
    sleep(2)
    print(' ')
    print('Dowload do script (Robo interativo.py)')
    print(' ')
    sleep(1.6)
    print('https://github.com/PietroHeineckBIGBANG/ScriptsPython/blob/main/robo%20interativo.py')
    print('Pietro Heineck:')
    print(' ')
    print('COPIA NAO COMÉDIA')
    sleep(50)
    print('...........')


elif num1 == 7:
    from time import sleep

    valor = float(input('Qual a velocidade maxima do carro(quilometros)? ').strip())
    a = int(input('Qual a velocidade atual do carro(quilometros)? ').strip())

    if a <= valor:
        print('Processando...')
        sleep(1.4)
        print(' ')
        print('O processo terminará em 3')
        sleep(1)
        print(' ')
        print('O processo terminará em 2')
        sleep(1)
        print(' ')
        print('O processo terminará em 1')
        sleep(1)
        print(' ')
        print('Processo concluído com sucesso!')
        sleep(1)
        print(' ')
        print('\034[35m''Tenha um bom dia, dirija com segurança!')
        sleep(50)
        print(' ')
    else:
        print('Processando...')
        sleep(1.4)
        print(' ')
        print('O processo terminará em 3')
        sleep(1)
        print(' ')
        print('O processo terminará em 2')
        sleep(1)
        print(' ')
        print('O processo terminará em 1')
        sleep(1)
        print(' ')
        print('Processo concluído com sucesso!')
        sleep(0.6)
        print(' ')
        multa = (a - valor) * 7
        print('\033[31m''MULTADO!\033[37m Voce ultrapassou o limite de \033[35m{}Km'.format(valor))
        print('Voce deve pagar uma multa de \033[36mR${:.2f}!'.format(multa))
        print('Tenha um bom dia, dirija com segurança!')
        print(' ')
        sleep(50)
        print(' ')

if num1 == 8:
    import random

    n1 = str(input('Primeiro item = '))
    n2 = str(input('Segundo item = '))
    n3 = str(input('Terceiro item = '))
    n4 = str(input('Quarto item = '))
    lista = [n1, n2, n3, n4]
    random.choice(lista)
    print('o resultado foi {}'.format(lista))
    print(lista)
    sleep(50)
    print(' ')


if num1 == 9:
    from time import sleep

    print('CARREGANDO CALCULADORA ESPERE UM MOMENTO...')
    sleep(1.5)
    print('CALCULADORA CARREGADA COM SUCESSO!')
    sleep(0.6)
    print('CALCULADORA Python')
    print(' ')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('use 1 para subtrair')
    print('use 2 para somar')
    print('use 3 para dividir')
    print('use 4 para multiplicar')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    index = int(input('Voce deseja executar que tipo de operaçao? ').strip())
    num1 = int(input('Digite o primeiro número: ').strip())
    num2 = int(input('Digite o segundo número: ').strip())

    if index == 1:
        calc1 = num1 - num2
        print('O resultado da subtraçao é: \033[33m{}'.strip().format(calc1))
    elif index == 2:
        calc2 = num1 + num2
        print('O resultado da soma é: \033[33m{}'.strip().format(calc2))
    elif index == 3:
        calc3 = num1 / num2
        print('O resultado da divisao é: \033[33m{}'.strip().format(calc3))
    elif index == 4:
        calc4 = num1 * num2
        print('O resultado da multiplicaçao é: \033[33m{}'.strip().format(calc4))
        sleep(50)
        print(' ')
    else:
        print('Digite um valor válido por favor!')

if num1 == 10:
    from random import randint
    from time import sleep

    itens = ('Pedra', 'Papel', 'Tesoura')
    comp = randint(0, 2)
    print('CARREGANDO...')
    sleep(2)
    print('CARREGADO COM SUCESSO!')
    sleep(1)
    print('=-' * 11)
    print('PEDRA, PAPEL, TESOURA')
    print('=-' * 11)
    print('''Suas opçoes:
    [ 1 ] PEDRA
    [ 2 ] PEPEL
    [ 3 ] TESOURA''')
    jogador = int(input('Qual é a sua jogada? '))
    print(' ')
    sleep(1)
    print('\033[31m''JO')
    sleep(1)
    print('\033[33m''KEN')
    sleep(1)
    print('\033[34m''PO!!!')
    sleep(1)
    print('\033[36m''-=' * 11)
    print('\033[35m''O computador jogou {}'.format(itens[comp]))
    print('O jogador jogou {}'.format(itens[jogador]))
    print('\033[36m''-=' * 11)
    print(' ')
    if comp == 1:
        if jogador == 1:
            print('\033[31m''Empatou.')
        elif jogador == 2:
            print('\033[31m''Jogador venceu.')
        elif jogador == 3:
            print('\033[31m''Computador venceu.')
        else:
            print('\033[31m''Número inválido.')
            sleep(50)
            print(' ')

    elif comp == 2:

        if jogador == 1:
            print('\033[31m''Computador venceu.')
        elif jogador == 2:
            print('\033[31m''Empatou.')
        elif jogador == 3:
            print('\033[31m''Jogador venceu.')
        else:
            print('\033[31m''Número inválido:')
            sleep(50)
            print(' ')

    elif comp == 3:

        if jogador == 1:
            print('\033[31m''Jogador venceu.')
        elif jogador == 2:
            print('\033[31m''Computador venceu.')
        elif jogador == 3:
            print('\033[31m''Empate.')
        else:
            print('\033[31m''Número inválido:')
            sleep(50)
            print(' ')


else:
    print('Número incorreto, por favor digite um número válido!')