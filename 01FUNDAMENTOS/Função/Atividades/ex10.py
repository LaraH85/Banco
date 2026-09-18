
livros = []

categorias = (
    "Romance",
    "Aventura",
    "Tecnologia",
    "História",
    "Ciência",
    "Infantil"
)

while True:

    print("\n" + "=" * 15, 'BILIOTECA',"=" * 15 )

    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Procurar livro pelo título")
    print("4 - Alterar quantidade disponível")
    print("5 - Excluir livro")
    print("6 - Relatório")

    print("\n========  DESAFIOS  ==========")
    print("7 - Procurar livro pelo autor")
    print("8 - Procurar código do livro")
    print("9 - Filtrar livros por categoria")
    print("10 - Listar livros em ordem alfabética")
    print("11 - Categoria com mais livros")
    print(30* "=")

    print("\n0 - Sair")

    opcao = input("\nEscolha: ")

    if opcao == "1":

        print("\n" + "=" * 15, 'CADASTRAR LIVRO',"=" * 15 )

        # Verificação do código
        while True:

            try:
                codigo = int(input("Código do livro: "))

                if codigo <= 0:
                    print("O código deve ser maior que zero.")

                else:
                    # Verifica se o código já existe
                    codigo_existe = False

                    for livro in livros:

                        if livro["codigo"] == codigo:
                            codigo_existe = True

                    if codigo_existe:
                        print("ERRO: Esse código já está cadastrado!")

                    else:
                        break

            except ValueError:
                print("Digite apenas números.")

        # Título
        titulo = input("Título: ").strip()

        while titulo == "":
            print("O título não pode ficar vazio.")
            titulo = input("Título: ").strip()

        # Autor
        autor = input("Autor: ").strip()

        while autor == "":
            print("O autor não pode ficar vazio.")
            autor = input("Autor: ").strip()

        # Ano
        while True:

            try:
                ano = int(input("Ano de publicação: "))

                if ano < 0:
                    print("O ano não pode ser negativo.")

                elif ano > 2026:
                    print(f'Não pode colocar maior que 2026.')

                else:
                    break

            except ValueError:
                print("Digite apenas números.")

        # Categoria
        while True:

            print("\nCategorias disponíveis:")

            for i in range(len(categorias)):
                print(f"{i + 1} - {categorias[i]}")

            try:
                escolha_categoria = int(input("Escolha a categoria: "))

                if (escolha_categoria >= 1
                    and escolha_categoria <= len(categorias)):

                    categoria = categorias[escolha_categoria - 1]
                    break

                else:
                    print("Categoria inválida!")

            except ValueError:
                print("Digite apenas números.")

        # Quantidade
        while True:

            try:
                quantidade = int(
                    input("Quantidade disponível: ")
                )

                if quantidade < 0:
                    print("A quantidade não pode ser negativa.")

                else:
                    break

            except ValueError:
                print("Digite apenas números.")

        # Criação do dicionário
        livro = {
            "codigo": codigo,
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "categoria": categoria,
            "quantidade": quantidade
        }

        # Adiciona o livro à lista
        livros.append(livro)

        print("\nLivro cadastrado com sucesso!")

    elif opcao == "2":
        print("\n" + "=" * 50)
        print("                LISTA DE LIVROS")
        print("=" * 50)

        if len(livros) == 0:

            print("Nenhum livro cadastrado.")

        else:

            for livro in livros:
                print("\n----------------------------------------")
                print(f"Código:       {livro['codigo']}")
                print(f"Título:       {livro['titulo']}")
                print(f"Autor:        {livro['autor']}")
                print(f"Ano:          {livro['ano']}")
                print(f"Categoria:    {livro['categoria']}")
                print(f"Quantidade:   {livro['quantidade']}")

            print("----------------------------------------")

    elif opcao == "3":

        print("\n" + "=" * 15, 'PROCURAR LIVRO', "=" * 15 )

        if len(livros) == 0:

            print("Nenhum livro cadastrado.")

        else:

            titulo_pesquisa = input("Digite o título do livro: ").strip()

            encontrou = False

            for livro in livros:

                if livro["titulo"].lower() == titulo_pesquisa.lower():
                    print("\nLivro encontrado!")
                    print("----------------------------------------")
                    print(f"Código:       {livro['codigo']}")
                    print(f"Título:       {livro['titulo']}")
                    print(f"Autor:        {livro['autor']}")
                    print(f"Ano:          {livro['ano']}")
                    print(f"Categoria:    {livro['categoria']}")
                    print(f"Quantidade:   {livro['quantidade']}")
                    print("----------------------------------------")

                    encontrou = True

            if encontrou == False:
                print("\nLivro não encontrado.")

    elif opcao == "4":

        print("\n" + "=" * 15, 'ALTERAR QUANTIDADE', "=" * 15 )

        if len(livros) == 0:

            print("Nenhum livro cadastrado.")

        else:
            while True:

                try:
                    codigo_pesquisa = int(
                        input("Digite o código do livro: ")
                    )

                    if codigo_pesquisa <= 0:
                        print("Digite um código válido.")

                    else:
                        break

                except ValueError:
                    print("Digite apenas números.")

            livro_encontrado = None

            for livro in livros:

                if livro["codigo"] == codigo_pesquisa:
                    livro_encontrado = livro

            if livro_encontrado is None:

                print("\nLivro não encontrado.")

            else:

                print(
                    f"\nLivro: {livro_encontrado['titulo']}"
                )

                print(
                    f"Quantidade atual: "
                    f"{livro_encontrado['quantidade']}"
                )

                while True:

                    try:
                        nova_quantidade = int(
                            input("Nova quantidade: ")
                        )

                        if nova_quantidade < 0:
                            print(
                                "A quantidade não pode ser negativa."
                            )

                        else:
                            break

                    except ValueError:
                        print("Digite apenas números.")

                livro_encontrado["quantidade"] = nova_quantidade

                print(
                    "\nQuantidade alterada com sucesso!"
                )

    elif opcao == "5":

        print("\n" + "=" * 15, 'EXCLUIR LIVRO', "=" * 15 )

        if len(livros) == 0:

            print("Nenhum livro cadastrado.")

        else:

            while True:

                try:
                    codigo_exclusao = int(
                        input("Digite o código do livro: ")
                    )

                    if codigo_exclusao <= 0:
                        print("Digite um código válido.")

                    else:
                        break

                except ValueError:
                    print("Digite apenas números.")

            livro_excluir = None

            for livro in livros:

                if livro["codigo"] == codigo_exclusao:
                    livro_excluir = livro

            if livro_excluir is None:

                print("\nLivro não encontrado.")

            else:

                print(
                    f"\nLivro encontrado: "
                    f"{livro_excluir['titulo']}"
                )

                confirmacao = input(
                    "Deseja realmente excluir? (S/N): "
                ).upper()

                if confirmacao == "S":

                    livros.remove(livro_excluir)

                    print(
                        "\nLivro excluído com sucesso!"
                    )

                else:

                    print("\nExclusão cancelada.")

    elif opcao == "6":

        print("\n" + "=" * 15, 'RELATÓRIO', "=" * 15 )

        if len(livros) == 0:

            print("Nenhum livro cadastrado.")

        else:

            # Quantidade de livros cadastrados
            total_livros = len(livros)

            # Quantidade total de exemplares
            total_exemplares = 0

            for livro in livros:
                total_exemplares += livro["quantidade"]

            # Livro mais antigo
            livro_antigo = livros[0]

            for livro in livros:

                if livro["ano"] < livro_antigo["ano"]:
                    livro_antigo = livro

            # Livro mais novo
            livro_novo = livros[0]

            for livro in livros:

                if livro["ano"] > livro_novo["ano"]:
                    livro_novo = livro

            # Maior quantidade
            maior_quantidade = livros[0]

            for livro in livros:

                if (
                        livro["quantidade"]
                        > maior_quantidade["quantidade"]
                ):
                    maior_quantidade = livro

            # Menor quantidade
            menor_quantidade = livros[0]

            for livro in livros:

                if (
                        livro["quantidade"]
                        < menor_quantidade["quantidade"]
                ):
                    menor_quantidade = livro

            # Média
            media = total_exemplares / total_livros

            # Exibição
            print(
                f"\nQuantidade de livros cadastrados: "
                f"{total_livros}"
            )

            print(
                f"Quantidade total de exemplares: "
                f"{total_exemplares}"
            )

            print(
                f"\nLivro mais antigo:"
                f"\nTítulo: {livro_antigo['titulo']}"
                f"\nAno: {livro_antigo['ano']}"
            )

            print(
                f"\nLivro mais novo:"
                f"\nTítulo: {livro_novo['titulo']}"
                f"\nAno: {livro_novo['ano']}"
            )

            print(
                f"\nLivro com maior quantidade:"
                f"\nTítulo: {maior_quantidade['titulo']}"
                f"\nQuantidade: "
                f"{maior_quantidade['quantidade']}"
            )

            print(
                f"\nLivro com menor quantidade:"
                f"\nTítulo: {menor_quantidade['titulo']}"
                f"\nQuantidade: "
                f"{menor_quantidade['quantidade']}"
            )

            print(
                f"\nMédia de exemplares por livro: "
                f"{media:.2f}"
            )

            print("\nQuantidade de livros por categoria:")

            for categoria in categorias:

                contador = 0

                for livro in livros:

                    if livro["categoria"] == categoria:
                        contador += 1

                print(
                    f"- {categoria}: {contador}"
                )


    elif opcao == "7":

        print("\n" + "=" * 15, 'PROCURAR POR AUTOR', "=" * 15)

        if len(livros) == 0:

            print("Nenhum livro cadastrado.")

        else:

            autor_pesquisa = input(
                "Digite o nome do autor: "
            ).strip()

            encontrou = False

            for livro in livros:

                if (
                        autor_pesquisa.lower()
                        in livro["autor"].lower()
                ):
                    print("\n----------------------------------------")
                    print(f"Código: {livro['codigo']}")
                    print(f"Título: {livro['titulo']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Ano: {livro['ano']}")
                    print(
                        f"Categoria: {livro['categoria']}"
                    )
                    print(
                        f"Quantidade: {livro['quantidade']}"
                    )

                    encontrou = True

            if encontrou == False:
                print(
                    "\nNenhum livro desse autor "
                    "foi encontrado."
                )
    elif opcao == "8":

        print("\n" + "=" * 15, 'PROCURAR POR CÓDIGO', "=" * 15)

        if len(livros) == 0:

            print("Nenhum código cadastrado.")

        else:

            codigo = int(input(
                "Digite o número do código: "
            ))

            encontrou = False

            for livro in livros:


                    print("\n----------------------------------------")
                    print(f"Código: {livro['codigo']}")
                    print(f"Título: {livro['titulo']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Ano: {livro['ano']}")
                    print(
                        f"Catégoria: {livro['codigo']}"
                    )
                    print(
                        f"Quantidade: {livro['quantidade']}"
                    )

                    encontrou = True

            if encontrou == False:
                print(
                    "\nNenhum código desse cadastro "
                    "foi encontrado."
                )

    elif opcao == "9":

        print("\n" + "=" * 15, 'FILTRAR POR CATEGORIA', "=" * 15)

        if len(livros) == 0:

            print("Nenhum livro cadastrado.")

        else:

            print("\nCategorias:")

            for i in range(len(categorias)):
                print(
                    f"{i + 1} - {categorias[i]}"
                )

            while True:

                try:

                    escolha = int(
                        input("Escolha uma categoria: ")
                    )

                    if (
                            escolha >= 1
                            and escolha <= len(categorias)
                    ):
                        break

                    else:
                        print("Categoria inválida.")

                except ValueError:

                    print("Digite apenas números.")

            categoria_escolhida = categorias[
                escolha - 1
                ]

            encontrou = False

            print(
                f"\nLivros da categoria "
                f"{categoria_escolhida}:"
            )

            for livro in livros:

                if (
                        livro["categoria"]
                        == categoria_escolhida
                ):
                    print("\n--------------------------------")
                    print(
                        f"Código: {livro['codigo']}"
                    )
                    print(
                        f"Título: {livro['titulo']}"
                    )
                    print(
                        f"Autor: {livro['autor']}"
                    )
                    print(
                        f"Quantidade: "
                        f"{livro['quantidade']}"
                    )

                    encontrou = True

            if encontrou == False:
                print(
                    "\nNenhum livro dessa categoria "
                    "foi cadastrado."
                )

    elif opcao == "10":

        print("\n" + "=" * 15, 'LIVROS EM ORDEM ALFABÉTICA', "=" * 15)

        if len(livros) == 0:

            print("Nenhum livro cadastrado.")

        else:

            # Faz uma cópia da lista
            livros_ordenados = livros.copy()

            # Ordenação manual
            for i in range(len(livros_ordenados)):

                menor = i

                for j in range(
                        i + 1,
                        len(livros_ordenados)
                ):

                    titulo_atual = (
                        livros_ordenados[j]["titulo"]
                        .lower()
                    )

                    titulo_menor = (
                        livros_ordenados[menor]["titulo"]
                        .lower()
                    )

                    if titulo_atual < titulo_menor:
                        menor = j

                # Troca os livros
                temporario = livros_ordenados[i]

                livros_ordenados[i] = (
                    livros_ordenados[menor]
                )

                livros_ordenados[menor] = temporario

            # Exibe os livros
            for livro in livros_ordenados:
                print(
                    f"\n{livro['titulo']}"
                    f" - {livro['autor']}"
                    f" ({livro['ano']})"
                )

    elif opcao == "11":

        print("\n" + "=" * 15, 'CATEGORIA COM MAIS LIVROS', "=" * 15)

        if len(livros) == 0:

            print("Nenhum livro cadastrado.")

        else:

            maior_categoria = categorias[0]
            maior_total = 0

            for categoria in categorias:

                contador = 0

                for livro in livros:

                    if livro["categoria"] == categoria:
                        contador += 1

                if contador > maior_total:
                    maior_total = contador
                    maior_categoria = categoria

            print(
                f"\nCategoria com mais livros: "
                f"{maior_categoria}"
            )

            print(
                f"Quantidade de livros: "
                f"{maior_total}"
            )

    elif opcao == "0":
        print("\nSistema encerrado!")
        print("Obrigado por utilizar a biblioteca.")
        break

    else:
        print("\nOpção inválida! Tente novamente.")

    if opcao != "0":
        input(
            "\nPressione ENTER para continuar..."
        )