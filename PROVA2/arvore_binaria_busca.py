# 1. Todas as questões deste arquivo referem-se à árvore binária de busca representada
#    na imagem "abb.png".
#
# 2. Caso seja necessário escrever algum código para responder às perguntas seguintes,
#    importe a classe BinarySearchTree neste arquivo e faça os testes aqui.
#
# 3. Qual a altura da subárvore à esquerda de 45?
#    RESPOSTA ~> A altura é 4 (quatro).
#
# 4. Quais níveis da árvore estão completos, isto é, já contêm o número máximo de nodos
#    permitidos?
#    RESPOSTA ~> São os níveis 0, 1, 2 e 3.
# 
# 5. Qual a profundidade do nodo de valor 51, em relação à árvore como um todo?
#    RESPOSTA ~> A altura do nodo citado é 6 (seis).
#
# 6. A árvore representada está equilibrada? Por quê? Justifique sua resposta.
#    RESPOSTA ~> Não, porque a diferença de altura entre as subárvores direita e esquerda
#                é maior que 1 (um).
#
# 7. Qual será o resultado do percurso pós-ordem após terem sido excluídos os nodos
#    de valor 3, 18, 42, 49 e 90?
#    RESPOSTA ~> 6, 0, 12, 15, 9, 33, 27, 36, 39, 24, 51, 57, 54, 63, 60, 69, 66, 81, 
#                78, 99, 96, 84, 75, 45
#
# 8. Após a exclusão dos nodos 3, 18, 42, 49 e 90, se for removido o nodo raiz (de 
#    valor 45), qual(is) nodo(s) poderia(m) ocupar o seu lugar? Justifique sua resposta.
#    RESPOSTA ~> Podem assumir a posição raiz os nodos de valor 39 (maior do lado esquerdo) ou
#                51 (menor do lado direito).

from lib.binary_search_tree import BinarySearchTree

arvore = BinarySearchTree()

arvore.insert(45)
arvore.insert(24)
arvore.insert(75)
arvore.insert(9)
arvore.insert(39)
arvore.insert(66)
arvore.insert(84)
arvore.insert(3)
arvore.insert(15)
arvore.insert(36)
arvore.insert(42)
arvore.insert(60)
arvore.insert(69)
arvore.insert(78)
arvore.insert(96)
arvore.insert(0)
arvore.insert(6)
arvore.insert(12)
arvore.insert(18)
arvore.insert(27)
arvore.insert(49)
arvore.insert(75)
arvore.insert(81)
arvore.insert(90)
arvore.insert(99)
arvore.insert(33)
arvore.insert(54)
arvore.insert(51)
arvore.insert(57)
arvore.insert(63)

percurso = []
arvore.in_order_traversal(lambda val: percurso.append(val))
print('Percurso em-ordem:', percurso)

# 3, 18, 42, 49 e 90
arvore.remove(3)
arvore.remove(18)
arvore.remove(42)
arvore.remove(49)
arvore.remove(90)

percurso = []
arvore.post_order_traversal(lambda val: percurso.append(val))
print('Percurso pós-ordem:', percurso)
