from random import choice, randint
from string import ascii_uppercase



pedidos = {}
entregadores = {}
rodando = 1

def cadastrarPedido (pedido):
    print("\n\n\tCADASTRAR PEDIDO")
    letra = choice(ascii_uppercase)
    numeros = f"{randint(0, 9999):04d}"
    id = letra + numeros
    nome = input("Insira o nome do cliente: ").upper()
    endereco = input("Insira o endereço: ").upper()
    print("NÍVEIS DE PRIORIDADE\n\tDigite 1 para PRIORIDADE ALTA\n\tDigite 2 para PRIORIDADE NORMAL")
    prioridade = int(input("Informe o nível de prioridade: "))
    match(prioridade):
        case 1:
            prioridade = "ALTA"
        case 2:
            prioridade = "NORMAL"
        case _:
            prioridade = "NORMAL"
    descricao = input("Digite a descrição do produto: ").upper()
    status = "PENDENTE"
    idEntregador = "NAO ASSOCIADO"
    pedido[id] = [nome, endereco, prioridade, descricao, status, idEntregador]

    if id in pedido:
        print(f"\n[SUCESSO] Pedido {id} cadastrado no sistema!\n\n")
    else:
        print(f"\n[ERRO] Falha ao registrar o pedido {id}.\n\n")
        
    return pedido
    
def cadastrarEntregadores (pedidos, entregadores):
    numAtual = len(entregadores) + 1
    id = f"{numAtual:04d}"
    nome = input("Insira o nome do entregador: ").upper()
    
    print("TIPOS DE VEÍCULOS\n\tDigite 1 para CARRO\n\tDigite 2 para MOTO\n\tDigite 3 para VAN")
    veiculo = int(input("Informe o veículo do entregador: "))
    match(veiculo):
        case 1:
            veiculo = "CARRO"
        case 2:
            veiculo = "MOTO"
        case 3:
            veiculo = "VAN"   

    print("DISPONIBILIDADE\n\tDigite 1 para DISPONÍVEL\n\tDigite 2 para INDISPONIVEL")
    disponibilidade = int(input("Informe a disponibilidade do entregador: "))
    match(disponibilidade):
        case 1:
            disponibilidade = "DISPONIVEL"
        case 2:
            disponibilidade = "INDISPONIVEL"
        case _:
            disponibilidade = "INDISPONIVEL"

    idPedidos = []    
    entregadores[id] = [nome, veiculo, disponibilidade, idPedidos]
    return entregadores

def atualizarPedidos(pedidos, entregadores):
    print("\n--- Atualização dos Pedidos ---")
    print("1 - Alterar o status do pedido")
    print("2 - Cancelar o pedido")
    print("3 - Associar entregador a pedido")
    print("4 - Remover associação de entregador")
    print("5 - Voltar ao menu principal\n")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        idPedido = input("Digite o ID do pedido: ").upper()
        if idPedido in pedidos:
            print("STATUS\n1 - PENDENTE\n2 - EM ROTA\n3 - ENTREGUE\n4 - CANCELADO")
            novo_status = int(input("Informe o novo status: "))
            match novo_status:
                case 1:
                    pedidos[idPedido][4] = "PENDENTE"
                case 2:
                    pedidos[idPedido][4] = "EM ROTA"
                case 3:
                    pedidos[idPedido][4] = "ENTREGUE"
                case 4:
                    pedidos[idPedido][4] = "CANCELADO"
            print(f"[SUCESSO] Status do pedido {idPedido} atualizado!")
        else:
            print("[ERRO] Pedido não encontrado.")

    elif opcao == 2:
        idPedido = input("Digite o ID do pedido: ").upper()
        if idPedido in pedidos:
            pedidos[idPedido][4] = "CANCELADO"
            print(f"[SUCESSO] Pedido {idPedido} cancelado!")
        else:
            print("[ERRO] Pedido não encontrado.")

    elif opcao == 3:
        idPedido = input("Digite o ID do pedido: ").upper()
        if idPedido in pedidos:
            idEntregador = input("Digite o ID do entregador: ").upper()
            if idEntregador in entregadores:
                pedidos[idPedido][5] = idEntregador
                entregadores[idEntregador][3].append(idPedido)
                print(f"[SUCESSO] Pedido {idPedido} associado ao entregador {idEntregador}!")
            else:
                print("[ERRO] Entregador não encontrado.")
        else:
            print("[ERRO] Pedido não encontrado.")

    elif opcao == 4:
        idPedido = input("Digite o ID do pedido: ").upper()
        if idPedido in pedidos:
            idEntregador = pedidos[idPedido][5]
            if idEntregador != "NAO ASSOCIADO" and idEntregador in entregadores:
                entregadores[idEntregador][3].remove(idPedido)
                pedidos[idPedido][5] = "NAO ASSOCIADO"
                print(f"[SUCESSO] Associação removida do pedido {idPedido}.")
            else:
                print("[ERRO] Pedido não possui entregador associado.")
        else:
            print("[ERRO] Pedido não encontrado.")

    elif opcao == 5:
        print("Voltando ao menu principal...")

    else:
        print("[ERRO] Opção inválida.")


