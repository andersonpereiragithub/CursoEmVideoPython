#Desenvolva um lógica que leia o peso e a altura de uma
#pessoa, calcule seu IMC e mostre seu status, de acordo
#com a tabela abaixo:
#Abaixo de  18.5: Abaixo do peso;
#Entre 18.5 e 25: Peso ideal;
#25 até 30: Sobrepeso;
#30 até 40: Obseidade;
#Acima de 40: Obsidade mórbida;

peso = float(input('Inferme o Peso: '))
altura = float(input('Inferme o Altura: '))

imc = peso / (altura * altura)
if imc < 18.5:
    print('Abaixo do peso com {:.2f} de IMC.' .format(imc))
elif imc < 25:
    print('Peso IDEAL com {:.2f} de IMC' .format(imc))
elif imc < 30:
    print('Sobrepeso com {:.2f} de IMC'.format(imc))
elif imc < 40:
    print('Obesidade com {:.2f} de IMC'.format(imc))
else:
    print('Obesidade Mórbida com {:.2f} de IMC'.format(imc))