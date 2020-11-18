from time import sleep
print(' ''\033[32m')
print('=====Robo interativo======')
print(' ')
print('Qual voce quer ir?')
print('Digite uma opiçao:')
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
print(' ')
num1 = int(input('Qual irá escolher? '))


if num1 == 1:
    temp = float(input('Informe a temperatura em °C: '))
    calc = (temp * 9 / 5 + 32)
    print('A temperatura em {}°C corresponde a {}ºF'.format(temp, calc))


if num1 == 2:
    print(' ')
    a = int(input('Digite um número para saber a tabuada: '))
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


if num1 == 3:
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


if num1 == 4:
    print('Creditos ao criador:')
    print('')
    sleep(1.4)
    print('Pietro Heineck')
    print('Iniciante no mundo da programaçao')
    print('Aprendendo Python')


if num1 == 5:
    from random import randint
    from time import sleep

    comp = randint(0, 5)
    print('-=-' * 20)
    print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
    print('-=-' * 20)
    player = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    sleep(1.20)
    if player == comp:
        print('PARABÉNS! Voce conseguiu me vencer!')
    else:
        print('GANHEI! Eu pensei no número {} e nao no {}!'.format(comp, player))
