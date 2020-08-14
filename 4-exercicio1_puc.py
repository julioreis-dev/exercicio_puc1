def maior(lista):
    numero = lista[0][0]
    altura = lista[0][1]
    for aluno2 in range(1, len(lista)):
        altura2 = lista[aluno2][1]
        if altura2 > altura:
            numero = lista[aluno2][0]
            altura = altura2
    return numero, altura


def menor(lista1):
    numero1 = lista1[0][0]
    altura1 = lista1[0][1]
    for aluno3 in range(1, len(lista1)):
        altura3 = lista1[aluno3][1]
        if altura3 < altura1:
            numero1 = lista1[aluno3][0]
            altura1 = altura3
    return numero1, altura1


lista_aluno = [(1, 2.2), (2, 1.8), (3, 2.32), (4, 2.12), (5, 2.1), (6, 1.97), (7, 1.81), (8, 1.48),
               (9, 1.93), (10, 2.33), (11, 1.94)]
resultado_maior = maior(lista_aluno)
resultado_menor = menor(lista_aluno)
print(f'O aluno {resultado_maior[0]} é o maior aluno com a altura de {resultado_maior[1]}cm')
print(f'O aluno {resultado_menor[0]} é o menor aluno com a altura de {resultado_menor[1]}cm')
