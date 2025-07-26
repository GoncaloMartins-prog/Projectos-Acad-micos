#a) stock ilimitado  em b) e c) stock limitado
#preçário de uma loja (produto, custo)
def faz_precario():
    """Pede um preçario ao utilizador

    Requires: quando se pedir o custo ser dado um inteiro
    Ensures: um dicionario que eh o preçario, com as chaves sendo os
             produtos e os valores o custo
    """
    precario = {}
    qts_produtos = int(input("Quantos produtos quer por no preçário? "))
    for i in range(qts_produtos):
        produto = input("Produto: ")
        custo = int(input("Custo(€): "))
        precario[produto] = custo

    return precario

def faz_pedido():
    """Pede o pedido ao utilizador

    Requires: quando se pede a quantidade que seja dado um inteiro
    Ensures: uma lista com tuplos do tipo (produtos, quantidades)
    """
    pedido = []
    qts_produtos = int(input("Quantos produtos quer por no pedido? "))
    for e in range(qts_produtos):
        produto = input("Produto: ")
        quantidade = int(input("Quantidade: "))
        pedido.append((produto, quantidade))
    return pedido

def calcula_custo(precario, pedido):
    """Calcula o custo total do pedido

    Requires: precario seja um dicionario com as chaves sendo os
              produtos (strings) e os valores o custo (inteiros), pedido
              seja uma lista com
              tuplos do tipo (produtos, quantidades), com os produtos sendo
              strings e as quantidades inteiros, e todos os produtos
              do pedido estejam no precario
    Ensures: um int que represente o custo total do pedido de acordo com
             os valores do precario

    """
    custo_total = 0
    for i in range(len(pedido)):
        produto = pedido[i][0] 
                        #quantidade * custo
        custo_total += pedido[i][1] * precario[produto]
    return custo_total

precario_m = faz_precario()
print(precario_m)
pedido_m = faz_pedido()
print(pedido_m)
print(calcula_custo(precario_m, pedido_m))
