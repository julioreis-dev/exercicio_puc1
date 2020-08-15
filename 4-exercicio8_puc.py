def analisar(lista):
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    for number in lista:
        if number in range(0, 25):
            l1.append(number)
        elif number in range(26, 50):
            l2.append(number)
        elif number in range(51, 75):
            l3.append(number)
        elif number in range(76, 100):
            l4.append(number)
    return len(l1), len(l2), len(l3), len(l4)


lista_resultado = []
flag = True
while flag:
    numero = int(input('Digite um numero: '))
    if numero > 0:
        lista_resultado.append(numero)
    else:
        flag = False

final = analisar(lista_resultado)
print(f'No intervalo [0-25] tem: {final[0]} numeros'
      f'\nNo intervalo [26-50] tem: {final[1]} numeros'
      f'\nNo intervalo [51-75] tem: {final[2]} numeros'
      f'\nNo intervalo [76-100] tem: {final[3]} numeros')


