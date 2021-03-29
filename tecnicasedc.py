# Authors
# Alexandre Fernandes da Silva e Stephen Michael Apolinário

# Códigos de alunos
# Alexandre - 6444989
# Stephen   - 6444962 -> Escolhido. 9 + 6 + 2 = 17

import os  # Para limpar o terminal.
import keyboard  # Para escutar as teclas pressionadas
import funcoes  # Funcoes para funcionamento correto do script


def main():
    # Menu principal do programa
    print('Bem vindo ao programa de técnicas de EDC\n')
    try:
        opcao = int(input("""Selecione uma opção:
                1 - Código de Hamming
                2 - Checksum
                3 - Créditos
                4 - Sair
       Escolha: """))
        if opcao == 1:
            os.system('cls')
            menuHamming('', '')
        elif opcao == 2:
            os.system('cls')
            menuChecksum('', '', '', '')
        elif opcao == 3:
            os.system('cls')
            print("""Acadêmicos:
            1 - Alexandre Fernandes da Silva
            2 - Stephen Michael Apolinário
            Para voltar ao menu, pressione ESC!
            """)
            keyboard.wait('esc')
            os.system('cls')
            main()
        elif opcao == 4:
            funcoes.sair()
        else:
            funcoes.mensagem()
            main()
    except ValueError:
        funcoes.mensagem()
        main()


# Menu princiapl de Hamming
def menuHamming(msgEnviada, msgRecebida):
    print('Bem vindo ao menu Hamming\n')
    try:
        opcao = int(input("""Selecione uma opção:
                1 - Enviar mensagem de Hamming - (12, 8) ou (22, 17) 
                2 - Visualizar mensagem enviada
                3 - Visualizar mensagem recebida
                4 - Checar erros
                5 - Alterar mensagem recebida (Simulação de troca de bit)
                6 - Voltar ao menu principal
       Escolha: """))
        if opcao == 1:
            os.system('cls')
            envioHamming()
        elif opcao == 2:
            funcoes.visualizarMensagem(
                msgEnviada, 'Enviada', 'Hamming', '', '')
            menuHamming(msgEnviada, msgRecebida)
        elif opcao == 3:
            funcoes.visualizarMensagem(
                msgRecebida, 'Recebida', 'Hamming', '', '')
            menuHamming(msgEnviada, msgRecebida)
        elif opcao == 4:
            funcoes.checarErros(msgEnviada, msgRecebida, 'Hamming', '', '')
            menuHamming(msgEnviada, msgRecebida)
        elif opcao == 5:
            funcoes.alterarMensagemRecebida(msgEnviada, 'Hamming', '', '')
            menuHamming(msgEnviada, msgRecebida)
        elif opcao == 6:
            os.system('cls')
            main()
        else:
            funcoes.mensagem()
            main()
    except ValueError:
        funcoes.mensagem()
        menuHamming('', '')


# Envio de mensagem através de Hamming
def envioHamming():
    print('Bem vindo ao transmissor de mensagem Hamming\n')
    mensagem = str(
        input("Digite a mensagem a ser transmitida\nMensagem: "))
    funcoes.checkBin(mensagem, '0')
    if len(mensagem) == 8:
        msgEnviada = funcoes.enviaMensagem(mensagem, 8)
        funcoes.mensagemEnviada()
        menuHamming(msgEnviada, msgEnviada)
    elif len(mensagem) == 17:
        msgEnviada = funcoes.enviaMensagem(mensagem, 17)
        funcoes.mensagemEnviada()
        menuHamming(msgEnviada, msgEnviada)
    else:
        os.system('cls')
        print(
            'Desculpe-me, mas suporto apenas mensagens de 8 e 17 bits.')
        print('Digite ESC para tentar novamente.')
        keyboard.wait('esc')
        os.system('cls')
        envioHamming()


# Menu principal de Checksum
def menuChecksum(msgEnviadas, msgRecebidas, edcEnviado, edcRecebido):
    print('Bem vindo ao menu Checksum\n')
    try:
        opcao = int(input("""Selecione uma opção:
                1 - Enviar mensagens Checksum
                2 - Visualizar mensagens enviadas
                3 - Visualizar mensagens recebidas
                4 - Checar erros
                5 - Alterar mensagem recebida (Simulação de troca de bit)
                6 - Voltar ao menu principal
       Escolha: """))
        if opcao == 1:
            os.system('cls')
            digitarMensagemChecksum(msgEnviadas, msgRecebidas)
        elif opcao == 2:
            funcoes.visualizarMensagem(
                msgEnviadas, 'Enviada', 'Checksum', edcEnviado, edcRecebido)
            menuChecksum(msgEnviadas, msgRecebidas, edcEnviado, edcRecebido)
        elif opcao == 3:
            funcoes.visualizarMensagem(
                msgRecebidas, 'Recebida', 'Checksum', edcEnviado, edcRecebido)
            menuChecksum(msgEnviadas, msgRecebidas, edcEnviado, edcRecebido)
        elif opcao == 4:
            funcoes.checarErros(msgEnviadas, msgRecebidas,
                                'Checksum', edcEnviado, edcRecebido)
            menuChecksum(msgEnviadas, msgRecebidas, edcEnviado, edcRecebido)
        elif opcao == 5:
            funcoes.alterarMensagemRecebida(
                msgEnviadas, 'Checksum', edcEnviado, edcRecebido)
            menuChecksum(msgEnviadas, msgRecebidas, edcEnviado, edcRecebido)
        elif opcao == 6:
            os.system('cls')
            main()
        else:
            funcoes.mensagem()
            menuChecksum(msgEnviadas, msgRecebidas, edcEnviado, edcRecebido)
    except ValueError:
        funcoes.mensagem()
        menuChecksum(msgEnviadas, msgRecebidas, edcEnviado, edcRecebido)


# Envio de mensagens com Checksum
def digitarMensagemChecksum(msgEnviadas, msgRecebidas):
    print('Bem vindo ao transmissor de mensagem com Checksum\n')
    print("Digite as mensagens a serem transmitidas:\n")
    mensagem1 = str(input("Mensagem 01: "))
    mensagem2 = str(input("Mensagem 02: "))
    mensagem3 = str(input("Mensagem 03: "))
    funcoes.checkBin(mensagem1, '1')
    funcoes.checkBin(mensagem2, '2')
    funcoes.checkBin(mensagem3, '3')
    if len(mensagem1) != len(mensagem2) or len(mensagem1) != len(mensagem3) or len(mensagem2) != len(mensagem3):
        os.system('cls')
        print("Infelizmente, suas mensagens são de tamanhos diferentes! Utilize mensagens de mesmo tamanho!")
        print('Digite ESC para tentar novamente.')
        keyboard.wait('esc')
        os.system('cls')
        digitarMensagemChecksum(msgEnviadas, msgRecebidas)
    os.system('cls')
    print('Mensagem enviada com sucesso!')
    somaMsgs123 = funcoes.somaMsgs([mensagem1, mensagem2, mensagem3])
    edcEnviado = funcoes.calculaComplementoDeUm(somaMsgs123)
    edcEnviado = ''.join(str(v) for v in edcEnviado)
    print(edcEnviado)
    msgEnviadas = [mensagem1, mensagem2, mensagem3]
    msgRecebidas = msgEnviadas
    menuChecksum(msgEnviadas, msgRecebidas, edcEnviado, edcEnviado)


# Para o programa ir direto para a funcão Main()
if __name__ == "__main__":
    os.system('cls')
    main()
