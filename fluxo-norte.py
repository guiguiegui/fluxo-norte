from random import choice, randint
from string import ascii_uppercase



pedidos = {}
entregadores = {}
rodando = 1

def cadastrarPedido (pedido):
    letra = choice(ascii_uppercase)
    numeros = f"{randint(0, 9999):04d}"
    id = letra + numeros
    nome = input("Insira o nome do cliente: ")
    endereco = input("Insira o endereço: ")
    print("NÍVEIS DE PRIORIDADE\n\tDigite 1 para PRIORIDADE ALTA\n\tDigite 2 para PRIORIDADE NORMAL")
    prioridade = int(input("Escolha o nível da prioridade: "))
    match(prioridade):
        case 1:
            prioridade = "Alta"
        case 2:
            prioridade = "Normal"
        case _:
            prioridade = "Normal"
    descricao = input("Digite a descrição do produto: ")
    print("TIPOS DE STATUS\n\tDigite 1 para status PENDENTE\n\tDigite 2 para status EM ROTA\n\tDigite 3 para status ENTREGUE\n\tDigite 4 para status CANCELADO")
    status = int(input("Informe o status do pedido: "))
    match(status):
        case 1:
            status = "Pendente"
        case 2:
            status = "Em Rota"
        case 3:
            status = "Entregue"
        case 4:
            status = "Cancelado"
        case _:
            status = "Pendente"
    idEntregador = int(input("Informe o ID do entregador: "))

    pedido[id] = [nome, endereco, prioridade, descricao, status, idEntregador]
    
    
    return pedido
    
def cadastrarEntregadores (pedidos, entregadores):
    id = f"{randint(0, 9999):04d}"
    nome = input("Insira o nome do Entregador: ")
    veiculo = int(input("Escolha o veiculo do entregador, 1 para Carro, 2 para moto, 3 para Van: "))
    match(veiculo):
        case 1:
            veiculo = "Carro"
        case 2:
            veiculo = "Moto"
        case 3:
            veiculo = "Van"   
    disponibilidade = input("Mostre a disponibilidade do entregador, 1 para disponivel, 2 para indisponivel: ")
    match(disponibilidade):
        case 1:
            disponibilidade = "Disponivel"
        case 2:
            disponibilidade = "Indisponivel"
    idPedidos = []
    if pedidos[6] == id and pedidos[5] == "Pendente":
        idPedidos = pedidos[id]
        entregadores[id] =  [nome, veiculo, idPedidos, disponibilidade]

    return entregadores

def consultarInformacoes(pedidos, entregadores):
    print("Consulta de informações")
    print("\n1 - Pedidos Entregues\n2 - Pedidos Entregues\n3 - Buscar por pedido\n4 - Entregador disponivel\n5 - Todas as entregas realizadas por um entregador\n6 - Voltar para o menu principal\n\n")
    opcao = int(input("Digite a opção desejada: "))
    match(opcao):
        case 1:
            print("Pedidos Entregues: ")
            for id, info in pedidos.items():
                if info[4] == "Entregue":
                    print(f"ID do pedido: {id}, Nome do cliente: {info[0]}, Endereço: {info[1]}, Prioridade: {info[2]}, Descrição do produto: {info[3]}, ID do entregador: {info[4]}")
        case 2:
            print("Pedidos Pendentes: ")
            for id, info in pedidos.items():
                if info[4] == "Pendente":
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
                if info[2] == "Disponivel":
                    print(f"ID do entregador: {id}, Nome do entregador: {info[0]}, Veículo: {info[1]}, Disponibilidade: {info[2]}, ID do entregador: {info[3]}")
        case 5:
            id_entregador = input("Digite o ID do entregador para ver suas entregas")
            print(f"Entregas realizadas pelo entregador {id_entregador}: ")
            for id, info in pedidos.items():
                if info[4] == id_entregador:
                    print(f"ID do pedido: {id}, Nome do cliente: {info[0]}, Endereço: {info[1]}, Prioridade: {info[2]}, Descrição do produto: {info[3]}, ID do entregador: {info[4]}")
            

print("\n\n----------Bem-vindo ao sistema de gerenciamento de entregas da Fluxo Norte!----------\n\n")
print("Digite a opção desejada:\n\n1 - Cadastro de pedidos \n2 - Cadastro de Entregadores \n3 - Atualização dos pedidos \n4 - Consulta de informações \n5 - Relatórios operacionais \n6 - Finalizar o sistema\n\n")
opcao = int(input("Digite a opção desejada: "))

while rodando != 0:
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

    print("\n1 - Cadastro de pedidos \n2 - Cadastro de Entregadores \n3 - Atualização dos pedidos \n4 - Consulta de informações \n5 - Relatórios operacionais \n6 - Finalizar o sistema\n\n")
    opcao = int(input("Quer continuar?\nDigite a opção desejada: "))

print(pedidos)
        
