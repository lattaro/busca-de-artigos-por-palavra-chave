
def buscar(doc_list, keyword):
    pass
    vet = []
    for titulo in doc_list:
        x = titulo.split(maxsplit=-1)
        for palavras in x:
            palavras = palavras.rstrip('.,?')
            for unica in keyword:
                if palavras.lower() == unica.lower():
                    vet.append(doc_list.index(titulo))
    if len(vet) > 2:
        for z in vet:
            j = 1
            z = 0
            if z == vet[j]:
                j = j + 1
                z = z +1
                del vet[j]
    return vet


print(buscar(['The Learn Python Challenge Casino', 'They bought a car, and a horse', 'Casinoville?'],['python','car']))