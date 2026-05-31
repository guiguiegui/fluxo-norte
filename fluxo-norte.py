from random import choice, randint


VERDE = "\033[32m"
VERMELHO = "\033[31m"
AMARELO = "\033[33m"
CIANO = "\033[36m"
RESET = "\033[0m"

pedidos = {}
entregadores = {}
rodando = 1


def gerarIdPedidoUnico(pedidos):
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while True:
        letra = choice(letras)
        numeros = f"{randint(0, 9999):04d}"
        idPedido = letra + numeros

        if idPedido not in pedidos:
            return idPedido


def gerarIdEntregadorUnico(entregadores):
    numeroAtual = len(entregadores) + 1
    idEntregador = f"{numeroAtual:04d}"

    while idEntregador in entregadores:
        numeroAtual = numeroAtual + 1
        idEntregador = f"{numeroAtual:04d}"

    return idEntregador


def mostrarPedido(idPedido, info):
    print("-" * 50)
    print(f"ID do pedido     : {AMARELO}{idPedido}{RESET}")
    print(f"Cliente          : {info[0]}")
    print(f"Endereço         : {info[1]}")
    print(f"Prioridade       : {info[2]}")
    print(f"Descrição        : {info[3]}")
    print(f"Status           : {info[4]}")
    print(f"ID do entregador : {info[5]}")


def removerPedidoDoEntregador(idPedido, pedidos, entregadores):
    idEntregador = pedidos[idPedido][5]

    if idEntregador != "NAO ASSOCIADO" and idEntregador in entregadores:
        if idPedido in entregadores[idEntregador][3]:
            entregadores[idEntregador][3].remove(idPedido)

    pedidos[idPedido][5] = "NAO ASSOCIADO"


def ordenarPedidosDoEntregador(idEntregador, pedidos, entregadores):
    listaPedidos = entregadores[idEntregador][3]
    listaOrdenada = []
    maiorOrdem = 0

    for idPedido in listaPedidos:
        if pedidos[idPedido][6] > maiorOrdem:
            maiorOrdem = pedidos[idPedido][6]

    ordemAtual = 1
    while ordemAtual <= maiorOrdem:
        for idPedido in listaPedidos:
            if pedidos[idPedido][2] == "ALTA" and pedidos[idPedido][6] == ordemAtual:
                listaOrdenada.append(idPedido)
        ordemAtual = ordemAtual + 1

    ordemAtual = 1
    while ordemAtual <= maiorOrdem:
        for idPedido in listaPedidos:
            if pedidos[idPedido][2] == "NORMAL" and pedidos[idPedido][6] == ordemAtual:
                listaOrdenada.append(idPedido)
        ordemAtual = ordemAtual + 1

    entregadores[idEntregador][3] = listaOrdenada


def cadastrarPedido(pedidos):
    print("\n" + "-" * 50)
    print("CADASTRO DE PEDIDO")
    print("-" * 50)

    idPedido = gerarIdPedidoUnico(pedidos)
    nome = input("Informe o nome do cliente: ").upper()
    endereco = input("Informe o endereço: ").upper()

    print("\nPRIORIDADE")
    print("1 - ALTA")
    print("2 - NORMAL")
    prioridade = int(input("Informe o nível de prioridade: "))

    match prioridade:
        case 1:
            prioridade = "ALTA"
        case 2:
            prioridade = "NORMAL"

    descricao = input("Informe a descrição do produto: ").upper()
    ordemPedido = len(pedidos) + 1

    pedidos[idPedido] = [
        nome,
        endereco,
        prioridade,
        descricao,
        "PENDENTE",
        "NAO ASSOCIADO",
        ordemPedido
    ]

    print(f"\n{VERDE}[SUCESSO]{RESET} Pedido {AMARELO}{idPedido}{RESET} cadastrado no sistema!\n")
    return pedidos


def cadastrarEntregadores(pedidos, entregadores):
    print("\n" + "-" * 50)
    print("CADASTRO DE ENTREGADOR")
    print("-" * 50)

    idEntregador = gerarIdEntregadorUnico(entregadores)
    nome = input("Informe o nome do entregador: ").upper()

    print("\nVEICULO")
    print("1 - CARRO")
    print("2 - MOTO")
    print("3 - VAN")
    veiculo = int(input("Informe o veículo do entregador: "))

    match veiculo:
        case 1:
            veiculo = "CARRO"
        case 2:
            veiculo = "MOTO"
        case 3:
            veiculo = "VAN"

    print("\nDISPONIBILIDADE")
    print("1 - DISPONIVEL")
    print("2 - INDISPONIVEL")
    disponibilidade = int(input("Informe a disponibilidade do entregador: "))

    match disponibilidade:
        case 1:
            disponibilidade = "DISPONIVEL"
        case 2:
            disponibilidade = "INDISPONIVEL"

    idPedidos = []
    entregadores[idEntregador] = [nome, veiculo, disponibilidade, idPedidos]
    print(f"\n{VERDE}[SUCESSO]{RESET} Entregador {idEntregador} cadastrado no sistema!\n")

    return entregadores


