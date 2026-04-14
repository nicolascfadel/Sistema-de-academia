from .dados import salvar_dados, CAMINHO_ARQUIVO



def salvar_treinos(lista_treinos, lista_exercicios):
    salvar_dados(CAMINHO_ARQUIVO, {"exercicios": lista_exercicios, "treinos": lista_treinos})


def cadastro_treino(lista_exercicios, lista_treinos) -> None:
    print("\n-- Cadastro de Treino --")
    
    while True:
        nome_treino = input("Digite o nome do treino: ").strip()
        if not nome_treino:
            print("❌ Nome inválido! Digite novamente.")
            continue
        if any(t["nome"].lower() == nome_treino.lower() for t in lista_treinos):
            print("❌ Treino já existe! Digite outro nome.")
            continue
        break

    exercicios_treino = []
    while True:
        filtrar = input("\nDeseja filtrar exercícios por categoria? (s/n): ").strip().lower()
        if filtrar not in ("s", "n"):
            print("❌ Resposta inválida! Digite 's' ou 'n'.")
            continue

        if filtrar == "s":
            categorias = list(set(ex["categoria"] for ex in lista_exercicios))
            print("\nCategorias disponíveis:")
            for i, cat in enumerate(categorias, start=1):
                print(f"[{i}] {cat}")
            escolha_cat = input("Escolha uma categoria pelo número: ").strip()
            if not escolha_cat.isdigit() or int(escolha_cat) not in range(1, len(categorias) + 1):
                print("❌ Opção inválida! Mostrando todos os exercícios.")
                exercicios_filtrados = lista_exercicios
            else:
                categoria_selecionada = categorias[int(escolha_cat) - 1]
                exercicios_filtrados = [ex for ex in lista_exercicios if ex["categoria"] == categoria_selecionada]
        else:
            exercicios_filtrados = lista_exercicios

        if not exercicios_filtrados:
            print("❌ Nenhum exercício encontrado nessa categoria.")
            continue

        print("\nExercícios disponíveis:")
        for i, ex in enumerate(exercicios_filtrados, start=1):
            print(f"[{i}] {ex['nome']} ({ex['categoria']})")

        escolha = input("Digite o número do exercício (ou '0' para finalizar): ").strip()
        if escolha == "0":
            break

        if not escolha.isdigit() or int(escolha) not in range(1, len(exercicios_filtrados) + 1):
            print("❌ Opção inválida!")
            continue

        ex_selecionado = exercicios_filtrados[int(escolha) - 1]

        if any(ex["nome"].lower() == ex_selecionado["nome"].lower() for ex in exercicios_treino):
            print("⚠️ Exercício já adicionado!")
            continue

        while True:
            try:
                num_series = int(input(f"Quantas séries para '{ex_selecionado['nome']}'? "))
                if num_series < 1:
                    print("❌ Número de séries deve ser maior que 0!")
                    continue
                break
            except ValueError:
                print("❌ Número inválido!")

        repeticoes_series = []
        for s in range(1, num_series + 1):
            while True:
                try:
                    rep = int(input(f"Número de repetições para a série {s}: "))
                    if rep < 1:
                        print("❌ Número de repetições deve ser maior que 0!")
                        continue
                    repeticoes_series.append(rep)
                    break
                except ValueError:
                    print("❌ Número inválido!")

        exercicios_treino.append({"nome": ex_selecionado["nome"], "series": repeticoes_series})

    lista_treinos.append({"nome": nome_treino, "exercicios": exercicios_treino})
    salvar_treinos(lista_treinos, lista_exercicios)
    print(f"✅ Treino '{nome_treino}' cadastrado com sucesso!")




def exibir_treino(lista_treinos):
    if not lista_treinos:
        print("❌ Nenhum treino cadastrado.")
        return

    for treino in lista_treinos:
        print(f"\n🏋️‍♂️ {treino['nome'].upper()}")
        print("-" * 40)
        for ex in treino["exercicios"]:
            series_formatadas = ", ".join(str(rep) for rep in ex["series"])
            print(f"• {ex['nome']}: {series_formatadas} repetições")
        print("-" * 40)


def remover_treino(lista_treinos) -> None:
    if not lista_treinos:
        print("🚫 Nenhum treino cadastrado.")
        return

    print("\n=== REMOVER TREINO ===")
    for i, treino in enumerate(lista_treinos, start=1):
        print(f" [{i}] {treino['nome']}")

    while True:
        opcao = input("Digite o número do treino que deseja remover: ").strip()

        if not opcao.isdigit():
            print("❌ Digite apenas números!")
            continue

        opcao = int(opcao)

        if opcao < 1 or opcao > len(lista_treinos):
            print("❌ Número inválido! Tente novamente.")
        else:
            break

    treino_selecionado = lista_treinos[opcao - 1]

    while True:
        confirmacao = input(
            f"Tem certeza que deseja remover '{treino_selecionado['nome']}'? (s/n): "
        ).strip().lower()
        if confirmacao not in ('s', 'n'):
            print("❌ Opção inválida! Digite 's' para sim ou 'n' para não.")
            continue
        break

    if confirmacao == 's':
        lista_treinos.pop(opcao - 1)
        print(f"✅ Treino '{treino_selecionado['nome']}' removido com sucesso!")
    else:
        print("❌ Remoção cancelada.")

