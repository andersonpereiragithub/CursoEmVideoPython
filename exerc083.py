# Crie um programa onde o usuário digite uma expressão qualquer
# que use parênteses. Seu aplicativo deverá analisar se a
# expressão passada está com os parênteses abertos e fechados na
# ordem correta.

pilha = []
expressao = str(input('Digite uma expressão entre parênteses: '))
for parentese in expressao:
    if parentese == '(':
        pilha.append('(')
    elif parentese == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão NÃO está válida!')
