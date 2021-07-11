#Desenvolva um programa que leia seis núeros inteiros e
#mostre a soma apenas daqueles que forem pares. Se o valor
#digita for ímpar, desconsidere-o.

soma = 0
for c in range(1, 7):
    num = int(input('Informe o {}o. número: ' .format(c)))
    if num % 2 == 0:
        soma += num
print('A soma dos números pares são {}.' .format(soma))