import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    """for letra in palavra_secreta:
        letras_acertadas.append('_')"""

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input('Qual a letra? ')
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            for index, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_acertadas[index] = letra
            print(letras_acertadas)
        else:
            erros += 1

        if erros == 6:
            enforcou = True

        if '_' not in letras_acertadas:
            acertou = True

    print('Fim do jogo!')

def imprime_mensagem_abertura():
    print('*********************************')
    print('***Bem vindo no jogo de Forca!***')
    print('*********************************')


def carregar_palavra_secreta():
    palavras = []
    with open('palavras.txt', 'r') as arquivo:
        """ O comando 'with' serve parar garantir que caso dê erro o arquivo será fechado """
        for linha in arquivo:
            palavras.append(linha.strip().upper())

    return random.choice(palavras)


def inicializa_letras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]


if __name__ == '__main__':
    jogar()
