def analisar(lista):
    maximo = max(lista)
    minimo = min(lista)
    lista.remove(maximo)
    lista.remove(minimo)
    soma = 0
    for j in lista:
        soma = soma + j
    media = soma/len(lista)
    return maximo, minimo, media


atleta = input('Nome do atleta: ')
lista_salto = []
n = 0
while n < 8:
    salto = float(input(f'{n+1}º salto, Nota: '))
    lista_salto.append(salto)
    n = n + 1

print(f'\nAtleta: {atleta}')
for t in lista_salto:
    print(f'Nota: {t}')
resultado_final = analisar(lista_salto)
print('\nResultado Final:'
      f'\nAtleta: {atleta}'
      f'\nMelhor Salto: {resultado_final[0]}'
      f'\nPior Salto: {resultado_final[1]}'
      f'\nMédia: {round(resultado_final[2], 2)}')
