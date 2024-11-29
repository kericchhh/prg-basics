###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file, 'r') as line:
   content = line.read()
   lines = content.splitlines()
   with open(position_file, 'w') as line_2:
      for line in lines:
         if job_title in line:
            line_2.write(f"{line}\n")