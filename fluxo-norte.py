from random import choice, randint


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
    print(
        f"ID do pedido: {idPedido}, "
        f"Nome do cliente: {info[0]}, "
        f"Endereco: {info[1]}, "
        f"Prioridade: {info[2]}, "
        f"Descricao do produto: {info[3]}, "
        f"Status: {info[4]}, "
        f"ID do entregador: {info[5]}"
    )


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
    print("\n\n\tCADASTRAR PEDIDO")

    idPedido = gerarIdPedidoUnico(pedidos)
    nome = input("Insira o nome do cliente: ").upper()
    endereco = input("Insira o endereco: ").upper()

    print("NIVEIS DE PRIORIDADE")
    print("\tDigite 1 para PRIORIDADE ALTA")
    print("\tDigite 2 para PRIORIDADE NORMAL")
    prioridade = int(input("Informe o nivel de prioridade: "))

    match prioridade:
        case 1:
            prioridade = "ALTA"
        case 2:
            prioridade = "NORMAL"

    descricao = input("Digite a descricao do produto: ").upper()
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

    print(f"\n[SUCESSO] Pedido {idPedido} cadastrado no sistema!\n\n")
    return pedidos


def cadastrarEntregadores(pedidos, entregadores):
    print("\n\n\tCADASTRAR ENTREGADOR")

    idEntregador = gerarIdEntregadorUnico(entregadores)
    nome = input("Insira o nome do entregador: ").upper()

    print("TIPOS DE VEICULOS")
    print("\tDigite 1 para CARRO")
    print("\tDigite 2 para MOTO")
    print("\tDigite 3 para VAN")
    veiculo = int(input("Informe o veiculo do entregador: "))

    match veiculo:
        case 1:
            veiculo = "CARRO"
        case 2:
            veiculo = "MOTO"
        case 3:
            veiculo = "VAN"

    print("DISPONIBILIDADE")
    print("\tDigite 1 para DISPONIVEL")
    print("\tDigite 2 para INDISPONIVEL")
    disponibilidade = int(input("Informe a disponibilidade do entregador: "))

    match disponibilidade:
        case 1:
            disponibilidade = "DISPONIVEL"
        case 2:
            disponibilidade = "INDISPONIVEL"

    idPedidos = []
    entregadores[idEntregador] = [nome, veiculo, disponibilidade, idPedidos]
    print(f"\n[SUCESSO] Entregador {idEntregador} cadastrado no sistema!\n")

    return entregadores


def atualizarPedidos(pedidos, entregadores):
    print("\n--- Atualizacao dos Pedidos ---")
    print("1 - Alterar o status do pedido")
    print("2 - Cancelar o pedido")
    print("3 - Associar entregador a pedido")
    print("4 - Remover associacao de entregador")
    print("5 - Voltar ao menu principal\n")

    opcao = int(input("Digite a opcao desejada: "))

    if opcao == 1:
        idPedido = input("Digite o ID do pedido: ").upper()
        if idPedido in pedidos:
            if pedidos[idPedido][4] == "CANCELADO":
                print("[ERRO] Pedido cancelado nao pode ser reativado ou alterado.")
                return

            print("STATUS")
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

            print(f"[SUCESSO] Status do pedido {idPedido} atualizado!")
        else:
            print("[ERRO] Pedido nao encontrado.")

    elif opcao == 2:
        idPedido = input("Digite o ID do pedido: ").upper()
        if idPedido in pedidos:
            if pedidos[idPedido][4] == "CANCELADO":
                print("[ERRO] Pedido ja esta cancelado.")
            else:
                pedidos[idPedido][4] = "CANCELADO"
                removerPedidoDoEntregador(idPedido, pedidos, entregadores)
                print(f"[SUCESSO] Pedido {idPedido} cancelado!")
        else:
            print("[ERRO] Pedido nao encontrado.")

    elif opcao == 3:
        idPedido = input("Digite o ID do pedido: ").upper()
        if idPedido in pedidos:
            if pedidos[idPedido][4] == "CANCELADO":
                print("[ERRO] Pedido cancelado nao pode ser associado a entregador.")
            elif pedidos[idPedido][4] == "ENTREGUE":
                print("[ERRO] Pedido entregue nao pode ser associado a entregador.")
            else:
                idEntregador = input("Digite o ID do entregador: ").upper()

                if idEntregador in entregadores:
                    if pedidos[idPedido][5] == idEntregador:
                        print("[ERRO] Pedido ja esta associado a este entregador.")
                    elif len(entregadores[idEntregador][3]) >= 10:
                        print("[ERRO] Entregador ja atingiu o limite de 10 pedidos.")
                    else:
                        removerPedidoDoEntregador(idPedido, pedidos, entregadores)
                        pedidos[idPedido][5] = idEntregador
                        entregadores[idEntregador][3].append(idPedido)
                        ordenarPedidosDoEntregador(idEntregador, pedidos, entregadores)
                        print(f"[SUCESSO] Pedido {idPedido} associado ao entregador {idEntregador}!")
                else:
                    print("[ERRO] Entregador nao encontrado.")
        else:
            print("[ERRO] Pedido nao encontrado.")

    elif opcao == 4:
        idPedido = input("Digite o ID do pedido: ").upper()
        if idPedido in pedidos:
            if pedidos[idPedido][5] != "NAO ASSOCIADO":
                removerPedidoDoEntregador(idPedido, pedidos, entregadores)
                print(f"[SUCESSO] Associacao removida do pedido {idPedido}.")
            else:
                print("[ERRO] Pedido nao possui entregador associado.")
        else:
            print("[ERRO] Pedido nao encontrado.")

    elif opcao == 5:
        print("Voltando ao menu principal...")


