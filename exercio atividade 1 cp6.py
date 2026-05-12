#nome: Guilherme cruz alves 
#rm: 56686

funcionarios = []

while True:
    print("""
========================
        MENU
========================

0 - SAIR
1 - CADASTRAR FUNCIONÁRIO
2 - CONSULTAR FUNCIONÁRIO
5 - LISTAR FUNCIONÁRIOS

ESCOLHA:
""", end=" ")

    opcao = input()

    match opcao:

        # SAIR
        case "0":
            print("\nEncerrando sistema...")
            break

        # CADASTRAR
        case "1":
            print("\n========================")
            print(" CADASTRANDO FUNCIONÁRIO")
            print("========================")

            nome = input("\nNome: ")
            cpf = input("CPF: ")
            salario = float(input("Salário: "))

            funcionario = {
                "nome": nome,
                "cpf": cpf,
                "salario": salario
            }

            funcionarios.append(funcionario)

            print("\nFuncionário cadastrado com sucesso!")
            input("\nPressione ENTER para continuar...")

        # CONSULTAR
        case "2":
            print("\n========================")
            print(" CONSULTANDO FUNCIONÁRIO")
            print("========================")

            cpf_busca = input("\nCPF......: ")

            encontrado = False

            for f in funcionarios:

                if f["cpf"] == cpf_busca:
                    print("\nCPF......:", f["cpf"])
                    print("Nome.....:", f["nome"])
                    print("Salário..:", f["salario"])

                    encontrado = True
                    break

            if encontrado == False:
                print("\nFuncionário inexistente!")

            input("\nPressione ENTER para continuar...")

        # LISTAR
        case "5":
            print("\n========================")
            print(" LISTA DE FUNCIONÁRIOS")
            print("========================")

            if len(funcionarios) == 0:
                print("\nNenhum funcionário cadastrado!")

            else:
                for i, f in enumerate(funcionarios, 1):
                    print(f"""
Funcionário {i}

CPF......: {f['cpf']}
Nome.....: {f['nome']}
Salário..: {f['salario']}
""")

            input("Pressione ENTER para continuar...")

        # OPÇÃO INVÁLIDA
        case _:
            print("\nOpção inválida!")
            input("Pressione ENTER para continuar...")
            