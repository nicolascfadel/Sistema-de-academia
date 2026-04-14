from .dados import carregar_dados, salvar_dados, CAMINHO_ARQUIVO
from .treino import cadastro_treino, remover_treino, exibir_treino, buscar_treino, atualizar_treino

dados = carregar_dados(CAMINHO_ARQUIVO)
lista_exercicios = dados["exercicios"]
lista_treinos = dados["treinos"]

def salvar_tudo():
    salvar_dados(CAMINHO_ARQUIVO, {"exercicios": lista_exercicios, "treinos": lista_treinos})



def cadastro_exercicio() -> None:
    print("\n -- Cadastro de Exercício --")

    while True:
        nome = input("Digite o nome do Exercício: ").strip()

        if not nome:
            print("❌ Nome inválido. Digite novamente.")
            continue


        if any(ex["nome"].lower() == nome.lower() for ex in lista_exercicios):
            print("❌ Esse exercício já está cadastrado! Digite outro nome.")
            continue

        break

    while True:
        categoria = input("Digite a categoria do exercício (ex: Peito, Costas, Pernas): ").strip()

        if not categoria:
            print("❌ Categoria inválida. Digite novamente.")
            continue

        if any(char.isdigit() for char in categoria):
            print("❌ A categoria não pode conter números! Digite novamente.")
            continue

        break

    novo_exercicio = {
        "nome": nome,
        "categoria": categoria
    }

    lista_exercicios.append(novo_exercicio)
    salvar_tudo()

    print(f"Exercício '{nome}' cadastrado com sucesso! Categoria: {categoria}")



def buscar_exercicio() -> None:
        termo = input("Digite parte do nome do Exercício: ").strip().lower()
        termo = termo.lower()
        encontrados = [ex for ex in lista_exercicios if termo in ex["nome"].lower()]

        if encontrados:
            print("Exercícios encontrados:")
            for ex in encontrados:
                print(f" - {ex['nome']} ({ex['categoria']})")
        else:
            print("Nenhum exercício encontrado.")



def remover_exercicio() -> None:
    if not lista_exercicios:
        print("Nenhum exercício cadastrado.")
        return

    print("\n=== REMOVER EXERCÍCIO ===")
    for i, ex in enumerate(lista_exercicios, start=1):
        print(f" [{i}] {ex['nome']} ({ex['categoria']})")

    while True:
        opcao = input("Digite o número do exercício que deseja remover: ").strip()

        if not opcao.isdigit():
            print("Digite apenas números!")
            continue

        opcao = int(opcao)

        if opcao < 1 or opcao > len(lista_exercicios):
            print("Número inválido! Tente novamente.")
        else:
            break

    ex_selecionado = lista_exercicios[opcao - 1]

    while True:
        confirmacao = input(
            f"Tem certeza que deseja remover '{ex_selecionado['nome']}'? (s/n): "
        ).strip().lower()


        if confirmacao not in ("s", "n"):
            print("Digite apenas 's' para sim ou 'n' para não.")
            continue

        break

    if confirmacao == 's':
        lista_exercicios.pop(opcao - 1)
        salvar_tudo()
        print(f"Exercício '{ex_selecionado['nome']}' removido com sucesso!")
    else:
        print("Remoção cancelada.")



def atualizar_exercicio() -> None:
    if not lista_exercicios:
        print("Nenhum exercício cadastrado.")
        return

    print("\n=== ATUALIZAR EXERCÍCIO ===")
    for i, ex in enumerate(lista_exercicios, start=1):
        print(f" [{i}] {ex['nome']} ({ex['categoria']})")

    
    while True:
        opcao = input("Digite o número do exercício que deseja atualizar: ").strip()

        if not opcao.isdigit():
            print("Digite apenas números!")
            continue

        opcao = int(opcao)

        if opcao < 1 or opcao > len(lista_exercicios):
            print("Número inválido! Tente novamente.")
        else:
            break

    exercicio = lista_exercicios[opcao - 1]

    print(f"\nExercício selecionado:")
    print(f"Nome atual: {exercicio['nome']}")
    print(f"Categoria atual: {exercicio['categoria']}\n")

    
    novo_nome = input("Digite o novo nome (deixe vazio para manter o atual): ").strip()
    if novo_nome:
        exercicio["nome"] = novo_nome

    
    while True:
        nova_categoria = input("Digite a nova categoria (deixe vazio para manter a atual): ").strip()

        if not nova_categoria:
            break

        
        if any(char.isdigit() for char in nova_categoria):
            print("❌ Categoria inválida! Não pode conter números.")
            continue

        exercicio["categoria"] = nova_categoria
        break

    salvar_tudo()
    print("\nExercício atualizado com sucesso!")
    print(f"Novo nome: {exercicio['nome']}")
    print(f"Nova categoria: {exercicio['categoria']}")

