import os
import time
import tecnicasedc
import keyboard
from colorama import Fore, Back, Style, init  # Para destacar as paridades
init()  # Necesário para iniciar o colorama\


def sair():
    os.system('cls')
    print("Terminando", end='', flush=True)
    time.sleep(0.5)
    print(".", end='', flush=True)
    time.sleep(0.5)
    print(".", end='', flush=True)
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    os.system('cls')
    exit()


def mensagem():
    os.system('cls')
    print("Opção inválida. Tente novamente.\n")
    os.system('pause')
    os.system('cls')


def checkBin(string):

    # Transforma a string em Set
    p = set(string)

    # Declara um set de 0 e 1
    s = {'0', '1'}

    # Verifica se a string é igual ao S.
    # Ou verifica se a string possui apenas 0
    # Ou verifica se a string possui apenas 1
    if s == p or p == {'0'} or p == {'1'}:
        pass
    else:
        os.system('cls')
        print("Desculpe, mas o valor inserido NÃO é um valor binário.")
        print('Digite ESC para tentar novamente.')
        keyboard.wait('esc')
        os.system('cls')
        tecnicasedc.envioHamming()


def enviaMensagem(mensagem, TAM):
    # Uma mensagem de 8 bits através de Hamming, receberá 4 bits de paridade.
    # (12, 8) - 8 + 4 Paridades. A mensagem enviada terá 12 bits ao total
    # Uma mensagem de 17 bits através de Hamming, receberá 5 bits de paridade.
    # (22, 17) - 17 + 5 Paridades. A mensagem enviada terá 22 bits ao total
    x = list(mensagem)

    # Adiciona um valor em branco na primeira posição. Apenas para trabalharmos igual na tabela.
    x.insert(0, '0')

    # Transformar os valores da lista em INT.
    x = [int(i) for i in x]
    p = []
    # Adiciona um valor em branco na primeira posição. Apenas para trabalharmos igual na tabela.
    p.insert(0, '0')
    if TAM == 8:
        p.append(x[1] ^ x[2] ^ x[4] ^ x[5] ^ x[7])  # P1
        p.append(x[1] ^ x[3] ^ x[4] ^ x[6] ^ x[7])  # P2
        p.append(x[2] ^ x[3] ^ x[4] ^ x[8])         # P3
        p.append(x[5] ^ x[6] ^ x[7] ^ x[8])         # P4

        mensagemEnviada = [p[1], p[2], x[1], p[3], x[2],
                           x[3], x[4], p[4], x[5], x[6], x[7], x[8]]

        mensagemEnviada = ''.join(str(v) for v in mensagemEnviada)
        return(mensagemEnviada)
    elif TAM == 17:
        # P1
        p.append(x[1] ^ x[2] ^ x[4] ^ x[5] ^ x[7] ^
                 x[9] ^ x[11] ^ x[12] ^ x[14] ^ x[16])
        # P2
        p.append(x[1] ^ x[3] ^ x[4] ^ x[6] ^ x[7] ^ x[10] ^
                 x[11] ^ x[13] ^ x[14] ^ x[16] ^ x[17])
        # P3
        p.append(x[2] ^ x[3] ^ x[4] ^ x[8] ^ x[9] ^
                 x[10] ^ x[11] ^ x[15] ^ x[16] ^ x[17])
        # P4
        p.append(x[5] ^ x[6] ^ x[7] ^ x[8] ^ x[9] ^ x[10] ^ x[11])
        # P5
        p.append(x[12] ^ x[13] ^ x[14] ^ x[15] ^ x[16] ^ x[17])

        mensagemEnviada = [p[1], p[2], x[1], p[3], x[2],
                           x[3], x[4], p[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], p[5], x[12], x[13], x[14], x[15], x[16], x[17]]

        mensagemEnviada = ''.join(str(v) for v in mensagemEnviada)
        return(mensagemEnviada)
    else:
        print('Ooops...Houve um ERRO!\nPor favor, contate um colaborador informando os dados de entrada.')