def atualizarPedidos(pedidos, entregadores):
    print("\n" + "-" * 50)
    print("ATUALIZAÇÃO DOS PEDIDOS")
    print("-" * 50)
    print("1 - Alterar o status do pedido")
    print("2 - Cancelar o pedido")
    print("3 - Associar entregador a pedido")
    print("4 - Remover associação de entregador")
    print("5 - Voltar ao menu principal\n")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        idPedido = input("Digite o ID do pedido: ").upper()
        if idPedido in pedidos:
            if pedidos[idPedido][4] == "CANCELADO":
                print(f"{VERMELHO}[ERRO]{RESET} Pedido cancelado não pode ser reativado ou alterado.")
                return

            print("\nSTATUS")
            print("1 - PENDENTE")
            print("2 - EM ROTA")
            print("3 - ENTREGUE")
            print("4 - CANCELADO")
            novoStatus = int(input("Informe o novo status: "))

            match novoStatus:
                case 1:
                    pedidos[idPedido][4] = "PENDENTE"
                case 2:
                    pedidos[idPedido][4] = "EM ROTA"
                case 3:
                    pedidos[idPedido][4] = "ENTREGUE"
                case 4:
                    pedidos[idPedido][4] = "CANCELADO"
                    removerPedidoDoEntregador(idPedido, pedidos, entregadores)

            print(f"{VERDE}[SUCESSO]{RESET} Status do pedido {AMARELO}{idPedido}{RESET} atualizado!")
        else:
            print(f"{VERMELHO}[ERRO]{RESET} Pedido não encontrado.")

    elif opcao == 2:
        idPedido = input("Digite o ID do pedido: ").upper()
        if idPedido in pedidos:
            if pedidos[idPedido][4] == "CANCELADO":
                print(f"{VERMELHO}[ERRO]{RESET} Pedido já está cancelado.")
            else:
                pedidos[idPedido][4] = "CANCELADO"
                removerPedidoDoEntregador(idPedido, pedidos, entregadores)
                print(f"{VERDE}[SUCESSO]{RESET} Pedido {AMARELO}{idPedido}{RESET} cancelado!")
        else:
            print(f"{VERMELHO}[ERRO]{RESET} Pedido não encontrado.")

    elif opcao == 3:
        idPedido = input("Digite o ID do pedido: ").upper()
        if idPedido in pedidos:
            if pedidos[idPedido][4] == "CANCELADO":
                print(f"{VERMELHO}[ERRO]{RESET} Pedido cancelado não pode ser associado a entregador.")
            elif pedidos[idPedido][4] == "ENTREGUE":
                print(f"{VERMELHO}[ERRO]{RESET} Pedido entregue não pode ser associado a entregador.")
            else:
                idEntregador = input("Digite o ID do entregador: ").upper()

                if idEntregador in entregadores:
                    if pedidos[idPedido][5] == idEntregador:
                        print(f"{VERMELHO}[ERRO]{RESET} Pedido já está associado a este entregador.")
                    elif len(entregadores[idEntregador][3]) >= 10:
                        print(f"{VERMELHO}[ERRO]{RESET} Entregador já atingiu o limite de 10 pedidos.")
                    else:
                        removerPedidoDoEntregador(idPedido, pedidos, entregadores)
                        pedidos[idPedido][5] = idEntregador
                        entregadores[idEntregador][3].append(idPedido)
                        ordenarPedidosDoEntregador(idEntregador, pedidos, entregadores)
                        print(f"{VERDE}[SUCESSO]{RESET} Pedido {AMARELO}{idPedido}{RESET} associado ao entregador {idEntregador}!")
                else:
                    print(f"{VERMELHO}[ERRO]{RESET} Entregador não encontrado.")
        else:
            print(f"{VERMELHO}[ERRO]{RESET} Pedido não encontrado.")

    elif opcao == 4:
        idPedido = input("Digite o ID do pedido: ").upper()
        if idPedido in pedidos:
            if pedidos[idPedido][5] != "NAO ASSOCIADO":
                removerPedidoDoEntregador(idPedido, pedidos, entregadores)
                print(f"{VERDE}[SUCESSO]{RESET} Associação removida do pedido {AMARELO}{idPedido}{RESET}.")
            else:
                print(f"{VERMELHO}[ERRO]{RESET} Pedido não possui entregador associado.")
        else:
            print(f"{VERMELHO}[ERRO]{RESET} Pedido não encontrado.")

    elif opcao == 5:
        print(f"{CIANO}[INFO]{RESET} Voltando ao menu principal...")
    else:
        print(f"{VERMELHO}[ERRO]{RESET} Opção inválida.")


