import desenhos as d
import fileHandler as fH

from random import choice #Sortear um item de uma lista


def jogar():
    lista_palavras = list()
    arquivo = fH.abrirArquivoLeitura('palavras.txt')
    for linha in arquivo:
        palavra = linha.strip()
        lista_palavras.append(palavra)

    palavra_sorteada = choice(lista_palavras)


    for x in range(50):
        print()


    digitadas = []
    acertos = []
    erros = 0

    nome = input('Digite seu nome: ')

    while True:
        adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)

        if adivinha == palavra_sorteada:
            print('Parabéns! Você acertou.')
            break
        #Tentativas
        tentativa = input('\nDigite uma letra: ').lower().strip()
        if len(tentativa)>1:
            print('Digite uma letra por vez')
            continue
        else:
            if tentativa in digitadas:
                print('Você já tentou essa letra!')
                continue
            else:
                digitadas += tentativa #Ou append
                if tentativa in palavra_sorteada:
                    acertos += tentativa
                else:
                    erros += 1
                    print('Você errou')

            score = d.desenhar_forca(erros)
            #Fim de Jogo:
            if erros == 6:
                print('Você perdeu. Enforcado!')
                print(f'A palavra correta era: {palavra_sorteada}.')
                break
    #inserir Score:
    fH.inserir_score('score.txt', nome, score)