def mensagemEnviada():
    os.system('cls')
    print(
        'Mensagem enviada com sucesso!')
    print('Digite ESC para voltar ao menu de Hamming.')
    keyboard.wait('esc')
    os.system('cls')


def visualizarMensagem(msg, typeMessage):
    os.system('cls')
    if len(msg) == 12:
        print(f'Mensagem {typeMessage}: ', end="", flush=True)
        print(Fore.RED + msg[0:2], end="", flush=True)
        print(Fore.WHITE + msg[2], end="", flush=True)
        print(Fore.RED + msg[3], end="", flush=True)
        print(Fore.WHITE + msg[4:7], end="", flush=True)
        print(Fore.RED + msg[7], end="", flush=True)
        print(Fore.WHITE + msg[8:12], end="", flush=True)
        print(Style.RESET_ALL)
    elif len(msg) == 22:
        print(f'Mensagem {typeMessage}: ', end="", flush=True)
        print(Fore.RED + msg[0:2], end="", flush=True)
        print(Fore.WHITE + msg[2], end="", flush=True)
        print(Fore.RED + msg[3], end="", flush=True)
        print(Fore.WHITE + msg[4:7], end="", flush=True)
        print(Fore.RED + msg[7], end="", flush=True)
        print(Fore.WHITE + msg[8:15], end="", flush=True)
        print(Fore.RED + msg[15], end="", flush=True)
        print(Fore.WHITE + msg[16:23], end="", flush=True)
        print(Style.RESET_ALL)
    else:
        print('Ooops...Houve um ERRO!\nPor favor, contate um colaborador informando os dados de entrada.')
    print('Digite ESC para voltar ao menu de Hamming.')
    keyboard.wait('esc')
    os.system('cls')


