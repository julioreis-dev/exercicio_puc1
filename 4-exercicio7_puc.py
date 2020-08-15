def tall(lista):
    cod1 = 0
    hgh1 = 0
    wght1 = 0
    for n in lista:
        cod_ver = n[0]
        hgh_ver = n[1]
        wght_ver = n[2]
        if hgh_ver > hgh1:
            cod1 = cod_ver
            hgh1 = hgh_ver
            wght1 = wght_ver
    return cod1, hgh1, wght1


def small(lista):
    cod1 = 3000
    hgh1 = 3000
    wght1 = 3000
    for n in lista:
        cod_ver = n[0]
        hgh_ver = n[1]
        wght_ver = n[2]
        if hgh_ver < hgh1:
            cod1 = cod_ver
            hgh1 = hgh_ver
            wght1 = wght_ver
    return cod1, hgh1, wght1


def fat(lista):
    cod1 = 0
    hgh1 = 0
    wght1 = 0
    for n in lista:
        cod_ver = n[0]
        hgh_ver = n[1]
        wght_ver = n[2]
        if wght_ver > wght1:
            cod1 = cod_ver
            hgh1 = hgh_ver
            wght1 = wght_ver
    return cod1, hgh1, wght1


def thin(lista):
    cod1 = 3000
    hgh1 = 3000
    wght1 = 3000
    for n in lista:
        cod_ver = n[0]
        hgh_ver = n[1]
        wght_ver = n[2]
        if wght_ver < wght1:
            cod1 = cod_ver
            hgh1 = hgh_ver
            wght1 = wght_ver
    return cod1, hgh1, wght1


def average_hgh(lista):
    sun = 0
    for n in lista:
        sun = sun + n[1]
    return sun/len(lista)


def average_wgh(lista):
    sun = 0
    for n in lista:
        sun = sun + n[2]
    return sun/len(lista)


arg = True
lista_general = []
while arg:
    cod = float(input('Type your code? '))
    if cod != 0:
        hgh = float(input('Type your Height?'))
        wght = float(input('Type your Weight? '))
        tupla_data = (cod, hgh, wght)
        lista_general.append(tupla_data)
    else:
        arg = False

x = tall(lista_general)
y = small(lista_general)
w = fat(lista_general)
t = thin(lista_general)
f = average_hgh(lista_general)
h = average_wgh(lista_general)

print(f'The tall client is {x[0]} with {x[1]}cm')
print(f'The small client is {y[0]} with {y[1]}cm')
print(f'The fat client is {w[0]} with {w[2]}KG')
print(f'The thing client is {t[0]} with {t[2]}KG')
print(f'The Height average is {round(f, 2)}')
print(f'The Weight average is {round(h, 2)}')
