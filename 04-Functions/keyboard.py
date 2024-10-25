###
# Functions to read any data type from the keyboard
#
def input_string(message):
    string = input(message)
    return string

def input_integer(message):
    integer = int(input(message))
    return integer

def input_real(message):
    real = float(input(message))
    return real

def input_boolean(message):
    bn = (input(message))
    result = True
    if bn == 'y' : 
        result = True
    elif bn == 'n': 
        result = False
    return result
