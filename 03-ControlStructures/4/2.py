###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    buf_ord = ord(char)
    # add one to the character's code
    buf_ord = buf_ord + 1 
    # replace new character code with its
    # corresponding character (use chr())
    
    # add encrypted character to encrypted text
    encrypted_text = encrypted_text + chr(buf_ord)

print(f'plain_text: {plain_text}')
print(f'encrypted_text: {encrypted_text}')