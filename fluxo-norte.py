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
    id = f"{randint(0, 9999):04d}"
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
    for idPedido, dados in pedidos.items():
        if (dados[4] == "PENDENTE" and dados[5] == id):
            idPedidos.append(idPedido)
    
    entregadores[id] = [nome, veiculo, disponibilidade, idPedidos]
    return entregadores

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
            id_pedido = input("Digite o ID do pedido que deseja buscar: ")
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
            id_entregador = input("Digite o ID do entregador para ver suas entregas")
            print(f"Entregas realizadas pelo entregador {id_entregador}: ")
            for id, info in pedidos.items():
                if info[4] == id_entregador:
                    print(f"ID do pedido: {id}, Nome do cliente: {info[0]}, Endereço: {info[1]}, Prioridade: {info[2]}, Descrição do produto: {info[3]}, ID do entregador: {info[4]}")
            

print("\n\n----------Bem-vindo ao sistema de gerenciamento de entregas da Fluxo Norte!----------\n\n")

while rodando != 0:
    print("\tMENU\n\n1 - Cadastro de pedidos \n2 - Cadastro de Entregadores \n3 - Atualização dos pedidos \n4 - Consulta de informações \n5 - Relatórios operacionais \n6 - Finalizar o sistema\n\n")
    opcao = int(input("Digite a opção desejada: "))
    match(opcao):
        case 1:
            cadastrarPedido(pedidos)
        case 2:
            cadastrarEntregadores(pedidos, entregadores)
        case 3:
            atualizarPedidos(pedidos)
        case 4:
            consultarInformacoes(pedidos, entregadores)
        case 5:
            relatoriosOperacionais(pedidos, entregadores)
        case 6:
            print("Sistema finalizado. Obrigado por usar o sistema de gerenciamento de entregas da Fluxo Norte!")
            rodando = 0

print(pedidos)
print(entregadores)
        
