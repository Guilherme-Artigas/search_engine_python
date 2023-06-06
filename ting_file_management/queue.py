from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""

    def __len__(self):
        """Aqui irá sua implementação"""

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        # 1.1 - Será validado que o método enqueue deve adicionar um elemento
        # à fila, modificando seu tamanho

    def dequeue(self):
        """Aqui irá sua implementação"""

        # 1.2 - Será validado que o método dequeue deve remover o elemento a
        # mais tempo na fila, modificando seu tamanho

    def search(self, index):
        """Aqui irá sua implementação"""

        # 1.3 - Será validado que o método search deve retornar um valor da
        # fila a partir de um índice válido

        # 1.4 - Será validado que o método search deve lançar a exceção
        # IndexError com a mensagem correspondente quando o índice passado for
        # inválido.
