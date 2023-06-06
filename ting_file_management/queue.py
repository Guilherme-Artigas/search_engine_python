from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._queue = list()
        self._tamanho = 0

    def __len__(self):
        return self._tamanho

    def enqueue(self, value):
        self._queue.append(value)
        self._tamanho += 1

    def dequeue(self):
        index = self._queue.pop(0)
        self._tamanho -= 1
        return index

    def search(self, index):
        if index < 0 or index > self._tamanho - 1:
            raise IndexError("Índice Inválido ou Inexistente")
        try:
            return self._queue[index]
        except Exception:
            raise IndexError("Índice Inválido ou Inexistente")
