secao = {
    "CERÂMICAS": [("TELHAS", 7), ("TIJOLOS", 6)],
    "FLORESTAL": [("MADEIRA", 2), ("TABUAS", 12)],
    "CONSTRUÇÃO": [
        ("ACO", 1), ("VIGA", 10), ("BRITA", 11),
        ("CONCRETO", 13), ("FERRO", 9), ("AREIA", 14), ("CIMENTO", 15)
    ],
    "OUTROS": [
        ("VIDRO", 4), ("ISOLAMENTOS", 8), ("ARGAMASSA", 5), ("GESSO", 3)
    ]
}

def print_section(titulo, items):
    maximo = max(len(titulo), max(len(item[0]) + len(str(item[1])) + 11 for item in items))
    print("-" * maximo)
    print(titulo.center(maximo))
    print("-" * maximo)
    for item, code in items:
        print(f"{item} - codigo {code}")
    print("-" * maximo)

for secao, items in secao.items():
    print_section(f"SEÇÃO {secao}", items)
    print()#adiciona linha em branco
    print()