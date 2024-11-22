# Weekly expenses for different categories
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

category_totals = [0, 0 , 0]
week_totals = [0, 0, 0, 0]
monthly_total = 0
# Calculates expenses
for week_index, week in enumerate(monthly_expenses):
    week_totals[week_index] = sum(week)
# Use loop statements


...
...

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',...)
print('Transport:',...)
print('Utilities:',...)
print('Week 1:',...)
print('Week 2:',...)
print('Week 3:',...)
print('Week 4:',...)
print('---------------')
print('TOTAL:',...)