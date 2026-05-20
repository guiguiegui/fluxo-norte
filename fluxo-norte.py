pedidos = {}
entregadores = {}

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
    
    

opcao = int(input("Digite a opção desejada: \n\n1 - Cadastro de pedidos \n2 - Cadastro de Entregadores \n3 - Atualização dos pedidos \n4 - Consulta de informações \n5 - Relatórios operacionais \n6 - Finalizar o sistema\n\n"))

match(opcao):
    case 1:
        cadastrarPedido(pedidos)


print(pedidos)
        
