###
# A program that prints your height both in cm and in feet and inches.
#
import math
cm = int(input(f'Enter your height in cm: '))
feet = int(math.ceil(cm * 0.0328))
inches =int(math.ceil(cm * 0.3937))
print(f'I am {cm}cm tall, that makes me {feet} feet and {inches} inches')