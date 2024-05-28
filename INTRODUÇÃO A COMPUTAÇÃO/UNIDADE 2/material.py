import json

almoxarifadoPath = "almoxarifado.json"

def main():
    try:
        file = open(almoxarifadoPath, "r")
        almoxarifado = json.load(file)
        print("Almoxarifado carregado com sucesso!")
    except FileNotFoundError:
        almoxarifado = {
            'Tijolos': 300,
            'Argamassa': 250,
            'Gesso':175,
            'Aco': 200, 
            'Vidro': 167,
            'Ceramica': 100,
            'Madeira': 50,
            'Concreto': 200,
            'Ferro': 150,
            'Telhas': 0,  # Sera convertido 
            'Tabua': 0,  # Sera convertido 
            'Brita': 0,  # Sera convertido 
            'Viga': 0      # Sera convertido 
        }
        
        file = open(almoxarifadoPath, "w")
        json.dump(almoxarifado, file)
        file.close()
        print("Almoxarifado criado com sucesso!")

def atualizarAlmoxarifado(item: str, quantidade: int) -> bool:
    almoxarifado = getAlmoxarifado()
    
    if almoxarifado[item] >= quantidade:
        almoxarifado[item] -= quantidade
        file = open(almoxarifadoPath, "w")
        json.dump(almoxarifado, file)
        file.close()
        print("Almoxarifado atualizado!")
        return True
    else:
        print(f"Quantidade insuficiente de {item} no almoxarifado.")
        return False

def getAlmoxarifado() -> dict:
    file = open(almoxarifadoPath, "r")
    almoxarifado = json.load(file)
    file.close()

    return almoxarifado

if __name__ == "material":
    main()
