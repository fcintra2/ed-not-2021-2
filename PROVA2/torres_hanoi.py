# 1. Veja, na imagem "torres-hanoi.png", como funciona o jogo das Torres de Hanoi.
#
# 2. Cada uma das torres do jogo se comporta como uma pilha. Importe a classe
#    apropriada e crie três pilhas, representando as três torres.

from lib.stack import Stack

torre_a = Stack()
torre_b = Stack()
torre_c = Stack()

# 3. Use os valores 1, 2 e 3 para representar os discos. Empilhe-os na primeira
#    torre.

torre_a.push(3)
torre_a.push(2)
torre_a.push(1)

print('--- ANTES ---')
print('Torre A:', torre_a.to_str())
print('Torre B:', torre_b.to_str())
print('Torre C:', torre_c.to_str())

# 4. Desempilhe um dos discos da primeira torre e empilhe-o na segunda.

torre_b.push(torre_a.pop())

# 5. Desempilhe o disco remanescente da primeira torre e coloque-o na terceira.

torre_c.push(torre_a.pop())

# 6. Desempilhe o disco da terceira torre e coloque-o sobre o disco da segunda torre.

torre_b.push(torre_c.pop())

# 7. Desempilhe o disco da primeira torre e coloque-o na terceira torre.

torre_c.push(torre_a.pop())

# 8. Desempilhe um dos discos da segunda torre e coloque-o na primeira torre.

torre_a.push(torre_b.pop())

# 9. Desempilhe o disco da primeira torre e coloque-o sobre o disco da terceira torre.

torre_c.push(torre_a.pop())

# 10.Finalmente, desempilhe o disco da segunda torre e coloque-o na terceira torre.

torre_c.push(torre_b.pop())

# 11.Use o método to_str() para exibir as três pilhas. As duas primeiras devem estar
#    vazias e a terceira deve conter os três discos, na ordem (3 na base, 1 no topo).

print('--- ANTES ---')
print('Torre A:', torre_a.to_str())
print('Torre B:', torre_b.to_str())
print('Torre C:', torre_c.to_str())