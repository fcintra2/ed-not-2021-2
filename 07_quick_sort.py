#   ALGORITMO DE ORDENAÇÃO QUICK SORT
    
#    Escolhe um dos elementos da lista para ser o pivô (na nossa implementação,
#    o último elemento) e, na primeira passada, divide a lista, a partir da posição
#    final da lista, em um sublista à esquerda contendo apenas valores menores que
#    o pivô e outro sublista à direita, que contém apenas valores maiores que o pivô.
#    
#    Em seguida, recursivamente, repete o processo em cada uma das sublistas até que
#    toda a lista esteja ordenado.

def quick_sort(lista, ini = 0, fim = None):
    """
        Função que implementa o algoritmo de ordenação Quick Sort
        de forma recursiva
    """