def consultarInformacoes(pedidos, entregadores):
    print("Consulta de informações")
    print("\n1 - Pedidos Entregues\n2 - Pedidos Entregues\n3 - Buscar por pedido\n4 - Entregador disponivel\n5 - Todas as entregas realizadas por um entregador\n6 - Voltar para o menu principal\n\n")
    opcao = int(input("Digite a opção desejada: "))
    match(opcao):
        case 1:
            print("Pedidos Entregues: ")
            for id, info in pedidos.items():
                if info[4] == "ENTREGUE":
                    print(f"ID do pedido: {id}, Nome do cliente: {info[0]}, Endereço: {info[1]}, Prioridade: {info[2]}, Descrição do produto: {info[3]}, ID do entregador: {info[4]}")
        case 2:
            print("Pedidos Pendentes: ")
            for id, info in pedidos.items():
                if info[4] == "PENDENTE":
                    print(f"ID do pedido: {id}, Nome do cliente: {info[0]}, Endereço: {info[1]}, Prioridade: {info[2]}, Descrição do produto: {info[3]}, ID do entregador: {info[4]}")
        case 3:
            id_pedido = input("Digite o ID do pedido que deseja buscar: ").upper()
            if id_pedido in pedidos:
                info = pedidos[id_pedido]
                print(f"ID do pedido: {id_pedido}, Nome do cliente: {info[0]}, Endereço: {info[1]}, Prioridade: {info[2]}, Descrição do produto: {info[3]}, ID do entregador: {info[4]}")
            else:
                print("Pedido não encontrado.")
        case 4:
            print("Entregadores Disponíveis: ")
            for id, info in entregadores.items():
                if info[2] == "DISPONIVEL":
                    print(f"ID do entregador: {id}, Nome do entregador: {info[0]}, Veículo: {info[1]}, Disponibilidade: {info[2]}, ID do entregador: {info[3]}")
        case 5:
            id_entregador = input("Digite o ID do entregador para ver suas entregas: ").upper()
            print(f"Entregas realizadas pelo entregador {id_entregador}: ")
            for id, info in pedidos.items():
                if info[5] == id_entregador:
                    print(f"ID do pedido: {id}, Nome do cliente: {info[0]}, Endereço: {info[1]}, Prioridade: {info[2]}, Descrição do produto: {info[3]}, ID do entregador: {info[4]}")
            
def relatoriosOperacionais(pedidos, entregadores):
    menuRelatorio = 1 

    while menuRelatorio == 1: 
        print("\n--- Relatórios Operacionais ---")
        print("1 - Total de Pedidos")
        print("2 - Quantidade de pedidos por status")
        print("3 - Pedidos com mais prioridade")
        print("4 - Entregador com maior número de entregas")

        print("5 - Voltar ao menu principal\n")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1: 
            total = 0 
            for id in pedidos: 
                total = total + 1
            print(f"\n\tTotal de pedidos cadastrados no sistema: {total}\n")

        elif opcao == 2: 
            pendente = 0 
            emRota = 0
            entregue = 0 
            cancelado = 0 

            for id in pedidos: 
                status = pedidos[id][4]
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

            for id in pedidos: 
                if pedidos[id][2] == "ALTA": 
                    listaAlta.append(id)

            if listaAlta == []: 
                print("\n\tNenhum pedido com prioridade ALTA.")
            else: 
                print(f"\n--- Pedidos com prioridade ALTA({len(listaAlta)}) ---")

                for id in listaAlta: 
                    info = pedidos[id]
                    print(f"ID: {id} | Cliente: {info[0]}  |  Status: {info[4]}  |  Entregador: {info[5]}")
                print()

        elif opcao == 4:
            if entregadores == {}:
                print("Nenhum entregador cadastrado no sistema")
            else: 
                contagemEntregas = {}

                for idEntregador in entregadores: 
                    contagemEntregas[idEntregador] = 0

                for idPedido in pedidos: 
                    if pedidos[idPedido][4] == "Entregue": 
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
                    print("Nenhuma entrega concluída até o momento")
                else: 
                    nomeEntregador = entregadores[melhorEntregador][0]
                    print("\n--- Entregador Destaque ---")
                    print(f"ID  : {melhorEntregador}")
                    print(f"Nome    : {nomeEntregador}")
                    print(f"Entregas    : {maiorNumero}")

        elif opcao == 5: 
            menuRelatorio = 0 

        else: 
            print("\n\t[ERRO] Opção Inválida. Tente Novamente.")

print("\n\n----------Bem-vindo ao sistema de gerenciamento de entregas da Fluxo Norte!----------\n\n")
while rodando != 0:
    print("-" * 20 + " MENU " + "-" * 20 + "\n\n")
    print("1 - Cadastro de pedidos")
    print("2 - Cadastro de Entregadores")
    print("3 - Atualização dos pedidos")
    print("4 - Consulta de informações")
    print("5 - Relatórios operacionais")
    print("6 - Finalizar o sistema\n")
    opcao = int(input("Digite a opção desejada: "))
    match(opcao):
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

print(pedidos)
print(entregadores)