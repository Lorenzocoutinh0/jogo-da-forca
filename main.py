import jogo as j
import bd


def mostrar_menu():
    print("=" * 30)
    print("" * 7 + "JOGO DA FORCA")
    print("=" * 30)
    print("\n1 - JOGAR")
    print("2 - SCORE")
    print("3 - SAIR")
    print("=" * 30)


while True:
    conn = bd.conectar()
    bd.criar_tabela(conn)
    mostrar_menu()

    opcao = int(input("Escolha uma opçao (1/2/3):"))

    if opcao == 1:
        print("Iniciar jogo! ")
        j.jogar()
        input("Digite qualquer tecla para continuar... ")

    elif opcao == 2:
        print("SCORE: ")
        dados = bd.listar_dados()
        if not dados:
            print("Score vazio. ")
        else:
            i = 1
            for jogador in dados:
                print(f'{i} -> {jogador[1]}, Pontuaçao: {jogador[2]}')
                i += 1

        input("Digite qualquer tecla para continuar... ")

    elif opcao == 3:
        print("Saindo do jogo! ")
        break

    else:
        print("Opçao invádlida ")

bd.desconectar(conn)
