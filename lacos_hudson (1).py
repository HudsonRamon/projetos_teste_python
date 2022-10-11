produtos = [] 
def soma(listProds):
    soma = 0
    for prod in listProds:
        preco = prod['price']
        soma += preco
    return soma

def listaProdutos(listProdutos):
    print('Listagem dos produtos')
    print('-'*20)
    for item in listProdutos:
        print(f"{item['name']} -> R${item['price']}")

while True:
    nomeProduto = str(input("Produto: "))
    precoProduto = float(input("Preço: "))
    
    prod = {'name': nomeProduto, 'price': precoProduto}
    produtos.append(prod)
    
    tot = soma(produtos)
    print(f"Total => R${tot}")
    
    cont = str(input("Continuar? [Enter/N] ")).upper()
    print('')
    if(cont == 'N'):
        break

print('')
print('='*20)
listaProdutos(produtos)
print('_'*20)
total = soma(produtos)
print(f"TOTAL -> R${total}")
print("="*25)
print('\nfinish')
