# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.C = 5 * ((F-32) / 9).

fahrenheit = int(input('Digite o valor da temperatura em Fahrenheit que deseja converter para graus Celcius: \n'))

valor = fahrenheit - 32

celcius = 5 * valor / 9

print(celcius)