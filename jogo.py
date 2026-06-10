import desenhos as d
from random import choice
import bd


def jogar():
    lista_palavras = []
    arquivo = open("PROJETO_JOGOFORCA/palavras.txt", "r")
    for linha in arquivo:
        palavra = linha.strip()
        lista_palavras.append(palavra)

    palavra_sorteada = choice(lista_palavras)

    for x in range(50):
        print()

    digitadas = []
    acertos = []
    erros = 0

    nome = input("Quem está jogando? ")

    while True:
        adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)

        # * CONDIÇAO DE VITORIA
        if adivinha == palavra_sorteada:
            print("Voce ganhou! ")
            break

        # * TENTATIVAS
        tentativa = input("Digite uma letra: ").lower().strip()
        if tentativa in digitadas:
            print("Voce ja digitou essa letra! ")
            continue
        else:
            digitadas += tentativa
            if tentativa in palavra_sorteada:
                acertos += tentativa
            else:
                erros += 1
                print("Voce errou! ")

        score = d.desenhar_forca(erros)

        # * CONDIÇAO DE FIM DE JOGO
        if erros == 6:
            print("Enforcado!")
            print(f"A palavra correta era {palavra_sorteada} ")
            break

    bd.inserir_dado(nome, score)
