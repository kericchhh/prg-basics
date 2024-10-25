###
# Calculates the sum of the digits in a number
#
import math
def sum_digits(number):
    number = abs(number)
    string_num = str(number)
    sum = 0
    for i in range(len(string_num)):
        sum += int(string_num[i])
    return sum

any_number = int(input('Enter integer number: '))

result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')