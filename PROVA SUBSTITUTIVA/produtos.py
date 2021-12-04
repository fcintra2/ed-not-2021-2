# 1. Observe a lista de produtos abaixo.
#
# 2. Utilizando os recursos estudados durante o semestre, faça o necessário para
#    que seja possível efetuar uma busca binária na lista.
#
# 3. Por meio da busca binária, informe as posições dos seguintes itens:
#    - Laranja: 23
#    - Bolacha: -1
#    - Iogurte: 22
#    - Leite condensado: -1
#    - Pimenta do reino: 33

produtos = [
    'Farinha de trigo',
    'Arroz',
    'Macarrão',
    'Extrato de tomate',
    'Azeite de oliva',
    'Feijão',
    'Leite',
    'Ovos',
    'Iogurte',
    'Achocolatado',
    'Palmito',
    'Creme de leite',
    'Biscoito',
    'Pão de forma',
    'Margarina',
    'Alface',
    'Tomate',
    'Batata',
    'Frango',
    'Carne moída',
    'Café',
    'Alho',
    'Cebola',
    'Milho de pipoca',
    'Sal',
    'Açúcar',
    'Pimenta do reino',
    'Farinha de mandioca',
    'Fubá',
    'Queijo ralado',
    'Goiabada',
    'Sardinha',
    'Suco de uva',
    'Gelatina',
    'Maçã',
    'Banana',
    'Laranja',
    'Melancia',
    'Manga',
    'Cenoura'
]

# A busca binária exige que a lista a ser pesquisada esteja ORDENADA. Era
# esperado que o aluno percebesse a necessidade de importar algum dos algoritmos
# de ordenação ANTES de fazer a busca binária.

#######################################################################

def quick_sort(lista, ini = 0, fim = None):
    """
        Função que implementa o algoritmo Quick Sort de forma ITERATIVA
    """

    if fim is None: fim = len(lista) - 1

    # Cria uma lista auxiliar
    tamanho = fim - ini + 1
    aux = [None] * tamanho
  
    # Inicializa a posição da lista auxiliar
    pos = -1
  
    # Coloca os valores iniciais de ini e fim na lista auxiliar
    pos = pos + 1
    aux[pos] = ini
    pos = pos + 1
    aux[pos] = fim
  
    # Continua retirando valores da lista auxiliar enquanto
    # ela não estiver vazia
    while pos >= 0:

        # print(aux)
  
        # Retira fim e início
        fim = aux[pos]
        pos = pos - 1
        ini = aux[pos]
        pos = pos - 1
  
        # Coloca o pivô em sua posição correta na lista ordenada
        i = ini - 1
        x = lista[fim]
    
        for j in range(ini , fim):
            if lista[j] <= x:
                # Incrementa a posição do menor elemento
                i = i + 1
                lista[i], lista[j] = lista[j], lista[i]
    
        lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
        
        pivot = i + 1
  
        # Se há elementos à esquerda do pivô, coloca-os
        # no lado esquerdo da lista auxiliar
        if pivot - 1 > ini:
            pos = pos + 1
            aux[pos] = ini
            pos = pos + 1
            aux[pos] = pivot - 1
  
        # Se há elementos à direita do pivô, coloca-os
        # no lado direito da lista auxiliar
        if pivot + 1 < fim:
            pos = pos + 1
            aux[pos] = pivot + 1
            pos = pos + 1
            aux[pos] = fim

########################################################################

def busca_binaria(lista, valor_busca):
    """
        Função que implementa o algoritmo de busca binária

        Retorna a posição onde valor_busca foi encontrado ou
        o valor convencional -1 se valor_busca não existir na lista
    """
    global comps    # Indica que estamos usando a variável declarada na linha 13
    comps = 0

    ini = 0                 # Primeira posição
    fim = len(lista) - 1    # Última posição

    while ini <= fim:
        meio = (ini + fim) // 2     # Operador // é divisão inteira

        # 1º caso: lista[meio] é igual a valor_busca
        if lista[meio] == valor_busca:  # ENCONTROU!
            comps += 1
            return meio     # meio é a posição onde valor_busca está na lista

        # 2º caso: valor_busca é menor que lista[meio]
        elif valor_busca < lista[meio]:
            comps += 2
            fim = meio - 1  # Descarta a 2ª metade da lista

        # 3º caso: valor_busca é maior que lista[meio]
        else:
            comps += 2
            ini = meio + 1  # Descarta a 1ª metade da lista

    # 4º caso: valor_busca não encontrado na lista
    return -1

#############################################################################

# Primeiramente, ordena a lista de produtos usando Quick Sort
quick_sort(produtos)

# Agora, podemos efetuar as buscas binárias
# 3. Por meio da busca binária, informe as posições dos seguintes itens:
#    - Laranja
#    - Bolacha
#    - Iogurte
#    - Leite condensado
#    - Pimenta do reino

print('Laranja:', busca_binaria(produtos, 'Laranja'))
print('Bolacha:', busca_binaria(produtos, 'Bolacha'))
print('Iogurte:', busca_binaria(produtos, 'Iogurte'))
print('Leite condensado:', busca_binaria(produtos, 'Leite condensado'))
print('Pimenta do reino:', busca_binaria(produtos, 'Pimenta do reino'))