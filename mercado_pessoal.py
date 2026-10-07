produtos = []

print('''Digite o nome do produto que deseja adicionar na lista.
Digite "remover" para remover um produto da lista.
Digite "sair" finalizar a lista.''')

while True:  
  novo_produto = input('Nome do produto:').capitalize()

  if novo_produto == 'Remover':
    produto_remover = input('Qual produto você quer remover?').capitalize()

    if produto_remover in produtos:
      produtos.remove(produto_remover)
    else:
      print(f'{produto_remover} não está na lista de compras')
    
  if novo_produto == 'Sair':
    break

  if novo_produto != 'Remover':
    produtos.append(novo_produto)
print(f'{produtos}')