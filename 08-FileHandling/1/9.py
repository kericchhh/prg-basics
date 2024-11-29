# Prints employees employed in a specified position.

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

# Open the file and process it line by line
with open(file_name, 'r') as file:
    # Initialize a counter for numbering
    count = 1

    # Iterate over each line in the file
    for line in file:
        # Check if the job title exists in the current line
        if job_title in line:
            # Print the line with numbering
            print(f"{count}. {line.strip()}")
            count += 1
