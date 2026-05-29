pedidos = {}
entregadores = {}
rodando = 1

def cadastrarPedido (pedido):
    id = input("Insira um ID: ")
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

    pedido[id] = [nome, endereco, prioridade, descricao, idEntregador]
    
    
    return pedido
    
def cadastrarEntregadores (entregadores):
    idEntregador = input("Insira um id para o Entregador: ")
    entregador_nome = input("Insira o nome do Entregador: ")
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

    entregadores[id] =  [entregador_nome, veiculo, disponibilidade, idEntregador]

    return entregadores

print("\n\n----------Bem-vindo ao sistema de gerenciamento de entregas da Fluxo Norte!----------\n\n")
print("Digite a opção desejada: \n\n1 - Cadastro de pedidos \n2 - Cadastro de Entregadores \n3 - Atualização dos pedidos \n4 - Consulta de informações \n5 - Relatórios operacionais \n6 - Finalizar o sistema\n\n")
opcao = int(input("Digite a opção desejada: "))

while rodando != 0:
    match(opcao):
        case 1:
            cadastrarPedido(pedidos)
        case 2:
            cadastrarEntregadores(entregadores)
    rodando = 0

    print("\n\n1 - Cadastro de pedidos \n2 - Cadastro de Entregadores \n3 - Atualização dos pedidos \n4 - Consulta de informações \n5 - Relatórios operacionais \n6 - Finalizar o sistema\n\n")
    opcao = int(input("Quer continuar?\n\nDigite a opção desejada: "))

print(pedidos)
        
