import os
import time
import tecnicasedc
import keyboard
from colorama import Fore, Back, Style, init  # Para destacar as paridades
init()  # Necesário para iniciar o colorama\


# Função para encerrar o programa
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

# Função de mensagem em alguns prints


def mensagem():
    os.system('cls')
    print("Opção inválida. Tente novamente.\n")
    os.system('pause')
    os.system('cls')


# Função para checar se o número é binário
def checkBin(string, msg):
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
        if msg == '0':
            print("Desculpe, mas o valor inserido NÃO é um valor binário.")
        else:
            print(
                f'Por favor, verifique se a mensagem {msg} é um valor binário.')
            print('Digite ESC para voltar ao menu principal.')
            keyboard.wait('esc')
            os.system('cls')
            tecnicasedc.main()
        print('Digite ESC para tentar novamente.')
        keyboard.wait('esc')
        os.system('cls')
        if msg == '0':
            tecnicasedc.envioHamming()
        else:
            tecnicasedc.envioChecksum()


# Envio de mensagens Hamming
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
        # Calcula os bits de paridade
        p.append(x[1] ^ x[2] ^ x[4] ^ x[5] ^ x[7])  # P1
        p.append(x[1] ^ x[3] ^ x[4] ^ x[6] ^ x[7])  # P2
        p.append(x[2] ^ x[3] ^ x[4] ^ x[8])         # P3
        p.append(x[5] ^ x[6] ^ x[7] ^ x[8])         # P4

        # Coloca a mensagem + bits de paridade na mensagem enviada
        mensagemEnviada = [p[1], p[2], x[1], p[3], x[2],
                           x[3], x[4], p[4], x[5], x[6], x[7], x[8]]

        # Transforma a mensagem enviada em um str
        mensagemEnviada = ''.join(str(v) for v in mensagemEnviada)
        return(mensagemEnviada)
    elif TAM == 17:
        # Calcula os bits de paridade
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

        # Coloca a mensagem + bits de paridade na mensagem enviada
        mensagemEnviada = [p[1], p[2], x[1], p[3], x[2],
                           x[3], x[4], p[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], p[5], x[12], x[13], x[14], x[15], x[16], x[17]]

        # Transforma a mensagem enviada em um str
        mensagemEnviada = ''.join(str(v) for v in mensagemEnviada)
        return(mensagemEnviada)
    else:
        print('Ooops...Houve um ERRO!\nPor favor, contate um colaborador informando os dados de entrada.')


# Função de mensagem enviada em alguns locais
def mensagemEnviada():
    os.system('cls')
    print(
        'Mensagem enviada com sucesso!')
    print('Digite ESC para voltar ao menu de Hamming.')
    keyboard.wait('esc')
    os.system('cls')


# Função de visualizar mensagens
def visualizarMensagem(msg, typeMessage, typeEDC, edcEnviado, edcRecebido):
    os.system('cls')
    if(typeEDC == 'Hamming'):
        if len(msg) == 0:
            print(f'Ooops... Parece que você não enviou nenhuma mensagem ainda!')
            print('Digite ESC para voltar ao menu de Hamming.')
            keyboard.wait('esc')
            os.system('cls')
            tecnicasedc.menuHamming('', '')
        # Para colorir para vermelho os bits de paridade, e amarelo os errors
        elif len(msg) == 12:
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
            print(
                'Ooops...Houve um ERRO!\nPor favor, contate um colaborador informando os dados de entrada.')
            print('Digite ESC para voltar ao menu de Hamming.')
    elif(typeEDC == 'Checksum'):
        if len(msg) == 0:
            print(f'Ooops... Parece que você não enviou nenhuma mensagem ainda!')
            print('Digite ESC para voltar ao menu de Checksum.')
            keyboard.wait('esc')
            os.system('cls')
            tecnicasedc.menuChecksum('', '', '', '')
        else:
            if typeMessage == 'Enviada':
                print('Mensagens & EDC Enviados: ')
            elif typeMessage == 'Recebida':
                print('Mensagens & EDC Recebidas: ')
            for i in range(len(msg)):
                print(f'Mensagem {i+1}: {msg[i]}')
            if typeMessage == 'Enviada':
                print(f'EDC       : {edcEnviado}')
            elif typeMessage == 'Recebida':
                print(f'EDC       : {edcRecebido}')

    keyboard.wait('esc')
    os.system('cls')


