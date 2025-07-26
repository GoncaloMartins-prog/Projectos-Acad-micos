#a) stock ilimitado  em b) e c) stock limitado
#preçário de uma loja (produto, custo)
def faz_inventario():
    """Pede um inventario ao utilizador

    Requires: quando se pedir a quantidade ser um dado inteiro e o custo
              um dado float
    Ensures: um dicionario que eh o inventario, com as chaves sendo os
             produtos e os valores um tuplo da forma (custo, quantidade)
    """
    inventario = {}
    qts_produtos = int(input("Quantos produtos quer por no inventário? "))
    for i in range(qts_produtos):
        produto = input("Produto: ")
        custo = float(input("Custo(€): "))
        quantidade = int(input("Quantidade que tem em stock: "))
        inventario[produto] = (custo, quantidade)

    return inventario

def faz_pedido():
    """Pede o pedido ao utilizador

    Ensures: uma lista com tuplos do tipo (produtos, quantidades)
    """
    pedido = []
    qts_produtos = int(input("Quantos produtos quer por no pedido? "))
    for e in range(qts_produtos):
        produto = input("Produto: ")
        quantidade = int(input("Quantidade: "))
        pedido.append((produto, quantidade))
    return pedido

def calcula_custo(inventario, pedido):
    """Calcula o custo total do pedido e atualiza o inventario

    Requires: inventario seja um dicionario com as chaves sendo os
              produtos (strings) e os valores um tuplo de inteiros do tipo
              (custo, quantidade), pedido seja uma lista com
              tuplos do tipo (produtos, quantidades), com os produtos sendo
              strings e as quantidades inteiros, e todos os produtos
              do pedido estejam no inventario
    Ensures: um int que represente o custo total do pedido de acordo com
             os valores do inventario, se a quantidade do pedido exceder
             a quantidade do inventario vai ser assumida a quantidade total
             do inventario
             tambem atualiza o inventario de acordo com o pedido
    """
    custo_total = 0
    for i in range(len(pedido)):
        produto = pedido[i][0]
        quantidade = pedido[i][1]
        custo_um = inventario[produto][0]
        quantidade_stock = inventario[produto][1]
        
        if quantidade < quantidade_stock:
            custo_total += quantidade * custo_um
        else:
            custo_total += custo_um * quantidade_stock
        
        quantidade_nova = quantidade_stock - quantidade
        if quantidade_nova < 0:
            quantidade_nova = 0
        inventario[produto] = (custo_um, quantidade_nova)
    return custo_total
print("Faça um iventário: ")
inventario_m = faz_inventario()
print("\nFaça agora um pedido: ")
pedido_m = faz_pedido()
print("O custo dete pedido é", calcula_custo(inventario_m, pedido_m), "€.")