def consultarInformacoes(pedidos, entregadores):
    print("\n--- Consulta de Informacoes ---")
    print("1 - Pedidos Pendentes")
    print("2 - Pedidos Entregues")
    print("3 - Buscar pedido por ID")
    print("4 - Entregadores disponiveis")
    print("5 - Todas as entregas realizadas por um entregador")
    print("6 - Voltar para o menu principal\n")

    opcao = int(input("Digite a opcao desejada: "))

    match opcao:
        case 1:
            print("\nPedidos Pendentes:")
            encontrou = 0
            for idPedido, info in pedidos.items():
                if info[4] == "PENDENTE":
                    mostrarPedido(idPedido, info)
                    encontrou = 1
            if encontrou == 0:
                print("Nenhum pedido pendente encontrado.")

        case 2:
            print("\nPedidos Entregues:")
            encontrou = 0
            for idPedido, info in pedidos.items():
                if info[4] == "ENTREGUE":
                    mostrarPedido(idPedido, info)
                    encontrou = 1
            if encontrou == 0:
                print("Nenhum pedido entregue encontrado.")

        case 3:
            idPedido = input("Digite o ID do pedido que deseja buscar: ").upper()
            if idPedido in pedidos:
                mostrarPedido(idPedido, pedidos[idPedido])
            else:
                print("Pedido nao encontrado.")

        case 4:
            print("\nEntregadores Disponiveis:")
            encontrou = 0
            for idEntregador, info in entregadores.items():
                if info[2] == "DISPONIVEL":
                    print(
                        f"ID do entregador: {idEntregador}, "
                        f"Nome do entregador: {info[0]}, "
                        f"Veiculo: {info[1]}, "
                        f"Disponibilidade: {info[2]}, "
                        f"Pedidos associados: {info[3]}"
                    )
                    encontrou = 1
            if encontrou == 0:
                print("Nenhum entregador disponivel encontrado.")

        case 5:
            idEntregador = input("Digite o ID do entregador para ver suas entregas: ").upper()
            if idEntregador not in entregadores:
                print("[ERRO] Entregador nao encontrado.")
                return

            print(f"\nEntregas do entregador {idEntregador}:")
            idPedidos = entregadores[idEntregador][3]
            if idPedidos == []:
                print("Nenhum pedido associado a este entregador.")
            else:
                for idPedido in idPedidos:
                    mostrarPedido(idPedido, pedidos[idPedido])

        case 6:
            print("Voltando ao menu principal...")


def relatoriosOperacionais(pedidos, entregadores):
    menuRelatorio = 1

    while menuRelatorio == 1:
        print("\n--- Relatorios Operacionais ---")
        print("1 - Total de Pedidos")
        print("2 - Quantidade de pedidos por status")
        print("3 - Pedidos com Alta Prioridade")
        print("4 - Entregador com maior numero de entregas")
        print("5 - Voltar ao menu principal\n")

        opcao = int(input("Digite a opcao desejada: "))

        if opcao == 1:
            total = 0
            for idPedido in pedidos:
                total = total + 1
            print(f"\n\tTotal de pedidos cadastrados no sistema: {total}\n")

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

            print("\n--- Pedidos por Status ---")
            print(f"PENDENTE: {pendente}")
            print(f"EM ROTA: {emRota}")
            print(f"ENTREGUE: {entregue}")
            print(f"CANCELADO: {cancelado}")

        elif opcao == 3:
            listaAlta = []

            for idPedido in pedidos:
                if pedidos[idPedido][2] == "ALTA":
                    listaAlta.append(idPedido)

            if listaAlta == []:
                print("\n\tNenhum pedido com prioridade ALTA.")
            else:
                print(f"\n--- Pedidos com prioridade ALTA ({len(listaAlta)}) ---")

                for idPedido in listaAlta:
                    info = pedidos[idPedido]
                    print(
                        f"ID: {idPedido} | "
                        f"Cliente: {info[0]} | "
                        f"Status: {info[4]} | "
                        f"Entregador: {info[5]}"
                    )
                print()

        elif opcao == 4:
            if entregadores == {}:
                print("Nenhum entregador cadastrado no sistema")
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
                    print("Nenhuma entrega concluida ate o momento")
                else:
                    nomeEntregador = entregadores[melhorEntregador][0]
                    print("\n--- Entregador Destaque ---")
                    print(f"ID: {melhorEntregador}")
                    print(f"Nome: {nomeEntregador}")
                    print(f"Entregas: {maiorNumero}")

        elif opcao == 5:
            menuRelatorio = 0


print("\n\n----------Bem-vindo ao sistema de gerenciamento de entregas da Fluxo Norte!----------\n\n")

while rodando != 0:
    print("-" * 20 + " MENU " + "-" * 20 + "\n")
    print("1 - Cadastro de pedidos")
    print("2 - Cadastro de Entregadores")
    print("3 - Atualizacao dos pedidos")
    print("4 - Consulta de informacoes")
    print("5 - Relatorios operacionais")
    print("6 - Finalizar o sistema\n")

    opcao = int(input("Digite a opcao desejada: "))

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
            print("Sistema finalizado. Obrigado por usar o sistema de gerenciamento de entregas da Fluxo Norte!")
            rodando = 0
