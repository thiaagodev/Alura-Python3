import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = pedir_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        if erros == 6:
            enforcou = True

        if '_' not in letras_acertadas:
            acertou = True

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

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


def pedir_chute():
    chute = input('Qual a letra? ')
    return chute.strip().upper()


def marca_chute_correto(chute, letras_acertadas, palavra):
    for index, letra in enumerate(palavra):
        if chute == letra:
            letras_acertadas[index] = letra
    print(letras_acertadas)



def imprime_mensagem_vencedor():
    print('Você ganhou!')


def imprime_mensagem_perdedor():
    print('Você perdeu!')


if __name__ == '__main__':
    jogar()