def consultarInformacoes(pedidos, entregadores):
    print("\n" + "-" * 50)
    print("CONSULTA DE INFORMAÇÕES")
    print("-" * 50)
    print("1 - Pedidos pendentes")
    print("2 - Pedidos entregues")
    print("3 - Buscar pedido por ID")
    print("4 - Entregadores disponíveis")
    print("5 - Listar todas as entregas realizadas por um entregador")
    print("6 - Voltar para o menu principal\n")

    opcao = int(input("Digite a opção desejada: "))

    match opcao:
        case 1:
            print("\n" + "-" * 50)
            print("PEDIDOS PENDENTES")
            encontrou = 0
            for idPedido, info in pedidos.items():
                if info[4] == "PENDENTE":
                    mostrarPedido(idPedido, info)
                    encontrou = 1
            if encontrou == 0:
                print(f"{CIANO}[INFO]{RESET} Nenhum pedido pendente encontrado.")

        case 2:
            print("\n" + "-" * 50)
            print("PEDIDOS ENTREGUES")
            encontrou = 0
            for idPedido, info in pedidos.items():
                if info[4] == "ENTREGUE":
                    mostrarPedido(idPedido, info)
                    encontrou = 1
            if encontrou == 0:
                print(f"{CIANO}[INFO]{RESET} Nenhum pedido entregue encontrado.")

        case 3:
            idPedido = input("Digite o ID do pedido que deseja buscar: ").upper()
            if idPedido in pedidos:
                mostrarPedido(idPedido, pedidos[idPedido])
            else:
                print(f"{VERMELHO}[ERRO]{RESET} Pedido não encontrado.")

        case 4:
            print("\n" + "-" * 50)
            print("ENTREGADORES DISPONÍVEIS")
            encontrou = 0
            for idEntregador, info in entregadores.items():
                if info[2] == "DISPONIVEL":
                    print("-" * 50)
                    print(f"ID do entregador  : {idEntregador}")
                    print(f"Nome              : {info[0]}")
                    print(f"Veículo           : {info[1]}")
                    print(f"Disponibilidade   : {info[2]}")
                    print("Pedidos associados: ", end="")
                    for idPedido in info[3]:
                        print(f"{AMARELO}{idPedido}{RESET} ", end="")
                    print()
                    encontrou = 1
            if encontrou == 0:
                print(f"{CIANO}[INFO]{RESET} Nenhum entregador disponível encontrado.")

        case 5:
            idEntregador = input("Digite o ID do entregador para ver suas entregas: ").upper()
            if idEntregador not in entregadores:
                print(f"{VERMELHO}[ERRO]{RESET} Entregador não encontrado.")
                return

            print("\n" + "-" * 50)
            print(f"ENTREGAS DO ENTREGADOR {idEntregador}")
            idPedidos = entregadores[idEntregador][3]
            if idPedidos == []:
                print(f"{CIANO}[INFO]{RESET} Nenhum pedido associado a este entregador.")
            else:
                for idPedido in idPedidos:
                    mostrarPedido(idPedido, pedidos[idPedido])

        case 6:
            print(f"{CIANO}[INFO]{RESET} Voltando ao menu principal...")
        case _:
            print(f"{VERMELHO}[ERRO]{RESET} Opção inválida.")


