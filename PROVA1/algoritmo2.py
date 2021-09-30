"""
    1) Identifique o algoritmo abaixo.
       RESPOSTA: algoritmo de busca binária.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
        m -> função busca_binaria()
        n -> lista em que será feita a busca
        o -> valor de busca
        p -> posição inicial
        q -> posição final
        r -> meio calculado do vetor  
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
        RESPOSTA: na linha de cálculo do meio do vetor, estavam sendo somadas
        as variáveis erradas (n + o). Além disso, a divisão feita não retornava
        um valor inteiro.
"""

def m(n, o):
    p = 0                 
    q = len(n) - 1    
    while p <= q:
        # r = (n + o) / 2
        r = (p + q) // 2   
        if n[r] == o: return r     
        elif o < n[r]: q = r - 1  
        else: p = r + 1  
    return -1