def buscar_treino(lista_treinos) -> None:
    if not lista_treinos:
        print("❌ Nenhum treino cadastrado!")
        return

    
    termo = input("Digite o nome ou parte dele: ").strip().lower()

    encontrados = []
    
    encontrados = [t for t in lista_treinos if termo in t["nome"].lower()]

    if encontrados:
        print("\nTreinos encontrados:")
        for t in encontrados:
            exibir_treino([t])
    else:
        print("❌ Nenhum treino encontrado.")


def atualizar_treino(lista_treinos,lista_exercicios) -> None:
    if not lista_treinos:
        print("❌ Nenhum treino cadastrado!")
        return

    print("\nTreinos disponíveis:")
    for i, t in enumerate(lista_treinos, start=1):
        print(f"[{i}] {t['nome']}")

    while True:
        entrada = input("Digite o número do treino para editar: ").strip()
        if not entrada.isdigit():
            print("❌ Digite apenas números!")
            continue
        indice = int(entrada) - 1
        if indice < 0 or indice >= len(lista_treinos):
            print("❌ Opção inválida!")
            continue
        treino = lista_treinos[indice]
        break

    print(f"\nEditando treino: {treino['nome']}")
    print("[1] Renomear treino")
    print("[2] Adicionar exercício")
    print("[3] Editar séries de exercício")
    print("[4] Remover exercício")

    while True:
        entrada = input("Escolha: ").strip()
        if not entrada.isdigit():
            print("❌ Digite apenas números!")
            continue
        opcao = int(entrada)
        if opcao not in [1, 2, 3, 4]:
            print("❌ Opção inválida!")
            continue
        break

    if opcao == 1:
        novo_nome = input("Novo nome: ").strip()
        if novo_nome:
            treino["nome"] = novo_nome
        else:
            print("❌ Nome inválido!")

    elif opcao == 2:
        if not lista_exercicios:
            print("❌ Nenhum exercício cadastrado no sistema!")
            return

        print("\nExercícios disponíveis:")
        for i, ex in enumerate(lista_exercicios, start=1):
            print(f"[{i}] {ex['nome']} ({ex['categoria']})")

        # Selecionar exercício existente
        while True:
            entrada = input("Escolha o exercício pelo número: ").strip()
            if not entrada.isdigit():
                print("❌ Digite apenas números!")
                continue
            idx = int(entrada) - 1
            if idx < 0 or idx >= len(lista_exercicios):
                print("❌ Opção inválida!")
                continue
            exercicio_escolhido = lista_exercicios[idx]
            break

        # Perguntar séries e repetições
        while True:
            try:
                series = int(input("Quantas séries? "))
                if series <= 0:
                    print("❌ Número de séries inválido!")
                    continue
                reps = []
                for i in range(series):
                    while True:
                        try:
                            r = int(input(f"Repetições da série {i+1}: "))
                            reps.append(r)
                            break
                        except ValueError:
                            print("❌ Valor inválido!")
                break
            except ValueError:
                print("❌ Valor inválido!")

        #    Adicionar ao treino
        treino["exercicios"].append({
            "nome": exercicio_escolhido["nome"],
            "categoria": exercicio_escolhido["categoria"],
            "series": reps
        })


    elif opcao == 3:
        if not treino["exercicios"]:
            print("❌ Nenhum exercício para editar!")
            return

        for i, ex in enumerate(treino["exercicios"], start=1):
            print(f"[{i}] {ex['nome']} - {ex['series']}")

        while True:
            entrada = input("Escolha o exercício: ").strip()
            if not entrada.isdigit():
                print("❌ Digite apenas números!")
                continue
            idx = int(entrada) - 1
            if idx < 0 or idx >= len(treino["exercicios"]):
                print("❌ Opção inválida!")
                continue
            exercicio = treino["exercicios"][idx]
            break

        print(f"\nEditando: {exercicio['nome']}")
        print(f"Séries atuais: {len(exercicio['series'])}")

        while True:
            entrada = input("Nova quantidade de séries: ").strip()
            if not entrada.isdigit() or int(entrada) <= 0:
                print("❌ Quantidade inválida!")
                continue
            nova_qtd = int(entrada)
            break

        novas_series = []
        for i in range(nova_qtd):
            while True:
                entrada = input(f"Repetições da série {i+1}: ").strip()
                if not entrada.isdigit():
                    print("❌ Valor inválido!")
                    continue
                novas_series.append(int(entrada))
                break

        exercicio["series"] = novas_series

    elif opcao == 4:
        if not treino["exercicios"]:
            print("❌ Nenhum exercício para remover!")
            return

        for i, ex in enumerate(treino["exercicios"], start=1):
            print(f"[{i}] {ex['nome']}")

        while True:
            entrada = input("Remover qual exercício? ").strip()
            if not entrada.isdigit():
                print("❌ Digite apenas números!")
                continue
            idx = int(entrada) - 1
            if idx < 0 or idx >= len(treino["exercicios"]):
                print("❌ Opção inválida!")
                continue
            #removido = treino["exercicios"].pop(idx)
            #print(f"✅ Removido: {removido['nome']}")
           # break

   # print("✅ Atualização concluída!")
            # Confirmação antes de remover
            while True:
                conf = input(f"Tem certeza que deseja remover '{treino['exercicios'][idx]['nome']}'? (s/n): ").strip().lower()
                if conf not in ["s", "n"]:
                    print("❌ Responda apenas com 's' ou 'n'.")
                    continue
                if conf == "n":
                    print("❌ Exclusão cancelada.")
                    return
                break

# Remove após confirmar
            removido = treino["exercicios"].pop(idx)
            print(f"✅ Removido: {removido['nome']}")
            break


