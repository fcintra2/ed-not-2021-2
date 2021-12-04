# 1. Em um escritório, há uma impressora compartilhada. No início do expediente,
#    Ariovaldo, Jucicléia, Epaminondas e Clementina enviaram a ela trabalhos de 
#    impressão.
# 
# 2. No entanto, antes que o trabalho de Ariovaldo pudesse ser impresso, Tertuliano e
#    Apolônia enviaram seus trabalhos de impressão com prioridade, para que ficassem
#    prontos antes dos impressos dos colegas.
# 
# 3. Quando 4 trabalhos de impressão já haviam sido concluídos, Clementina percebeu
#    que havia enviado o arquivo errado, e cancelou seu trabalho de impressão.
# 
# 4. Enquanto a impressora ainda processava os pedidos, ela recebeu mais dois pedidos:
#    o de Constança, sem prioridade, e o de Zenóbio, com prioridade.
# 
# 5. Utilize a estrutura de dados apropriada para representar a situação relatada. 

# A situação relatada requer o uso da estrutura Deque
from lib.deque import Deque

fila_impressao = Deque()

# 1
fila_impressao.insert_back('Ariovaldo')
fila_impressao.insert_back('Jucicléia')
fila_impressao.insert_back('Epaminondas')
fila_impressao.insert_back('Clementina')

# 2
fila_impressao.insert_front('Tertuliano')
fila_impressao.insert_front('Apolônia')

# 3
fila.remove_front() # 4 trabalhos concluídos
fila.remove_front()
fila.remove_front()
fila.remove_front()

fila.remove_back()  # Clementina desiste

# 4
fila_impressao.insert_back('Constança')
fila_impressao.insert_front('Zenóbio')