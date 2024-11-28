names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest_name = " "
max_lenght = 0

for name in names: 
    if len(name) > max_lenght : 
        longest_name = name 
        max_lenght = len(name)

print("Names: ", ' '.join(names))
print("Longest name: ", longest_name)