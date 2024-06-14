import material as m

class ListaDeMateriais:
    def __init__(self):
        self.materiais = m.getAlmoxarifado()

    def obter_material(self, codigo) -> str:
        return self.materiais.get(codigo, "CÓDIGO INVÁLIDO!")

def lista_de_materiais():
    lista = ListaDeMateriais()
    try:
        codigo = input("Digite o código do produto: ")
        material = lista.obter_material(codigo)
        print(f'Item selecionado: {material["nome"]}')
        return codigo
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")
        return "Entrada inválida!"

# Exemplo de uso
if __name__ == "material":
    lista_de_materiais()