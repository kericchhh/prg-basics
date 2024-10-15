###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"
capitals = movie.upper()
lower = movie.lower()
e_count = movie.count('e')
lord = movie.find('Lord')
dragon = movie.find('dragon')

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print(f'The title in capital letters: ', capitals)

# print title in small letters
print(f'The title in small letters: ', lower)

# print how many times the vowel "e" appears in the title
print(f'how many times the vowel "e" appears in the title:', e_count)

# print where in the text is the word "Lord"
print(f'where in the text is the word "Lord": ', lord)

# print where in the text is the word "dragon"
print(f'where in the text is the word "dragon": ', dragon)