# Função de checar errors
def checarErros(msgEnviada, msgRecebida, typeMessage, edcEnviado, edcRecebido):
    os.system('cls')
    if typeMessage == 'Hamming':
        if len(msgEnviada) == 0 or len(msgRecebida) == 0:
            os.system('cls')
            print(
                f'Ooops... Parece que você ainda não enviou nenhuma mensagem! Tente novamente!')
            print('Digite ESC para voltar ao menu de Hamming.')
            keyboard.wait('esc')
            os.system('cls')
            tecnicasedc.menuHamming('', '')
        # Uma mensagem de 8 bits através de Hamming, receberá 4 bits de paridade.
        # (12, 8) - 8 + 4 Paridades. A mensagem enviada terá 12 bits ao total
        # Uma mensagem de 17 bits através de Hamming, receberá 5 bits de paridade.
        # (22, 17) - 17 + 5 Paridades. A mensagem enviada terá 22 bits ao total
        # Apenas transforma a mensagem em uma lista
        x = list(msgRecebida)

        # Adiciona um valor em branco na primeira posição. Apenas para trabalharmos igual na tabela.
        x.insert(0, '0')

        # Transformar os valores da lista em INT.
        x = [int(i) for i in x]
        # K = Bits de paridade
        k = []
        # Adiciona um valor em branco na primeira posição. Apenas para trabalharmos igual na tabela.
        k.insert(0, '0')
        if len(msgRecebida) == 12:
            # Locais das paridades
            paridades = [0, 1, 3, 7]
            # P1 P2 X1 P3 X2 X3 X4 P4 X5 X06 X07 X08
            # X1 X2 X3 X4 X5 X6 X7 X8 X9 X10 X11 X12
            k.append(x[1] ^ x[3] ^ x[5] ^ x[7] ^ x[9] ^ x[11])   # K1
            k.append(x[2] ^ x[3] ^ x[6] ^ x[7] ^ x[10] ^ x[11])  # K2
            k.append(x[4] ^ x[5] ^ x[6] ^ x[7] ^ x[12])          # K3
            k.append(x[8] ^ x[9] ^ x[10] ^ x[11] ^ x[12])        # K4

            somaErros = k[1: len(k)]
        elif len(msgRecebida) == 22:
            # Locais das paridades
            paridades = [0, 1, 3, 7, 15]
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
            k.append(x[8] ^ x[9] ^ x[10] ^ x[11] ^
                     x[12] ^ x[13] ^ x[14] ^ x[15])
            # K5
            k.append(x[16] ^ x[17] ^ x[18] ^ x[19] ^ x[20] ^ x[21] ^ x[22])

            somaErros = k[1: len(k)]

        else:
            print(
                'Ooops...Houve um ERRO!\nPor favor, contate um colaborador informando os dados de entrada.')
        if sum(somaErros) == 0:
            print('Sua mensagem foi transmitida com sucesso!')
            print(f'Mensagem: ', end="", flush=True)
            for item in range(len(msgRecebida)):
                if item in paridades:
                    print(Fore.RED + msgRecebida[item], end="", flush=True)
                else:
                    print(Fore.WHITE + msgRecebida[item], end="", flush=True)
            print(Style.RESET_ALL)
        else:

            # Deleta o primeiro elemento de K para fazer as contas... (Que é vazio)
            del k[0]

            # Para calcular a posição do Erro, inverte a lista.
            k.reverse()

            # Concatena os itens em uma única string
            k = ''.join(str(v) for v in k)

            # Transforma o número binário em inteiro
            k = binToDecimal(k)

            print(
                f'Infelizmente sua mensagem foi transmitida com erros, provavelmente na posição {k}')
            print(f'Mensagem: ', end="", flush=True)
            for item in range(len(msgRecebida)):
                if item == k - 1:
                    print(Fore.YELLOW + msgRecebida[item], end="", flush=True)
                elif item in paridades:
                    print(Fore.RED + msgRecebida[item], end="", flush=True)
                else:
                    print(Fore.WHITE + msgRecebida[item], end="", flush=True)
            print(Style.RESET_ALL)

            opcao = int(input(
                "Deseja corrigir automaticamente o erro?\nEscolha uma opção:\n[0] Não\n[1] Sim\n  Resposta: "))
            if opcao == 1:
                print("Parabéns! Sua mensagem foi corrigida!")
                msgRecebidaList = list(msgRecebida)
                if msgRecebidaList[k-1] == '0':
                    msgRecebidaList[k-1] = '1'
                else:
                    msgRecebidaList[k-1] = '0'
                msgRecebida = "".join(msgRecebidaList)
            elif opcao == 0:
                pass
            else:
                print("Oops... Houve um erro, tente novamente!")
                checarErros(msgEnviada, msgRecebida,
                            typeMessage, edcEnviado, edcRecebido)
        print('Digite ESC para voltar ao menu de Hamming.')
        keyboard.wait('esc')
        os.system('cls')
        tecnicasedc.menuHamming(msgEnviada, msgRecebida)
    elif typeMessage == 'Checksum':
        if len(msgEnviada) == 0 or len(msgRecebida) == 0:
            os.system('cls')
            print(
                f'Ooops... Parece que você ainda não enviou nenhuma mensagem! Tente novamente!')
            print('Digite ESC para voltar ao menu de Checksum.')
            keyboard.wait('esc')
            os.system('cls')
            tecnicasedc.menuChecksum('', '', '', '')

        erro = False
        [mensagem1, mensagem2, mensagem3] = msgRecebida
        somaMsgs123 = somaMsgs([mensagem1, mensagem2, mensagem3])
        verifica = []
        vai1 = 0
        overflow = False

        # Somar msg123 com edc
        for i in reversed(range(len(somaMsgs123))):
            if i == 0 and vai1 == 1:
                overflow = True
            if int(somaMsgs123[i]) + int(edcRecebido[i]) + vai1 == 3:
                vai1 = 1
                verifica.insert(0, "1")
            elif int(somaMsgs123[i]) + int(edcRecebido[i]) + vai1 == 2:
                vai1 = 1
                verifica.insert(0, "0")
            elif int(somaMsgs123[i]) + int(edcRecebido[i]) + vai1 == 1:
                vai1 = 0
                verifica.insert(0, "1")
            elif int(somaMsgs123[i]) + int(edcRecebido[i]) + vai1 == 0:
                vai1 = 0
                verifica.insert(0, "0")
        # Se tiver overflow, soma + 1, se não, pula
        if overflow == True:
            somatorio = [0] * (len(str(verifica)) - 1)
            somatorio.append(1)
            for i in reversed(range(len(verifica))):
                if int(verifica[i]) + int(somatorio[i]) + vai1 == 3:
                    vai1 = 1
                    verifica[i] = "1"
                elif int(verifica[i]) + int(somatorio[i]) + vai1 == 2:
                    vai1 = 1
                    verifica[i] = "0"
                elif int(verifica[i]) + int(somatorio[i]) + vai1 == 1:
                    vai1 = 0
                    verifica[i] = "1"
                elif int(verifica[i]) + int(somatorio[i]) + vai1 == 0:
                    vai1 = 0
                    verifica[i] = "0"
            overflow == False

        for i in range(len(verifica)):
            if verifica[i] != '1':
                erro = True
        # Transforma a lista em uma string
        verifica = [str(verifica) for verifica in verifica]
        verifica = "".join(verifica)

        if erro == True:
            print(
                f'Infelizmente sua mensagem veio com erros!\nA soma das mensagens com o EDC deu: {verifica}')
            opcao = input(
                "Deseja receber a mensagem novamente?:\n[0] Sim\n[1] Não\nEscolha: ")
            if opcao == '0':
                # Se tiver erro, apenas coloca os valores de Recebidos igual aos enviados
                msgRecebida = msgEnviada
                edcRecebido = edcEnviado
                print("A mensagem foi enviada novamente!")
        else:
            print(
                f'Sua mensagem foi enviada com sucesso!!!!!\nA soma das mensagens com o EDC deu: {verifica}')
        print('Digite ESC para voltar ao menu de Checksum.')
        keyboard.wait('esc')
        os.system('cls')
        tecnicasedc.menuChecksum(
            msgEnviada, msgRecebida, edcEnviado, edcRecebido)


