###
# A program that checks whether the password length
# read from the keyboard is correct.
#
password = input('Enter password: ')
password_ok = len(password) >= 8
password_short = len(password) < 8
print(f'Password length is valid: {password_ok}')
print(f'Password lenght is too short: {password_short}')