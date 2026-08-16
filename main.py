import jogo as j
import fileHandler as fH

def mostrar_menu():
    print('='*30)
    print(' '*7 + 'JOGO DA FORCA')
    print('='*30)
    print('\n1 - JOGAR')
    print('2 - SCORE')
    print('3 - SAIR\n')
    print('='*30)

arquivo = 'score.txt'
if fH.existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('ARQUIVO NÃO EXISTE')
    fH.criaArquivo(arquivo)

while True:
    mostrar_menu()
    try:
        opcao = int(input('Escolha a opção (1|2|3): '))
    except ValueError:
        print('Digite uma opção numérica de 1 a 3 ')
        continue
    match opcao:
        case 1:
            print('Iniciar jogo')
            j.jogar()
        case 2:
            print('Score')
            dados = fH.listarArquivo('score.txt')
            if not dados:
                print('Score Vazio')
            else:
                ranking = []
                for jogador in dados:
                    nome, pontuacao = jogador.strip().split(';')
                    ranking.append([nome, int(pontuacao)])
                ranking.sort(key=lambda jogador: jogador[1], reverse=True)
                i = 1
                for jogador in ranking:
                    print(f'{i} -> {jogador[0]}, pontuação: {jogador[1]}')
                    i += 1
        case 3:
            print('Sair')
            break
        case _:
            print('Opção inválida')