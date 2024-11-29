# Initialize a word count variable
total_word_count = 0

# Open the file and process each line
with open('pets.txt', 'r') as file:
    for line in file:
        # Print the current line
        print(line, end="")  # end="" to avoid double newlines

        # Count the words in the line
        word_count = len(line.split())
        total_word_count += word_count

# Print the total word count
print(f"\n\nTotal number of words: {total_word_count}")