# Conversão de binário para decimal através de função
def binToDecimal(bin):
    funcao = []
    bin = str(bin)
    x = len(str(bin)) - 1
    for i in range(len(str(bin))):
        funcao.append(int(bin[i]) * 2 ** x)
        x = x - 1
    decimal = sum(funcao)
    return decimal


# Função para alterar a mensagem recebida
def alterarMensagemRecebida(msgEnviada, typeEDC, edcEnviado, edcRecebido):
    os.system('cls')
    if typeEDC == 'Hamming':
        if len(msgEnviada) == 0:
            os.system('cls')
            print(
                f'Ooops... Parece que você ainda não enviou nenhuma mensagem! Tente novamente!')
            print('Digite ESC para voltar ao menu de Hamming.')
            keyboard.wait('esc')
            os.system('cls')
            tecnicasedc.menuHamming('', '')
        TAM = len(msgEnviada)
        if TAM == 22:
            TAM = 17
            PAR = 5
        elif TAM == 12:
            TAM = 8
            PAR = 4
        else:
            print(
                'Ooops...Houve um ERRO!\nPor favor, contate um colaborador informando os dados de entrada.')

        msgRecebida = input("Digite sua nova mensagem recebida: ")

        if len(msgRecebida) != 12 and len(msgRecebida) != 22:
            os.system('cls')
            print(
                f'A mensagem enviada originalmente é de {TAM} bits + {PAR} paridades.\nEntão, por favor, digite uma mensagem de {TAM} bits!')
            print('Digite ESC para voltar ao menu de Hamming.')
            keyboard.wait('esc')
            os.system('cls')
            alterarMensagemRecebida(msgEnviada, 'Hamming', '')
        else:
            os.system('cls')
            tecnicasedc.menuHamming(msgEnviada, msgRecebida)
    elif typeEDC == 'Checksum':
        if len(msgEnviada) == 0:
            os.system('cls')
            print(
                f'Ooops... Parece que você ainda não enviou nenhuma mensagem! Tente novamente!')
            print('Digite ESC para voltar ao menu de Checksum.')
            keyboard.wait('esc')
            os.system('cls')
            tecnicasedc.menuChecksum('', '', '', '')
        [mensagem1, mensagem2, mensagem3] = msgEnviada
        msg = ''

        escolha = input(
            'Escolha uma nova mensagem para alterar:\n[0] Mensagem 1\n[1] Mensagem 2\n[2] Mensagem 3\n[3] EDC\nEscolha: ')

        # Apenas para printar "bonito"
        if escolha == '0':
            msg = 'Mensagem 1'
        elif escolha == '1':
            msg = 'Mensagem 2'
        elif escolha == '2':
            msg = 'Mensagem 3'
        elif escolha == '3':
            msg = 'EDC'
        else:
            print('Ooops... Parece que você digitou uma opção inválida!')
            print('Digite ESC para voltar ao menu de Checksum.')
            keyboard.wait('esc')
            os.system('cls')
            tecnicasedc.menuChecksum(
                msgEnviada, msgEnviada, edcEnviado, edcRecebido)
        novaMensagem = input(f'Digite sua nova {msg}: ')

        # Atribui a nova mensagem digitada pelo usuário
        if escolha == '0':
            mensagem1 = novaMensagem
        elif escolha == '1':
            mensagem2 = novaMensagem
        elif escolha == '2':
            mensagem3 = novaMensagem
        elif escolha == '3':
            edcRecebido = novaMensagem

        # Atribui a msgRecebida as mensagens
        msgRecebida = [mensagem1, mensagem2, mensagem3]
        print('Digite ESC para voltar ao menu de Checksum.')
        keyboard.wait('esc')
        os.system('cls')
        tecnicasedc.menuChecksum(
            msgEnviada, msgRecebida, edcEnviado, edcRecebido)


