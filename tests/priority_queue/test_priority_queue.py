from ting_file_management.priority_queue import PriorityQueue
from ting_file_management.file_process import process
import pytest


def test_basic_priority_queueing():
    container = PriorityQueue()
    process("statics/novo_paradigma_globalizado.txt", container)
    process("statics/nome_pedro.txt", container)
    process("statics/novo_paradigma_globalizado-min.txt", container)
    process("statics/arquivo_teste.txt", container)

    assert len(container.high_priority) == 2
    assert len(container.regular_priority) == 2

    container.dequeue()

    file_one = container.search(0)
    assert file_one["nome_do_arquivo"] == "statics/arquivo_teste.txt"

    with pytest.raises(IndexError):
        container.search(10)
