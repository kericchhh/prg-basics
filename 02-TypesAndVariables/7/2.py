###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.

#Input in celsius 
celsius = int(input('Enter degrees in ceclcius: '))

#Conversion into fahrenheit
fahrenheit = celsius * (9 / 5) + 32

#Conversion into Kelvin
kelvin = celsius + 273.15

#Printing results
print(f'Celcius: {celsius}')
print(f'Fahrenheit: {fahrenheit}')
print(f'Kelvin: {kelvin}')


