# Importando as listas de materiais do almoxarifado
import listamaterialfinal
import material

produtos_precos = {
    1: {"nome": "aço", "preco": 8.99, "almoxarifado": "Ferro"},
    2: {"nome": "madeira", "preco": 7.99, "almoxarifado": "Madeira"},
    3: {"nome": "gesso", "preco": 8.99, "almoxarifado": "Gesso"},
    4: {"nome": "vidro", "preco": 11.99, "almoxarifado": "Vidro"},
    5: {"nome": "argamassa", "preco": 7.99, "almoxarifado": "Argamassa"},
    6: {"nome": "tijolos", "preco": 5.99, "almoxarifado": "Tijolos"},
    7: {"nome": "telhas", "preco": 9.99, "almoxarifado": "Telhas"},
    8: {"nome": "isolamentos", "preco": 14.99},
    9: {"nome": "ferro", "preco": 8.78, "almoxarifado": "Ferro"},
    10: {"nome": "viga", "preco": 9.65, "almoxarifado": "Viga"},
    11: {"nome": "brita", "preco": 6.44, "almoxarifado": "Brita"},
    12: {"nome": "tabua", "preco": 5.32, "almoxarifado": "Tabua"},
    13: {"nome": "concreto", "preco": 9.87, "almoxarifado": "Concreto"}
}

# Função para calcular o custo total
def calcular_custo(codigo, quantidade):
    preco_unitario = produtos_precos[codigo]["preco"]
    custo_total = preco_unitario * quantidade
    return custo_total

# Função para sugerir produtos mais sustentáveis
def sugerir_produto_sustentavel(codigo):
    sugestoes = {
        "aço": "Uma alternativa mais sustentável para o aço na construção pode ser o bambu, que é renovável e tem baixo impacto ambiental.",
        "madeira": "Para substituir a madeira, você pode considerar o uso de madeira de reflorestamento certificada, que é mais sustentável.",
        "gesso": "O gesso é um material bastante utilizado, porém para um opção mais sustentável, pode-se considerar o uso de materiais como o barro.",
        "vidro": "Uma alternativa mais sustentável para o vidro na construção pode ser o uso de materiais transparentes à base de polímeros ou até mesmo painéis solares translúcidos.",
        "argamassa": "Para substituir a argamassa, você pode considerar o uso de adobes ou tijolos de barro, que são materiais mais naturais e sustentáveis.",
        "tijolos": "Em vez de tijolos convencionais, você pode considerar o uso de tijolos de solo-cimento, que são mais sustentáveis e têm menor impacto ambiental.",
        "telhas": "Uma alternativa mais sustentável para telhas de cerâmica ou metal pode ser o uso de telhados verdes, que são mais eficientes energeticamente e contribuem para a biodiversidade urbana.",
        "isolamentos": "Em vez de isolamentos convencionais, você pode considerar o uso de isolamentos feitos com materiais reciclados, como papelão ou espuma de celulose."
    }
    produto_atual = produtos_precos[codigo]["nome"]
    return sugestoes.get(produto_atual, "Não há sugestões disponíveis.")

# Função para atualizar o almoxarifado
def atualizar_almoxarifado(codigo, quantidade):
    produto_nome = produtos_precos[codigo].get("almoxarifado")
    if produto_nome in material.getAlmoxarifado():
        return material.atualizarAlmoxarifado(produto_nome, quantidade)
    return True  # Para produtos que não estão gerenciados no almoxarifado

# Interface com o usuário
custo_total_acumulado = 0
continuar = True

print('Itens disponíveis no almoxarifado:')
for item, quantidade in material.getAlmoxarifado().items():
    print(f'{item}: {quantidade}')

while continuar:
    codigo = listamaterialfinal.listaDeMateriais()

    quantidade = int(input("Digite a quantidade desejada: "))

    # Calcular o frete a 15%
    custo_total = calcular_custo(codigo, quantidade)
    
    if atualizar_almoxarifado(codigo, quantidade):
        custo_total_acumulado += custo_total
        print(f"O custo total é: R$ {custo_total:.2f}")
        print(f"Custo total acumulado: R$ {custo_total_acumulado:.2f}")

        if quantidade > 9:
            print("A quantidade solicitada irá exigir um meio de transporte para sua locomoção. Aproveite o nosso frete para produtos a partir de R$50,00")
        else:
            print("Agradecemos a preferência.")

        # Sugerir produto mais sustentável
        sugestao_sustentavel = sugerir_produto_sustentavel(codigo)
        print("Para uma opção mais sustentável, você pode considerar:", sugestao_sustentavel)
    
    resposta = input("Deseja adicionar mais algum produto? (sim/não) ").lower()
    if resposta != "sim":
        continuar = False

print("Obrigado por sua compra!")
print('\nQuantidade restante no almoxarifado após as compras:')
for item, quantidade in material.getAlmoxarifado().items():
    print(f'{item}: {quantidade}')