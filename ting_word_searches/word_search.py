def exists_word(word, instance):
    occurrence_list = []
    occ = {}
    occ["palavra"] = ""
    occ["arquivo"] = ""
    occ["ocorrencias"] = []
    count = 1

    for i in range(0, instance._tamanho):
        for linha in instance._queue[i]["linhas_do_arquivo"]:
            if str(word).lower() in str(linha).lower():
                occ["palavra"] = word
                occ["arquivo"] = instance._queue[i]["nome_do_arquivo"]
                occ["ocorrencias"].append({"linha": count})
                if len(occurrence_list) == 0:
                    occurrence_list.append(occ)
            count += 1
        count = 1
    return occurrence_list


def search_by_word(word, instance):
    ...