def relatoriosOperacionais(pedidos, entregadores):
    menuRelatorio = 1

    while menuRelatorio == 1:
        print("\n" + "-" * 50)
        print("RELATORIOS OPERACIONAIS")
        print("-" * 50)
        print("1 - Total de pedidos")
        print("2 - Quantidade de pedidos por status")
        print("3 - Pedidos com alta prioridade")
        print("4 - Entregador com maior número de entregas")
        print("5 - Voltar ao menu principal\n")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            total = 0
            for idPedido in pedidos:
                total = total + 1
            print("\n" + "-" * 50)
            print("RELATÓRIO - TOTAL DE PEDIDOS")
            print(f"Total de pedidos: {total}")

        elif opcao == 2:
            pendente = 0
            emRota = 0
            entregue = 0
            cancelado = 0

            for idPedido in pedidos:
                status = pedidos[idPedido][4]
                if status == "PENDENTE":
                    pendente = pendente + 1
                elif status == "EM ROTA":
                    emRota = emRota + 1
                elif status == "ENTREGUE":
                    entregue = entregue + 1
                elif status == "CANCELADO":
                    cancelado = cancelado + 1

            print("\n" + "-" * 50)
            print("RELATÓRIO - PEDIDOS POR STATUS")
            print(f"PENDENTE  : {pendente}")
            print(f"EM ROTA   : {emRota}")
            print(f"ENTREGUE  : {entregue}")
            print(f"CANCELADO : {cancelado}")

        elif opcao == 3:
            listaAlta = []

            for idPedido in pedidos:
                if pedidos[idPedido][2] == "ALTA":
                    listaAlta.append(idPedido)

            if listaAlta == []:
                print(f"\n{CIANO}[INFO]{RESET} Nenhum pedido com prioridade ALTA.")
            else:
                print("\n" + "-" * 50)
                print(f"RELATÓRIO - PEDIDOS COM PRIORIDADE ALTA ({len(listaAlta)})")

                for idPedido in listaAlta:
                    info = pedidos[idPedido]
                    print("-" * 50)
                    print(f"ID         : {AMARELO}{idPedido}{RESET}")
                    print(f"Cliente    : {info[0]}")
                    print(f"Status     : {info[4]}")
                    print(f"Entregador : {info[5]}")
                print()

        elif opcao == 4:
            if entregadores == {}:
                print(f"{CIANO}[INFO]{RESET} Nenhum entregador cadastrado no sistema.")
            else:
                contagemEntregas = {}

                for idEntregador in entregadores:
                    contagemEntregas[idEntregador] = 0

                for idPedido in pedidos:
                    if pedidos[idPedido][4] == "ENTREGUE":
                        idEntregadorDoPedido = pedidos[idPedido][5]
                        if idEntregadorDoPedido in contagemEntregas:
                            contagemEntregas[idEntregadorDoPedido] = contagemEntregas[idEntregadorDoPedido] + 1

                maiorNumero = 0
                melhorEntregador = "Nenhum"

                for idEntregador in contagemEntregas:
                    if contagemEntregas[idEntregador] > maiorNumero:
                        maiorNumero = contagemEntregas[idEntregador]
                        melhorEntregador = idEntregador

                if maiorNumero == 0:
                    print(f"{CIANO}[INFO]{RESET} Nenhuma entrega concluída até o momento.")
                else:
                    nomeEntregador = entregadores[melhorEntregador][0]
                    print("\n" + "-" * 50)
                    print("RELATÓRIO - ENTREGADOR DESTAQUE")
                    print(f"ID       : {melhorEntregador}")
                    print(f"Nome     : {nomeEntregador}")
                    print(f"Entregas : {maiorNumero}")

        elif opcao == 5:
            menuRelatorio = 0
        else:
            print(f"{VERMELHO}[ERRO]{RESET} Opção Inválida.")


print("\n" + "-" * 50)
print("SISTEMA DE GERENCIAMENTO DE ENTREGAS - FLUXO NORTE")
print("-" * 50)

while rodando != 0:
    print("\n" + "-" * 50)
    print("MENU PRINCIPAL")
    print("-" * 50)
    print("1 - Cadastro de pedidos")
    print("2 - Cadastro de entregadores")
    print("3 - Atualização dos pedidos")
    print("4 - Consulta de informações")
    print("5 - Relatórios operacionais")
    print("6 - Finalizar o sistema\n")

    opcao = int(input("Digite a opção desejada: "))

    match opcao:
        case 1:
            cadastrarPedido(pedidos)
        case 2:
            cadastrarEntregadores(pedidos, entregadores)
        case 3:
            atualizarPedidos(pedidos, entregadores)
        case 4:
            consultarInformacoes(pedidos, entregadores)
        case 5:
            relatoriosOperacionais(pedidos, entregadores)
        case 6:
            print(f"{CIANO}[INFO]{RESET} Sistema finalizado. Obrigado por usar o Fluxo Norte!")
            rodando = 0
        case _:
            print(f"{VERMELHO}[ERRO]{RESET} Opção inválida.")
