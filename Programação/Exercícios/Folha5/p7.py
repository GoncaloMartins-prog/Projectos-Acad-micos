from p4 import unidades
import p5
import p6
#ou soh import p4 e dps quando se usa a funçao: p4.unidades()
def eh_capicua_c_string(num):
    """Verifica se num eh uma capicua

    Requires: num seja um numero inteiro positivo
    Ensures: devolve True se num for uma capicua,
            False caso contrário
    """
    capicua = True
    numero = str(num)
    #0, -1
    #1, -2
    #2, -3
    #a, b
    for i in range(len(str(num))//2):
        index_a = i
        index_b = -(i+1)
        if numero[index_a] != numero[index_b]:
            capicua = False
    
    return capicua
def eh_capicua_c_int(num):
    """
    """
    num_alterado = num
    num_final = 0
    while (num_alterado > 0):
        u = unidades(num_alterado)
        num_final = p6.aumenta(num_final) + u
        num_alterado = p5.retira(num_alterado)
    return num == num_final
    
n = int(input("Numero inteiro >0: "))
print(eh_capicua_c_int(n))
