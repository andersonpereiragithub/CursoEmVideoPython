str = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(str))
print('Só tem espaços? ', str.isspace())
print('É um número? ', str.isnumeric())
print('É alfabético? ', str.isalpha())
print('É alfanumérico? ', str.isalnum())
print('Está em maiúsculas? ', str.isupper())
print('Está em minúsculas? ', str.islower())
print('Está capitalizada? ', str.istitle())