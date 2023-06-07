def txt_importer(path_file):
    if not str(path_file).endswith(".txt"):
        return print("Formato inválido")

    line_list = []

    try:
        with open(path_file) as file:
            for line in file:
                line_list.append(line)
        print(line_list)
        return line_list
    except Exception:
        return print(f"Arquivo {path_file} não encontrado")

    # 2.1 - Será validado que o método txt_importer deve retornar uma lista
    # contendo as linhas do arquivo

    # 2.2 - Será validado que ao executar o método txt_importer com um arquivo
    # TXT que não exista, deve ser exibida a mensagem Arquivo {path_file} não
    # encontrado na stderr, em que {path_file} é o caminho do arquivo

    # 2.3 - Será validado que ao executar o método txt_importer com uma
    # extensão diferente de .txt, deve ser exibida a mensagem Formato inválido
    # na stderr


txt_importer("ting_file_management/teste.txt")
