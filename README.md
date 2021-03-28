# Técnicas de EDC
Este script tem como finalidade resolver a atividade proposta para nota da M1 de comunicação digital - Univali Itajaí.

## Execução

Para rodar o script, basta abrir um terminal no diretório do script, e execute py -m pip install -r requirements.txt / pip install -r requirements.txt para instalar as importações.
Após isso, basta executar py tecnicasedc.py para começar o script

## Funcionalidades

A aplicação permite realizar Código Hamming para uma mensagem que contenha uma quantidade de bits igual a soma dos três últimos números do seu código de aluno(962) e também o Hamming(12,8).

A permite usar palavras de dados quaisquer e que possuam os tamanhos acima. Além disso, o código permite escolher qual versão utilizar. Também foi implementando o detector e corretor de erroes também o simulador de injeção de erro.

O algoritmo também faz Checksum para blocos de 3 palavras com uma quantidade de bits iguais a soma dos três últimos dígitos do seu Código de Aluno (962). E por meio de uma função é simulado a inversão de um bit de transmissão entre dois meios de comunicação em uma das palavras.
