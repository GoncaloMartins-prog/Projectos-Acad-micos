def get_max(l):
    """Devolve o maior numero da lista

    Requires: l ser uma lista de inteiros
    Ensures: 
    """
    m_atual = l[0]
    for i in l:
        if m_atual < i:
            m_atual = i

    return m_atual

lista = []
n_elementos = int(input("Quantos elementos tem a lista? "))
for i in range(n_elementos):
    lista.append(int(input("Insira um elemento da lista: ")))
print(get_max(lista))
