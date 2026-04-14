from .exercicio import (
    cadastro_exercicio, remover_exercicio, lista_exercicios,
    atualizar_exercicio, buscar_exercicio
)
from .treino import (
    cadastro_treino, remover_treino, atualizar_treino,
    buscar_treino, exibir_treino
)
from .exercicio import salvar_tudo, lista_treinos


def linha():
    print("=" * 45)


def titulo(texto):
    linha()
    print(texto.center(45))
    linha()


def menu_exercicio():
    while True:
        titulo("MENU DE EXERCÍCIO")
        print(" 1 | Cadastrar")
        print(" 2 | Remover")
        print(" 3 | Atualizar")
        print(" 4 | Buscar")
        print(" 5 | Listar")
        print(" 6 | Voltar ao Menu Principal")
        linha()

        entrada = input("Escolha uma opção: ").strip()

        if not entrada.isdigit():
            print("❌ Opção inválida! Digite apenas números.")
            continue

        opcao = int(entrada)

        if opcao == 1:
            cadastro_exercicio()
            salvar_tudo()

        elif opcao == 2:
            remover_exercicio()
            salvar_tudo()

        elif opcao == 3:
            atualizar_exercicio()
            salvar_tudo()

        elif opcao == 4:
            buscar_exercicio()

        elif opcao == 5:
            titulo("LISTA DE EXERCÍCIOS")
            if not lista_exercicios:
                print("Nenhum exercício cadastrado.")
            else:
                for ex in lista_exercicios:
                    print(f" - {ex['nome']} ({ex['categoria']})")
            linha()

        elif opcao == 6:
            break

        else:
            print("❌ Opção inválida! Escolha entre 1 e 6.")



def menu_treino():
    while True:
        titulo("MENU DE TREINO")
        print(" 1 | Cadastrar")
        print(" 2 | Remover")
        print(" 3 | Atualizar")
        print(" 4 | Buscar")
        print(" 5 | Listar")
        print(" 6 | Voltar ao Menu Principal")
        linha()

        entrada = input("Escolha uma opção: ").strip()

        if not entrada.isdigit():
            print("❌ Opção inválida! Digite apenas números.")
            continue

        opcao = int(entrada)

        if opcao == 1:
            cadastro_treino(lista_exercicios, lista_treinos)
            salvar_tudo()

        elif opcao == 2:
            remover_treino(lista_treinos)
            salvar_tudo()

        elif opcao == 3:
            atualizar_treino(lista_treinos,lista_exercicios)
            salvar_tudo()

        elif opcao == 4:
            buscar_treino(lista_treinos)

        elif opcao == 5:
            titulo("LISTA DE TREINOS")
            exibir_treino(lista_treinos)
            linha()

        elif opcao == 6:
            break

        else:
            print("❌ Opção inválida! Escolha entre 1 e 6.")



def opcoes():
    while True:
        print("\n-- Seja Bem-Vindo(a) à FitHub!! --\n")
        print("\n=== MENU PRINCIPAL ===")
        print(" [1] Menu de Exercício")
        print(" [2] Menu de Treino")
        print(" [3] Sair")

        entrada = input("Escolha uma opção: ").strip()

        if not entrada.isdigit():
            print("❌ Opção inválida! Digite apenas números.")
            continue

        opcao = int(entrada)

        if opcao == 1:
            menu_exercicio()
        elif opcao == 2:
            menu_treino()
        elif opcao == 3:
            print("Saindo do sistema... até logo!")
            break
        else:
            print("❌ Opção inválida! Escolha entre 1 e 3.")


