class ListaDeMateriais:
    def __init__(self):
        self.materiais = {
            1: 'Aço',
            2: 'Madeira',
            3: 'Gesso',
            4: 'Vidro',
            5: 'Argamassa',
            6: 'Tijolos',
            7: 'Telhas',
            8: 'Isolamentos',
            9: 'Ferro',
            10: 'Viga',
            11: 'Brita',
            12: 'Tábua',
            13: 'Concreto',
            14: 'Areia',
            15: 'Cimento'
        }

    def obter_material(self, codigo: int) -> str:
        return self.materiais.get(codigo, "CÓDIGO INVÁLIDO!")

def lista_de_materiais():
    lista = ListaDeMateriais()
    try:
        codigo = int(input("Digite o código do produto: "))
        material = lista.obter_material(codigo)
        print(f'Item selecionado: {material}')
        return codigo
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")
        return "Entrada inválida!"

# Exemplo de uso
if __name__ == "material":
    lista_de_materiais()