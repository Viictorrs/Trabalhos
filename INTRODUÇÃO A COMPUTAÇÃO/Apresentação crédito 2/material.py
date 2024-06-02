import json

almoxarifadoPath = "almoxarifado.json"

def main():
    try:
        with open(almoxarifadoPath, "r") as file:
            almoxarifado = json.load(file)
        print("Almoxarifado carregado com sucesso!")
    except FileNotFoundError:
        almoxarifado = {
            'Aco': 1000, 
            'Madeira': 300,
            'Gesso': 175,
            'Vidro': 167,
            'Argamassa': 350,
            'Tijolos': 3000,
            'Telhas': 2500, 
            'Isolamentos': 100,
            'Ferro': 1500,
            'Viga': 250,
            'Brita': 250,   
            'Tabua': 100,  
            'Concreto': 200, 
            'Areia': 300, 
            'Cimento': 500
        }
        
        with open(almoxarifadoPath, "w") as file:
            json.dump(almoxarifado, file)
        print("Almoxarifado criado com sucesso!")

def atualizarAlmoxarifado(item: str, quantidade: int) -> bool:
    almoxarifado = getAlmoxarifado()
    
    if item in almoxarifado and almoxarifado[item] >= quantidade:
        almoxarifado[item] -= quantidade
        
        # Verifica se a quantidade está abaixo de 30% do valor inicial
        if almoxarifado[item] - quantidade  < 0.3 * almoxarifado[item]:
            print(f"Atenção: estoque de {item} abaixo de 30% do total. Reposição recomendada.")
        
        with open(almoxarifadoPath, "w") as file:
            json.dump(almoxarifado, file)
        
        print("Almoxarifado atualizado!")
        return True
    else:
        print(f"Quantidade insuficiente de {item} no almoxarifado.")
        return False

def getAlmoxarifado() -> dict:
    with open(almoxarifadoPath, "r") as file:
        almoxarifado = json.load(file)

    return almoxarifado

if __name__ == "material":
    main()