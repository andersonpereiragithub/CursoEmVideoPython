#Nessa aula, vamos aprender o que são LISTAS e como utilizar
# listas em Python. As listas são variáveis compostas que
# permitem armazenar vários valores em uma mesma estrutura,
# acessíveis por chaves individuais.

num = (2, 5, 9, 1)
num1 = [2, 5, 3, 1]
num1[2] = 10
num1.append(12)
num1.insert(2, 27)
print(num)
print(num1)
num1.sort()
print(num1)
num1.sort(reverse=True)
print(num1)
num1.pop(0)
print(num1)
num1.remove(12)
print(num1)