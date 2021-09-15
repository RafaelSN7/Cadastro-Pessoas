from interface import *
from arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # opção de listar o conteúdo de um arquivo!
        ler_arquivo(arq)
    elif resposta == 2:
        # opção de cadastrar um nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # opção de sair do sistema
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
