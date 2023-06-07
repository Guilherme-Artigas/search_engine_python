import sys


def txt_importer(path_file):
    if not str(path_file).endswith(".txt"):
        return print("Formato inválido", file=sys.stderr)

    line_list = []

    try:
        with open(path_file) as file:
            for line in file:
                line_list.append(line.strip())
        return line_list
    except Exception:  # oi
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
