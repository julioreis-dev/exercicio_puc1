def fechar(lista):
    soma = 0
    for k in lista:
        soma = soma + k
    return soma


arg = True
n = 0
lista_compras = []
while arg:
    valor = float(input(f'Produto {n+1}:R$ '))
    if valor != 0:
        lista_compras.append(valor)
        n = n + 1
    else:
        arg = False

flag = True
while flag:
    valor_final = fechar(lista_compras)
    print(f'Total: R$ {round(valor_final, 2)}')
    dinheiro = float(input('Dinheiro: R$ '))
    if valor_final > dinheiro:
        print('insufficient funds to pay the purchase!!!')
    else:
        print(f'Troco:R$ {round(dinheiro-valor_final, 2)}'
              '\nThank you so munch!!!')

        flag = False
