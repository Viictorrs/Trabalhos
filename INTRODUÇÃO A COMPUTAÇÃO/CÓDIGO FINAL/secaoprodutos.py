import json

secaoPath = "secao.json"

def main():
    try:
        with open(secaoPath, "r") as file:
            secao = json.load(file)
        print("Secao carregada com sucesso!")
    except FileNotFoundError:
        secao = {
            "CERAMICAS": [("TELHAS", "7"), ("TIJOLOS", "6")],
            "FLORESTAL": [("MADEIRA", "2"), ("TABUAS", "12")],
            "CONSTRUCAO": [
                ("ACO", "1"), ("VIGA", "10"), ("BRITA", "11"),
                ("CONCRETO", "13"), ("FERRO", "9"), ("AREIA", "14"), ("CIMENTO", "15")
            ],
            "OUTROS": [
                ("VIDRO", "4"), ("ISOLAMENTOS", "8"), ("ARGAMASSA", "5"), ("GESSO", "3")
            ]
        }
        
        with open(secaoPath, "w") as file:
            json.dump(secao, file)
        print("Secões criada com sucesso!")

def print_section(titulo, items):
    maximo = max(len(titulo), max(len(item[0]) + len(str(item[1])) + 11 for item in items))
    print("-" * maximo)
    print(titulo.center(maximo))
    print("-" * maximo)
    for item, code in items:
        print(f"{item} - codigo {code}")
    print("-" * maximo)

def getSecoes() -> dict:
    with open(secaoPath, "r") as file:
        secao = json.load(file)
    
    return secao

def adicionarItem(secao, codigo, nome):
    secoes = getSecoes()

    secoes[secao].append((nome, codigo))
    
    with open(secaoPath, "w") as file:
        json.dump(secoes, file)
    
    print("Item adicionado com sucesso")

def removerItem(nomeSecao, codigo):
    secao = getSecoes()

    c = 0
    while c < len(secao.get(nomeSecao)):
        if secao[nomeSecao][c][1] == codigo:
            secao[nomeSecao].pop(c)
            break
        c += 1
    
    with open(secaoPath, "w") as file:
        json.dump(secao, file)
    
    print("Removido com sucesso")

def mostrarSecao():
    with open(secaoPath, "r") as file:
        secao = json.load(file)
    for key, items in secao.items():
        print_section(f"SEÇÃO {key}", items)
        print() # adiciona linha em branco

if __name__ == "secaoprodutos":
    main()
