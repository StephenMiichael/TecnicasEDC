# Authors
# Alexandre Fernandes da Silva e Stephen Michael Apolinário

# Códigos de alunos
# Alexandre - 6444989
# Stephen   - 6444962 -> Escolhido. 9 + 6 + 2 = 17

import os  # Para limpar o terminal.
import keyboard  # Para escutar as teclas pressionadas
import funcoes  # Implementação do algoritmo de dijkstra


def main():
    print('Bem vindo ao script técnicas de EDC\n')
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
            print(
                'Desculpe, mas essa função ainda está em desenvolvimento!\nPara voltar ao menu, pressione ESC!')
            keyboard.wait('esc')
            os.system('cls')
            main()
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


def menuHamming(msgEnviada, msgRecebida):
    print('Bem vindo ao menu Hamming\n')
    try:
        opcao = int(input("""Selecione uma opção:
                1 - Enviar mensagem de Hamming - (12, 8) ou (22, 17)
                2 - Visualizar mensagem enviada
                3 - Visualizar mensagem recebida
                4 - Checar erros
                5 - Alterar mensagem recebida (Simualção de troca de bit)
                6 - Voltar ao menu principal
       Escolha: """))
        if opcao == 1:
            os.system('cls')
            envioHamming()
        elif opcao == 2:
            funcoes.visualizarMensagem(msgEnviada, 'Enviada')
            menuHamming(msgEnviada, msgRecebida)
        elif opcao == 3:
            funcoes.visualizarMensagem(msgRecebida, 'Recebida')
            menuHamming(msgEnviada, msgRecebida)
        elif opcao == 4:
            funcoes.checarErros(msgRecebida)
            menuHamming(msgEnviada, msgRecebida)
        elif opcao == 5:
            funcoes.alterarMensagemRecebida(msgEnviada)
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


def envioHamming():
    print('Bem vindo ao transmissor de mensagem Hamming\n')
    mensagem = str(
        input("Digite a mensagem a ser transmitida\nMensagem: "))
    funcoes.checkBin(mensagem)
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
            'Desculpe-me, mas suporto apenas mensagens de 8 e 12 bits.')
        print('Digite ESC para tentar novamente.')
        keyboard.wait('esc')
        os.system('cls')
        envioHamming()


if __name__ == "__main__":
    os.system('cls')
    main()
