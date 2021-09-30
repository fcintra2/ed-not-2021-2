"""
    1) Identifique o algoritmo abaixo.
        RESPOSTA: algoritmo de ordenação Bubble Sort.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
        m -> função bubble_sort()
        n -> lista a ser ordenada
        o -> indicador de ocorrência de trocas
        p -> contador do for que percorre até a penúltima posição
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
        RESPOSTA: na linha do for, o range deve verificar o comprimento da lista
        (n) e não da variável indicadora de trocas (o).
"""

def m(n):
    while 1 > 0:
        o = False
        # for p in range(len(o) - 1):
        for p in range(len(n) - 1):
            if n[p + 1] < n[p]:
                n[p + 1], n[p] = n[p], n[p + 1]
                o = True
        if not o: break