lista = []

while True:
    item = input('Adicione algo na lista: ')
    lista.append(item)

    decisao = input('Deseja adicionar outro item? [S]im / [N]ão:' )

    if decisao == 'N':
        print(lista)
        break
    elif decisao == 'S':
        continue
    else:
        print('Opção incorreta')
