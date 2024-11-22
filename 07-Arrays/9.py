# Define the categories and expenses arrays
categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

# Find the maximum expense and its index
max_expense = max(expenses)
max_index = expenses.index(max_expense)

# Find the corresponding category
most_expensive_category = categories[max_index]

# Print the result
print(f"The most expensive category is '{most_expensive_category}' with an expense of ${max_expense}.")
