"""
    1) Identifique o algoritmo abaixo.
       RESPOSTA: algoritmo de ordenação Quick Sort
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
        m -> função quick_sort()
        n -> vetor a ser ordenado
        o -> posição inicial do vetor
        p -> posição final do vetor
        q -> pivô
        r -> divisor
        i -> contador do loop até a penúltima posição
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
        RESPOSTA: estão faltando, na função, os parâmetros opcionais 
        correspondentes à posição inicial do vetor (o) e da posição 
        final do vetor (p), com seus respectivos valores padrão.
"""

def m(n, o = 0, p = None):
    if p is None: p = len(n) - 1
    if p <= o: return
    q = p
    r = o - 1
    for i in range(o, p):
        if n[i] < n[q]:
            r += 1
            if r != i: n[r], n[i] = n[i], n[r]
    r += 1
    if n[q] < n[r] and q != r: n[q], n[r] = n[r], n[q]
    m(n, o, r - 1)
    m(n, r + 1, p)