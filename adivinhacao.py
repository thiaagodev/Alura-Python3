from random import randint


def jogar():
    print('*********************************')
    print('Bem vindo no jogo de Adivinhação!')
    print('*********************************')

    total_tentativas = 0
    numero_secreto = randint(1, 101)
    pontos = 1000

    print('Qual o nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')
    nivel = int(input('Defina o nível: '))

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for i in range(0, total_tentativas + 1):
        print(f'Tentativa {i} de {total_tentativas}')
        print('Digite um número entre 1 e 100.')
        chute = input('Digite o seu número: ')

        if int(chute) < 1 or int(chute) > 100:
            print('Digite um número entre 1 e 100!')
            continue
        print(f'Você digitou {chute}')

        if numero_secreto == int(chute):
            print(f'Você acertou!')
            break
        elif numero_secreto != int(chute):
            pontos -= abs(numero_secreto - int(chute))

        if numero_secreto > int(chute):
            print('Chutou mais baixo!')
        else:
            print('Chutou mais alto!')

        print('----------------------------------')

    print('Fim do jogo!')
    print(f'Você fez um total de {pontos} pontos.')


if __name__ == '__main__':
    jogar()