# Funcao que soma as mensagems 1+2+3 para Checksum
def somaMsgs(msg):
    mensagem1 = list(msg[0])
    mensagem2 = list(msg[1])
    mensagem3 = list(msg[2])
    somaMsgs12 = []
    somaMsgs123 = []
    vai1 = 0
    overflow = False

    # Somar msg1 com msg2
    for i in reversed(range(len(mensagem1))):
        if i == 0 and vai1 == 1:
            overflow = True
        if int(mensagem1[i]) + int(mensagem2[i]) + vai1 == 3:
            vai1 = 1
            somaMsgs12.insert(0, "1")
        elif int(mensagem1[i]) + int(mensagem2[i]) + vai1 == 2:
            vai1 = 1
            somaMsgs12.insert(0, "0")
        elif int(mensagem1[i]) + int(mensagem2[i]) + vai1 == 1:
            vai1 = 0
            somaMsgs12.insert(0, "1")
        elif int(mensagem1[i]) + int(mensagem2[i]) + vai1 == 0:
            vai1 = 0
            somaMsgs12.insert(0, "0")
    # Se tiver overflow, soma + 1, se não, pula
    if overflow == True:
        somatorio = [0] * (len(str(mensagem1)) - 1)
        somatorio.append(1)
        for i in reversed(range(len(somaMsgs12))):
            if int(somaMsgs12[i]) + int(somatorio[i]) + vai1 == 3:
                vai1 = 1
                somaMsgs12[i] = "1"
            elif int(somaMsgs12[i]) + int(somatorio[i]) + vai1 == 2:
                vai1 = 1
                somaMsgs12[i] = "0"
            elif int(somaMsgs12[i]) + int(somatorio[i]) + vai1 == 1:
                vai1 = 0
                somaMsgs12[i] = "1"
            elif int(somaMsgs12[i]) + int(somatorio[i]) + vai1 == 0:
                vai1 = 0
                somaMsgs12[i] = "0"
        overflow == False

    # Somar (msg1 + msg2) + msg3
    for i in reversed(range(len(somaMsgs12))):
        if i == 0 and vai1 == 1:
            overflow = True
        if int(mensagem3[i]) + int(somaMsgs12[i]) + vai1 == 3:
            vai1 = 1
            somaMsgs123.insert(0, "1")
        elif int(mensagem3[i]) + int(somaMsgs12[i]) + vai1 == 2:
            vai1 = 1
            somaMsgs123.insert(0, "0")
        elif int(mensagem3[i]) + int(somaMsgs12[i]) + vai1 == 1:
            vai1 = 0
            somaMsgs123.insert(0, "1")
        elif int(mensagem3[i]) + int(somaMsgs12[i]) + vai1 == 0:
            vai1 = 0
            somaMsgs123.insert(0, "0")

    # Se tiver overflow, soma + 1, se não, pula
    if overflow == True:
        somatorio = [0] * (len(str(somaMsgs123)) - 1)
        somatorio.append(1)
        for i in reversed(range(len(somaMsgs12))):
            if int(somaMsgs123[i]) + int(somatorio[i]) + vai1 == 3:
                vai1 = 1
                somaMsgs123[i] = "1"
            elif int(somaMsgs123[i]) + int(somatorio[i]) + vai1 == 2:
                vai1 = 1
                somaMsgs123[i] = "0"
            elif int(somaMsgs123[i]) + int(somatorio[i]) + vai1 == 1:
                vai1 = 0
                somaMsgs123[i] = "1"
        overflow == False

    return somaMsgs123


# Função para calcular o complemento de 1 (EDC) do checksum
def calculaComplementoDeUm(msg):
    # Faço complemento de 1 do resultado (EDC)
    edc = msg
    for i in range(len(msg)):
        if int(msg[i]) == 0:
            edc[i] = 1
        elif int(msg[i]) == 1:
            edc[i] = 0
    print('Digite ESC para voltar ao menu de Checksum.')
    keyboard.wait('esc')
    os.system('cls')

    return edc
