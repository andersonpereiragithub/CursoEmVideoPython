#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(* num, sit = False):
    """
    -> Função para analisar as notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita variação de quantidade)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    infoGeral = {}
    infoGeral['total'] = len(num)
    infoGeral['maior'] = max(num)
    infoGeral['menor'] = min(num)
    infoGeral['media'] = sum(num) / len(num)
    if sit:
        if infoGeral['media'] >= 7:
            infoGeral['situacao'] = 'BOM'
        elif infoGeral['media'] >= 5:
            infoGeral['situacao'] = 'RAZOÁVEL'
        else:
            infoGeral['situacao'] = 'RUIM'
    return infoGeral

resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)