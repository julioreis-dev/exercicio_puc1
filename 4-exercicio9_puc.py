def corrigir(lista_answ):
    pergunta = 0
    lista_pontuacao = []
    while pergunta < 10:
        resposta = input(f'Qual é a resposta da questão {pergunta + 1}?')
        lista_opc = ['a', 'b', 'c', 'd', 'e']
        if resposta.lower() in lista_opc:
            if lista_answ[pergunta] == resposta:
                lista_pontuacao.append('certo')
            else:
                lista_pontuacao.append('errado')
            pergunta = pergunta + 1
        else:
            print('Opção incorreta!!!')
    return lista_pontuacao


def calcular_media(lista1):
    valor = 0
    for n in lista1:
        valor = valor + n
    media = valor/len(lista1)
    return media


lista_gabarito = ['a', 'a', 'c', 'd', 'e', 'd', 'b', 'b', 'c', 'b']
lista_notaturma = []
arg = True
while arg:
    correcao = corrigir(lista_gabarito)
    notas = correcao.count('certo')
    lista_notaturma.append(notas)
    arg1 = True
    while arg1:
        question = input('\nDeseja continuar incluindo nota de aluno?\nPressione "S" pra continuar ou "N" para sair')
        if question.lower() == 's':
            arg1 = False
        elif question.lower() == 'n':
            arg = False
            arg1 = False
        else:
            print('Opção incorreta')
resumo = lista_notaturma
media_turma = calcular_media(resumo)
print(f'Maior nota obteve {max(resumo)} acertos'
      f'\nMenor nota obteve {min(resumo)} acertos'
      f'\nTotal de alunos que utilizaram o sistema foi de {len(resumo)} alunos'
      f'\nA média das notas da turma foi de {media_turma}')
print('\nGabarito da Prova')
numero = 0
for t in lista_gabarito:
    print(f'{numero+1} - {t}')
    numero = numero + 1
