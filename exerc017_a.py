#Faça um programa que leia o comprimento do cateto oposto e do
#cateto adjacente de um triângulo retângulo, calcule e mostre
#o comprimento da hipotenusa.
import math
catetoOposto = float(input('Informe o comprimento do Cateto Oposto: '))
catetoAdjacente = float(input('Informe o comprimento do Cateto Adjacente: '))

print('Hipotenusa = {:.2f}' .format(math.sqrt(catetoOposto * catetoOposto + catetoAdjacente * catetoAdjacente)))