def checarErros(msg):
    os.system('cls')
    # Uma mensagem de 8 bits através de Hamming, receberá 4 bits de paridade.
    # (12, 8) - 8 + 4 Paridades. A mensagem enviada terá 12 bits ao total
    # Uma mensagem de 17 bits através de Hamming, receberá 5 bits de paridade.
    # (22, 17) - 17 + 5 Paridades. A mensagem enviada terá 22 bits ao total
    x = list(msg)

    # Adiciona um valor em branco na primeira posição. Apenas para trabalharmos igual na tabela.
    x.insert(0, '0')

    # Transformar os valores da lista em INT.
    x = [int(i) for i in x]
    k = []
    # Adiciona um valor em branco na primeira posição. Apenas para trabalharmos igual na tabela.
    k.insert(0, '0')
    if len(msg) == 12:
        # P1 P2 X1 P3 X2 X3 X4 P4 X5 X06 X07 X08
        # X1 X2 X3 X4 X5 X6 X7 X8 X9 X10 X11 X12
        k.append(x[1] ^ x[3] ^ x[5] ^ x[7] ^ x[9] ^ x[11])   # K1
        k.append(x[2] ^ x[3] ^ x[6] ^ x[7] ^ x[10] ^ x[11])  # K2
        k.append(x[4] ^ x[5] ^ x[6] ^ x[7] ^ x[12])          # K3
        k.append(x[8] ^ x[9] ^ x[10] ^ x[11] ^ x[12])        # K4

        somaErros = k[1: len(k)]
    elif len(msg) == 22:
        # P1 P2 X1 P3 X2 X3 X4 P4 X5 X06 X07 X08 X09 X10 X11 P05 X12 X13 X14 X15 X16 X17
        # X1 X2 X3 X4 X5 X6 X7 X8 X9 X10 X11 X12 X13 X14 X15 X16 X17 X18 X19 X20 X21 X22
        # K1
        k.append(x[1] ^ x[3] ^ x[5] ^ x[7] ^ x[9] ^ x[11] ^
                 x[13] ^ x[15] ^ x[17] ^ x[19] ^ x[21])
        # K2
        k.append(x[2] ^ x[3] ^ x[6] ^ x[7] ^ x[10] ^ x[11] ^ x[14] ^
                 x[15] ^ x[18] ^ x[19] ^ x[21] ^ x[22])
        # K3
        k.append(x[4] ^ x[5] ^ x[6] ^ x[7] ^ x[12] ^ x[13] ^
                 x[14] ^ x[15] ^ x[20] ^ x[21] ^ x[22])
        # K4
        k.append(x[8] ^ x[9] ^ x[10] ^ x[11] ^ x[12] ^ x[13] ^ x[14] ^ x[15])
        # K5
        k.append(x[16] ^ x[17] ^ x[18] ^ x[19] ^ x[20] ^ x[21] ^ x[22])

        somaErros = k[1: len(k)]

    else:
        print('Ooops...Houve um ERRO!\nPor favor, contate um colaborador informando os dados de entrada.')
    if sum(somaErros) == 0:
        print('Sua mensagem foi transmitida com sucesso!')
    else:

        # Deleta o primeiro elemento de K para fazer as contas... (Que é vazio)
        del k[0]

        # Para calcular a posição do Erro, inverte a lista.
        k.reverse()

        # Concatena os itens em uma única string
        k = ''.join(str(v) for v in k)

        # Transforma o número binário em inteiro
        k = int(k, 2)

        print(
            f'Infelizmente sua mensagem foi transmitida com erros, provavelmente na posição {k}')
        # 111101001110
        # 111101001
        #          1
        #           10

    if len(msg) == 12:
        paridades = [0, 1, 3, 7]

    elif len(msg) == 22:
        paridades = [0, 1, 3, 7, 15]

    print(f'Mensagem: ', end="", flush=True)

    for item in range(len(msg)):
        if item == k - 1:
            print(Fore.YELLOW + msg[item], end="", flush=True)
        elif item in paridades:
            print(Fore.RED + msg[item], end="", flush=True)
        else:
            print(Fore.WHITE + msg[item], end="", flush=True)
    print(Style.RESET_ALL)

    print('Digite ESC para voltar ao menu de Hamming.')
    keyboard.wait('esc')
    os.system('cls')


def alterarMensagemRecebida(msgEnviada):
    os.system('cls')
    TAM = len(msgEnviada)
    if TAM == 22:
        TAM = 17
        PAR = 5
    elif TAM == 12:
        TAM = 8
        PAR = 4
    else:
        print('Ooops...Houve um ERRO!\nPor favor, contate um colaborador informando os dados de entrada.')

    msgRecebida = input("Digite sua nova mensagem recebida: ")

    if len(msgRecebida) != 12 and len(msgRecebida) != 22:
        os.system('cls')
        print(
            f'A mensagem enviada originalmente é de {TAM} bits + {PAR} paridades.\nEntão, por favor, digite uma mensagem de {TAM} bits!')
        print('Digite ESC para voltar ao menu de Hamming.')
        keyboard.wait('esc')
        os.system('cls')
        alterarMensagemRecebida(msgEnviada)
    # if len(msg) == 12:
    #     # P1 P2 X1 P3 X2 X3 X4 P4 X5 X06 X07 X08
    #     # X1 X2 X3 X4 X5 X6 X7 X8 X9 X10 X11 X12
    #     print('Em dev')
    # elif len(msg) == 22:
    #     # P1 P2 X1 P3 X2 X3 X4 P4 X5 X06 X07 X08 X09 X10 X11 P05 X12 X13 X14 X15 X16 X17
    #     # X1 X2 X3 X4 X5 X6 X7 X8 X9 X10 X11 X12 X13 X14 X15 X16 X17 X18 X19 X20 X21 X22
    #     print('Em dev')
    else:
        os.system('cls')
        tecnicasedc.menuHamming(msgEnviada, msgRecebida)
