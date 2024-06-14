import json

almoxarifadoPath = "almoxarifado.json"

def main():
    try:
        with open(almoxarifadoPath, "r") as file:
            almoxarifado = json.load(file)
        print("Almoxarifado carregado com sucesso!")
    except FileNotFoundError:
        almoxarifado = {
            '1': {
                "nome": "aco", 
                "preco": 8.99,
                "quantidade": 1000,
                "secao": "CONSTRUCAO",
                "peso": 7.4  # peso em Kg
            }, 
            '2': {
                "nome": "madeira",
                "preco": 12.99,
                "quantidade": 300,
                "secao": "FLORESTAL",
                "peso": 5 # peso em kg/m2
            },
            '3': {
                "nome": "gesso",
                "preco": 31.99,
                "quantidade": 300,
                "secao": "OUTROS",
                "peso": 40  # peso em kg
            },
            '4': {
                "nome": "vidro",
                "preco": 49.99,
                "quantidade": 300,
                "secao": "OUTROS",
                "peso": 10  # peso em kg/m2
            },
            '5': {
                "nome": "argamassa",
                "preco": 14.99,
                "quantidade": 350,
                "secao": "OUTROS",
                "peso": 20  # peso em kg
            },
            '6': {
                "nome": "tijolos",
                "preco": 1.28,
                "quantidade": 3000,
                "secao": "CERAMICAS",
                "peso": 2.2  # peso em kg
            },
            '7': {
                "nome": "telhas",
                "preco": 1.23,
                "quantidade": 2500,
                "secao": "CERAMICAS",
                "peso": 2.4  # peso unitário em kg
            }, 
            '8': {
                "nome": "isolamentos",
                "preco": 17.78,
                "quantidade": 100,
                "secao": "OUTROS",
                "peso": 0.5  # peso em kg/m2
            },
            '9': {
                "nome": "ferro",
                "preco": 25.96,
                "quantidade": 1500,
                "secao": "CONSTRUCAO",
                "peso": 7.5 # peso em kg
            },
            '10': {
                "nome": "viga",
                "preco": 755.24,
                "quantidade": 250,
                "secao": "CONSTRUCAO",
                "peso": 15  # peso em kg/m2
            },
            '11': {
                "nome": "brita",
                "preco": 32,
                "quantidade": 250,
                "secao": "CONSTRUCAO",
                "peso": 1360  # peso em kg/m3
            },   
            '12': {
                "nome": "tabua",
                "preco": 33.65,
                "quantidade": 100,
                "secao": "FLORESTAL",
                "peso": 20  # peso em kg
            },  
            '13': {
                "nome": "concreto",
                "preco": 350,
                "quantidade": 200,
                "secao": "CONSTRUCAO",
                "peso": 8.7  # peso em kg/m3
            }, 
            '14': {
                "nome": "Areia",
                "preco": 34,
                "quantidade": 300,
                "secao": "CONSTRUCAO",
                "peso": 1500  # peso em kg/m3
            }, 
            '15': {
                "nome": "Cimento",
                "preco": 36.29,
                "quantidade": 500,
                "secao": "CONSTRUCAO",
                "peso": 50  # peso em kg
            }
        }
        
        with open(almoxarifadoPath, "w") as file:
            json.dump(almoxarifado, file)
        print("Almoxarifado criado com sucesso!")

def atualizarAlmoxarifado(item: str, quantidade: int) -> bool:
    almoxarifado = getAlmoxarifado()
    
    if item in almoxarifado and almoxarifado[item].get("quantidade") >= quantidade:
        almoxarifado[item]["quantidade"] -= quantidade
        produto_nome = almoxarifado[item]["nome"]
        
        # Verifica se a quantidade está abaixo de 30% do valor inicial
        if almoxarifado.get(item).get("quantidade") - quantidade< 0.3 * almoxarifado.get(item).get("quantidade"):
            print("-"*80)
            print(f"Atenção: estoque de {produto_nome} abaixo de 30% do total. Reposição recomendada.")
            print("-"*80)
        
        with open(almoxarifadoPath, "w") as file:
            json.dump(almoxarifado, file)
        
        print("Almoxarifado atualizado!")
        return True
    else:
        print(f"Quantidade insuficiente de {item} no almoxarifado.")
        return False

def adicionarMaterial(codigo, secao, nome, quantidade, preco, peso):
    almoxarifado = getAlmoxarifado()

    almoxarifado[codigo] = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco,
        "secao": secao,
        "peso": peso
    }
    
    with open(almoxarifadoPath, "w") as file:
        json.dump(almoxarifado, file)
    
    print("Item adicionado com sucesso")

def removerProduto(codigo: str):
    almoxarifado = getAlmoxarifado()

    almoxarifado.pop(codigo)

    with open(almoxarifadoPath, "w") as file:
        json.dump(almoxarifado, file)
    
    print("Item removido com sucesso")

def getAlmoxarifado() -> dict:
    with open(almoxarifadoPath, "r") as file:
        almoxarifado = json.load(file)

    return almoxarifado

if __name__ == "material":
    main()