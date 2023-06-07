from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    lista_linhas = txt_importer(path_file)
    report_dict = {}

    report_dict["nome_do_arquivo"] = path_file
    report_dict["qtd_linhas"] = len(lista_linhas)
    report_dict["linhas_do_arquivo"] = lista_linhas

    if instance.__len__() == 0:
        instance.enqueue(report_dict)
        print(report_dict, file=sys.stdout)

    for i in range(0, instance.__len__()):
        file = instance.search(i)
        if path_file != file["nome_do_arquivo"]:
            instance.enqueue(report_dict)
            print(report_dict, file=sys.stdout)


def remove(instance):
    if instance.__len__() == 0:
        return print("Não há elementos", file=sys.stdout)

    file = instance.dequeue()
    path_file = file["nome_do_arquivo"]

    return print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    # .1 - Será validado que ao executar a função file_metadata com sucesso
    # deverá exibir a mensagem correta via stdout

    # 5.2 - Será validado que ao executar a função file_metadata com posição
    # inválida deverá exibir a mensagem correta via stderr
