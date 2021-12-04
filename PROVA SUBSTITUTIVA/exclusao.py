# 1. Observe os dois métodos de exclusão listados abaixo.
#
# 2. Identifique a quais estruturas pertencem os métodos, respectivamente.
#    RESPOSTA ~> Os métodos pertencem, respectivamente, às estruturas
#                DoublyLinkedList e LinkedList.
#
# 3. Explique qual a diferença FUNDAMENTAL entre os dois métodos.
#    RESPOSTA ~> A presença do ponteiro "prev" em DoublyLinkedList evita que
#                seja necessário percorrer quase toda a estrutura (linha 43)
#                para excluir o último nodo, como acontece em LinkedList. 

# Método 1
def remove(self, pos):
    if self.is_empty() or pos < 0 or pos > self.__count - 1: return None
    if pos == 0:
        removed = self.__head
        self.__head = removed.next
        if self.__head is not None: self.__head.prev = None
        if self.__count == 1: self.__tail = None
    elif pos == self.__count - 1:
        removed = self.__tail
        self.__tail = removed.prev
        if self.__tail is not None: self.__tail.next = None
        if self.__count == 1: self.__head = None
    else:
        removed = self.__find_node(pos)
        before = removed.prev 
        after = removed.next
        before.next = after
        after.prev = before
    self.__count -= 1
    return removed.data


# Método 2
def remove(self, pos):
    if self.__count == 0 or pos < 0 or pos > self.__count - 1: return None
    if pos == 0:
        removed = self.__head
        self.__head = self.__head.next
    else:
        before = self.__head
        for i in range(1, pos): before = before.next
        removed = before.next
        after = removed.next
        before.next = after
        if removed == self.__tail:
            self.__tail = before
    self.__count -= 1
    return removed.data